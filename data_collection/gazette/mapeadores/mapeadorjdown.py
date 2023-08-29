from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorJdown(Mapeador):
    name = "mapeadorjdown"

    def column(self):
        return "JDOWN"

    def backup_column(self):
        return "VALID_JDOWN"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://diariooficial.taipas.to.gov.br/index.php/publicacoes

        return [
            f"{protocol}://diariooficial.{city}.{state_code}.gov.br/index.php/publicacoes"
        ]

    def validation(self, response):
        if "jDownloads.com" in response.text or "jdownloads.com" in response.text:
            return True
        return False
