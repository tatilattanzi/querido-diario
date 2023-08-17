import csv
import time
from pathlib import Path

import scrapy
from unidecode import unidecode  # não existe nos requirements


class Mapeador(scrapy.Spider):
    ## TODO: acertar a documentação

    """
    Class base para Mapeadores (Em Processo)
    """

    name = "mapeador"
    territories = []
    protocols = ["http", "https"]

    def start_requests(self):
        self.read_csv("dados_mapeamento")
        self.add_column_key()  # add new key to data dict. Valid urls found will be placed here

        for i in range(len(self.territories)):
            self.log(i)

            name, state_code = self.format_str(
                self.territories[i]["name"], self.territories[i]["state_code"]
            )
            for protocol_option in self.protocols:
                for name_option in self.city_name_generator(name):
                    for url_option in self.urls_pattern(
                        protocol_option, name_option, state_code
                    ):
                        yield scrapy.Request(
                            url_option, callback=self.parse, cb_kwargs=dict(index=i)
                        )

        self.save_csv("dados_mapeamento")

    def parse(self, response, index):
        if self.validation(response):
            if response.url not in self.territories[index][self.column()]:
                self.territories[index][self.column()].append(response.url)
        elif response.url not in self.territories[index][self.backup_column()]:
            self.territories[index][self.backup_column()].append(response.url)

    def city_name_generator(self, city_name):
        combination_list = []

        combination_list.append(self.remove_blankspaces(city_name))  # cityname
        combination_list.append(self.blankspaces_to_underline(city_name))  # city_name
        combination_list += self.name_parts(city_name)  # city / name

        # combination_list += self.name_abbreviation(city_name)  # cname
        # combination_list += self.add_pm_to_names(combination_list) #pm + all above

        return combination_list

    def format_str(self, name, state_code):
        name = unidecode(name).strip().lower().replace("-", " ").replace("'", "")
        state_code = unidecode(state_code).strip().lower()
        return name, state_code

    def remove_blankspaces(self, name):
        return name.replace(" ", "")

    def blankspaces_to_underline(self, name):
        return name.replace(" ", "_")

    def name_parts(self, name):
        parts = name.split()
        for n in parts:
            if n in ["da", "de", "do"]:
                parts.remove(n)
        return parts

    def name_abbreviation(self, city_name):
        # problema: d'agua está virando dagua no codigo, chega aqui usando d no split e nao a
        subnames = city_name.split()
        abbrev_list = []

        if len(subnames) > 1:
            begin = ""
            end = ""
            for i in range(len(subnames)):
                if subnames[i] not in ["da", "de", "do"]:
                    begin += subnames[i][0]
                    for y in range(i + 1, len(subnames)):
                        if subnames[y] not in ["da", "de", "do"]:
                            end += subnames[y]
                    abbrev = begin + end
                    if len(abbrev) > 3:
                        abbrev_list.append(abbrev)
                    end = ""

        return abbrev_list

    def add_pm_to_names(self, list_names):
        aux = []
        for name in list_names:
            aux.append(f"pm{name}")
        return aux

    def add_column_key(self):
        column = self.column()
        bcolumn = self.backup_column()
        for y in range(len(self.territories)):
            self.territories[y][column] = []
            self.territories[y][bcolumn] = []

    def save_csv(self, file_name):
        file_path = (Path(__file__).parent / f"../../../{file_name}.csv").resolve()

        with open(file_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=list(self.territories[0].keys())
            )
            writer.writeheader()
            for i in range(len(self.territories)):
                writer.writerow(self.territories[i])
        csvfile.close()

    def read_csv(self, file_name):
        if (Path(__file__).parent / f"../../../{file_name}.csv").is_file():
            file_path = (Path(__file__).parent / f"../../../{file_name}.csv").resolve()
        else:
            file_path = (
                Path(__file__).parent / "../../resources/territories.csv"
            ).resolve()

        with open(file_path, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.territories.append(row)
        csvfile.close()

    def log(self, i):
        if i % 100 == 0:
            print(f"[{i}/5570] {time.strftime('%H:%M:%S', time.localtime())}")
        if i % 1000 == 0:
            print(
                f"[BACKUP PARCIAL] Salvando dados parciais... {i}/{len(self.territories)}"
            )
            self.save_csv(f"[PARCIAL][{self.column()}] dados_mapeamento-{i}-5570")
