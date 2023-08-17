from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDalins(Mapeador):
    name = "mapeadordalins"

    custom_settings = {"CONCURRENT_REQUESTS": 100}

    def column(self):
        return "DALINS_URL"

    def backup_column(self):
        return "VALID_DALINS"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://cachoeirinha.to.gov.br/diariooficial
        # https://saobentodotocantins.to.gov.br/diariooficial

        return [f"{protocol}://{city}.{state_code}.gov.br/diariooficial"]

    def validation(self, response):
        if "datalins.com.br" in response.text:
            return True
        return False
