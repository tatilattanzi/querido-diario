from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDkc(Mapeador):
    name = "mapeadordkc"

    custom_settings = {"CONCURRENT_REQUESTS": 50}

    def column(self):
        return "DKC_URL"

    def backup_column(self):
        return "VALID_DKC"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.lizarda.to.gov.br/diariooficial
        # https://www.goianorte.to.gov.br/diariooficial

        return [f"{protocol}://www.{city}.{state_code}.gov.br/diariooficial"]

    def validation(self, response):
        if "Termos de uso |" in response.text:
            if "Mantido por" in response.text:
                if "dkc-logo" in response.text:
                    return True
        return False
