from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorMegas(Mapeador):
    name = "mapeadormegas"

    custom_settings = {"CONCURRENT_REQUESTS": 25}

    def column(self):
        return "MEGAS_URL"

    def backup_column(self):
        return "VALID_MEGAS"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://brejinhodenazare.to.gov.br/diariooficial/
        # https://arraias.to.gov.br/diariooficial/

        return [f"{protocol}://{city}.{state_code}.gov.br/diariooficial"]

    def validation(self, response):
        if "grupomegas.com" in response.text:
            return True
        return False
