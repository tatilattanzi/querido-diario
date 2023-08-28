from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDome(Mapeador):
    name = "mapeadordome"

    def column(self):
        return "DOME"

    def backup_column(self):
        return "VALID_DOME"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # http://diariooficial.conceicaodotocantins.to.gov.br/
        # http://diariooficial.brasilandiadotocantins.to.gov.br/
        # http://diariooficial.saovalerio.to.gov.br/inicio

        return [f"{protocol}://diariooficial.{city}.{state_code}.gov.br/"]

    def validation(self, response):
        if "DOMe" in response.text:
            return True
        return False
