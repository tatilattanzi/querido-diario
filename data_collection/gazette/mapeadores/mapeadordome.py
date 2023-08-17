from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDome(Mapeador):
    name = "mapeadordome"

    custom_settings = {"CONCURRENT_REQUESTS": 25}

    def column(self):
        return "DOME_URL"

    def backup_column(self):
        return "VALID_DOME"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # http://diariooficial.conceicaodotocantins.to.gov.br/
        # http://diariooficial.brasilandiadotocantins.to.gov.br/

        # http://diariooficial.saovalerio.to.gov.br/inicio TODO: n sendo pego pela coleta

        return [f"{protocol}://diariooficial.{city}.{state_code}.gov.br/"]

    def validation(self, response):
        if "DOMe" in response.text:
            return True
        return False
