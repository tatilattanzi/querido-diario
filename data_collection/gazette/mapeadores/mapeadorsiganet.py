from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorSiganet(Mapeador):
    name = "mapeadorsiganet"

    def column(self):
        return "SIGANET"

    def backup_column(self):
        return "VALID_SIGANET"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://balsas.ma.gov.br/diario/diario
        # https://transparencia.beneditoleite.ma.gov.br/acessoInformacao/diario/diario

        lista = [
            f"{protocol}://{city}.{state_code}.gov.br/diario/diario",
            f"{protocol}://transparencia.{city}.{state_code}.gov.br/acessoInformacao/diario/diario",
        ]
        return lista

    def validation(self, response):
        if "siganet" in response.text:
            if ".org" not in response.url:
                return True
        return False
