from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorSiasp(Mapeador):
    name = "mapeadorsiasp"

    custom_settings = {
        "CONCURRENT_REQUESTS": 50,
    }

    def column(self):
        return "SIASP_URL"

    def backup_column(self):
        return "VALID_SIASP"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.taboleirogrande.rn.gov.br/diario.php

        return [f"{protocol}://www.{city}.{state_code}.gov.br/diario.php"]

    def validation(self, response):
        if "siasp.com.br" in response.text:
            return True
        return False
