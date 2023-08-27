from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorSistC(Mapeador):
    name = "mapeadorsistc"

    def column(self):
        return "SISTC"

    def backup_column(self):
        return "VALID_SISTC"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # http://www.auroradotocantins.to.gov.br/transparencia/diarioeletronico/
        # http://www.pontealtadobomjesus.to.gov.br/transparencia/diarioeletronico/

        return [
            f"{protocol}://www.{city}.{state_code}.gov.br/transparencia/diarioeletronico/"
        ]

    def validation(self, response):
        if "scMenuTHeaderFont" in response.text:
            return True
        return False
