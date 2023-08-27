from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorPortalFacil(Mapeador):
    name = "mapeadorportalfacil"

    def column(self):
        return "PORTALFACIL"

    def backup_column(self):
        return "VALID_PORTALFACIL"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.manhuacu.mg.gov.br/diario-eletronico
        # https://www.saojosederibamar.ma.gov.br/diario-eletronico

        return [f"{protocol}://www.{city}.{state_code}.gov.br/diario-eletronico"]

    def validation(self, response):
        if "portalfacil.com.br" in response.text:
            if "pagina-nao-encontrada" not in response.url:
                return True
        return False
