from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDOBR(Mapeador):
    name = "mapeadordobr"

    custom_settings = {
        "CONCURRENT_REQUESTS": 50,
    }

    def column(self):
        return "DOBR_URL"

    def backup_column(self):
        return "VALID_DOBR"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://tocantinia.diariooficialbr.com.br/
        # https://diariooficial.aguiarnopolis.to.gov.br/
        # https://miracema.diariooficialbr.com.br/

        lista = [
            f"{protocol}://diariooficial.{city}.{state_code}.gov.br/",
            f"{protocol}://{city}.diariooficialbr.com.br",
        ]
        return lista

    def validation(self, response):
        if "ooka.com.br" in response.text:
            return True
        return False
