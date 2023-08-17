from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorAplus(Mapeador):
    name = "mapeadoraplus"

    custom_settings = {"CONCURRENT_REQUESTS": 25}

    def column(self):
        return "APLUS_URL"

    def backup_column(self):
        return "VALID_APLUS"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.bacabal.ma.gov.br/diario
        # https://www.codo.ma.gov.br/diario

        return [f"{protocol}://www.{city}.{state_code}.gov.br/diario/"]

    def validation(self, response):
        if "agenciaplus.com.br" in response.text:
            return True
        return False
