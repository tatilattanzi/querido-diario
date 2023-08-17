from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorSaiio(Mapeador):
    name = "mapeadorsaiio"

    custom_settings = {"CONCURRENT_REQUESTS": 16}

    def column(self):
        return "SAIIO_URL"

    def backup_column(self):
        return "VALID_SAIIO"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://sai.io.org.br/al/penedo/Site/DiarioOficial
        # https://diariooficial.ourolandia.ba.gov.br/Site/DiarioOficial

        lista = [
            f"{protocol}://sai.io.org.br/{state_code}/{city}/Site/DiarioOficial",
            f"{protocol}://diariooficial.{city}.{state_code}.gov.br/Site/DiarioOficial",
        ]
        return lista

    def validation(self, response):
        if "imap.org.br" in response.text:
            return True
        return False
