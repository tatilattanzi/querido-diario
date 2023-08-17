from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorPortalFacil(Mapeador):
    name = "mapeadorportalfacil"

    custom_settings = {"CONCURRENT_REQUESTS": 25}

    def column(self):
        return "PFACIL_URL"

    def backup_column(self):
        return "VALID_PFACIL"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.manhuacu.mg.gov.br/diario-eletronico
        # https://www.saojosederibamar.ma.gov.br/diario-eletronico

        return [f"{protocol}://www.{city}.{state_code}.gov.br/diario-eletronico"]

    def validation(self, response):
        if "portalfacil.com.br" in response.text:
            return True
        return False
