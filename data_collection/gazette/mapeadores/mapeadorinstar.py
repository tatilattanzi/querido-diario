from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorInstar(Mapeador):
    name = "mapeadorinstar"

    def column(self):
        return "INSTAR"

    def backup_column(self):
        return "VALID_INSTAR"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.valinhos.sp.gov.br/portal/diario-oficial
        # https://www.vinhedo.sp.gov.br/portal/diario-oficial

        return [f"{protocol}://www.{city}.{state_code}.gov.br/portal/diario-oficial"]

    def validation(self, response):
        if "Instar Tecnologia" in response.text or "instar.com.br" in response.text:
            if "Nenhum diário oficial encontrado" not in response.text:
                if "diario-oficial" in response.url:
                    return True
        return False
