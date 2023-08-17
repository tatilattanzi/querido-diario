from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorNucleogov(Mapeador):
    name = "mapeadornucleogov"

    custom_settings = {"CONCURRENT_REQUESTS": 75}

    def column(self):
        return "NUCGOV_URL"

    def backup_column(self):
        return "VALID_NUCGOV"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://diariooficial.valparaisodegoias.go.gov.br/
        # https://dom.pirenopolis.go.gov.br/
        # https://diariooficial.jau.to.gov.br/

        lista = [
            f"{protocol}://diariooficial.{city}.{state_code}.gov.br/",
            f"{protocol}://dom.{city}.{state_code}.gov.br/",
        ]
        return lista

    def validation(self, response):
        if "nucleogov.com.br" in response.text:
            return True
        return False
