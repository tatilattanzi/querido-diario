import re

import scrapy
from unidecode import unidecode

from gazette.mapeadores.base.mapeador import Mapeador

# TODO: emendei aqui um código que tinha em outro contexto. Precisa revisar.


class MapeadorSigpub(Mapeador):
    name = "mapeadorsigpub"

    associacoes = {
        "aam": "AM",
        "ama": "AL",
        "bahia": "BA",
        "amurc": "BA",
        "aprece": "CE",
        "agm": "GO",
        "fgm": "GO",
        "amm-mg": "MG",
        "amm-mt": "MT",
        "ms": "MS",
        "famep": "PA",
        "famup": "PB",
        "amp": "PR",
        "amupe": "PE",
        "appm": "PI",
        "aemerj": "RJ",
        "femurn": "RN",
        "amr": "RR",
        "arom": "RO",
        "famurs": "RS",
        "sergipe": "SE",
        "apm": "SP"
        # monte alto, sp
        # macatuba
    }

    def start_requests(self):
        self.read_csv("dados_mapeamento")
        self.add_column_key()

        for association in self.associacoes.keys():
            yield scrapy.Request(
                self.urls_pattern(association),
                callback=self.parsesigpub,
                cb_kwargs=dict(assoc=association),
            )

        self.save_csv("dados_mapeamento")

    def parsesigpub(self, response, assoc):
        lista = response.text.split("\n")

        municipios = []
        for item in lista:
            if "Prefeitura" in item:
                municipios += re.findall(
                    r">Prefeitura\s*Municipal\s*de\s*([-\w\s]*)</option>", item
                )
            if "Município" in item:
                municipios += re.findall(r">Município\s*de\s*([-\w\s]*)</option>", item)

        for i in range(len(municipios)):
            municipios[i] = unidecode(
                municipios[i]
            ).lower()  # retira acentuação e torna caixa baixa
        self.relation(self.associacoes[assoc], municipios, assoc)

    def relation(self, state_code, cities_list, assoc):
        for j in range(len(self.territories)):
            if state_code in self.territories[j]["state_code"]:
                if unidecode(self.territories[j]["name"]).lower() in cities_list:
                    self.territories[j][self.column()].append(assoc)

    def column(self):
        return "SIGPUB"

    def backup_column(self):
        return "VALID_SIGPUB"

    def urls_pattern(self, association):
        return f"https://www.diariomunicipal.com.br/{association}/pesquisar/"
