from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorSemnome(Mapeador):
    name = "mapeadorsemnome"

    custom_settings = {"CONCURRENT_REQUESTS": 25}

    def column(self):
        return "SEMNOME_URL"

    def backup_column(self):
        return "VALID_SEMNOME"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # http://www.auroradotocantins.to.gov.br/transparencia/diarioeletronico/
        # http://www.pontealtadobomjesus.to.gov.br/transparencia/diarioeletronico/

        return [
            f"{protocol}://www.{city}.{state_code}.gov.br/transparencia/diarioeletronico/"
        ]

    def validation(self, response):
        if "Histórico Resumido:" in response.text and "Anexo" in response.text:
            return True
        return False
