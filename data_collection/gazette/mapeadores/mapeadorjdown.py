from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorJdown(Mapeador):
    name = "mapeadorjdown"

    custom_settings = {
        "CONCURRENT_REQUESTS": 50,
    }

    def column(self):
        return "JDOWN_URL"

    def backup_column(self):
        return "VALID_JDOWN"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://diariooficial.taipas.to.gov.br/index.php/publicacoes

        return [
            f"{protocol}://diariooficial.{city}.{state_code}.gov.br/index.php/publicacoes"
        ]

    def validation(self, response):
        if "jdownloads.com" in response.text:
            return True
        return False
