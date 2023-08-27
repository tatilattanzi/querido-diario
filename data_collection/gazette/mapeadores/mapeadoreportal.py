from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorEPortal(Mapeador):
    name = "mapeadoreportal"

    custom_settings = {"CONCURRENT_REQUESTS": 50}

    def column(self):
        return "EPORTAL_URL"

    def backup_column(self):
        return "VALID_EPORTAL"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.riodosbois.to.gov.br/diariooficial
        # https://www.piraque.to.gov.br/diariooficial

        return [f"{protocol}://www.{city}.{state_code}.gov.br/diariooficial"]

    def validation(self, response):
        if "Termos de uso |" in response.text:
            if "Mantido por" in response.text:
                if "pratica-logo" in response.text:
                    return True
        return False