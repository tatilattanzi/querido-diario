from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorIweb(Mapeador):
    name = "mapeadoriweb"

    custom_settings = {"CONCURRENT_REQUESTS": 25}

    def column(self):
        return "IWEB_URL"

    def backup_column(self):
        return "VALID_IWEB"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.caboverde.mg.gov.br/
        # https://www.muzambinho.mg.gov.br/

        return [f"{protocol}://www.{city}.{state_code}.gov.br"]

    def validation(self, response):
        if "Invicta Web" in response.text:
            return True
        return False
