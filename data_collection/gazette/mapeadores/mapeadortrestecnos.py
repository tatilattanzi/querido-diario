from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorTrestecnos(Mapeador):
    name = "mapeadortrestecnos"

    custom_settings = {
        "CONCURRENT_REQUESTS": 50,
    }

    def column(self):
        return "TREST_URL"

    def backup_column(self):
        return "VALID_TREST"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://aquidaba.se.gov.br/portaltransparencia/?servico=cidadao/diariooficial
        # https://www.municipioonline.com.br/se/prefeitura/japaratuba/cidadao/diariooficial

        return [
            f"{protocol}://{city}.{state_code}.gov.br/portaltransparencia/?servico=cidadao/diariooficial",
            f"{protocol}://www.municipioonline.com.br/{state_code}/prefeitura/{city}/cidadao/diariooficial",
        ]

    def validation(self, response):
        if "3tecnos.com.br" in response.text or "3Tecnos.co.br" in response.text:
            return True
        return False
