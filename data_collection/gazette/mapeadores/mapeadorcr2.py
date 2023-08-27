from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorCR2(Mapeador):
    name = "mapeadorcr2"

    def column(self):
        return "CR2"

    def backup_column(self):
        return "VALID_CR2"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://vigia.pa.gov.br/c/publicacoes/diario-oficial/
        # https://altamira.pa.gov.br/c/publicacoes/diario-oficial/

        return [f"{protocol}://{city}.{state_code}.gov.br/c/publicacoes/diario-oficial"]

    def validation(self, response):
        if "Desenvolvido por CR2" in response.text or "logo-cr2" in response.text:
            return True
        return False
