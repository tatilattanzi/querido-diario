from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorSistB(Mapeador):
    name = "mapeadorsistb"

    def column(self):
        return "SISTB"

    def backup_column(self):
        return "VALID_SISTB"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://transparencia.altoalegredomaranhao.ma.gov.br/diario
        # https://transparencia.santaluzia.ma.gov.br/diario

        lista = [f"{protocol}://transparencia.{city}.{state_code}.gov.br/diario"]
        return lista

    def validation(self, response):
        if "Edições Anteriores" in response.text and 'id="datahora"' in response.text:
            return True
        return False
