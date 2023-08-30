from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorTrestecnos(Mapeador):
    name = "mapeadortrestecnos"

    def column(self):
        return "TREST"

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
        if "3tecnos.com.br" in response.text or "3Tecnos.com.br" in response.text:
            if "indisponivel" not in response.url:
                if "O serviço solicitado está indisponível" not in response.text:
                    return True
        return False
