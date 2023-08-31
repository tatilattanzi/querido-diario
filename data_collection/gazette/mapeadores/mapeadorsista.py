from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorSistA(Mapeador):
    name = "mapeadorsista"

    def column(self):
        return "SISTA"

    def backup_column(self):
        return "VALID_SISTA"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://do.corumba.ms.gov.br/
        # http://diariodomunicipio.sjc.sp.gov.br/

        lista = [
            f"{protocol}://do.{city}.{state_code}.gov.br/",
            f"{protocol}://diariodomunicipio.{city}.sp.gov.br/",
        ]
        return lista

    def validation(self, response):
        if (
            "previewsDO p-2 mt-3" in response.text
            or "suporte@autopage.inf.br" in response.text
        ):
            return True
        return False
