from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorVale(Mapeador):
    name = "mapeadorvale"

    custom_settings = {"CONCURRENT_REQUESTS": 50}

    def column(self):
        return "VALE_URL"

    def backup_column(self):
        return "VALID_VALE"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://diario.cristalandia.to.gov.br/
        # https://dom.novaolinda.to.gov.br/

        return [
            f"{protocol}://www.diario.{city}.{state_code}.gov.br/",
            f"{protocol}://dom.{city}.{state_code}.gov.br/",
        ]

    def validation(self, response):
        if "Termos de uso |" in response.text:
            if "Mantido por" in response.text:
                if "vale-solucoes" in response.text:
                    return True
        return False
