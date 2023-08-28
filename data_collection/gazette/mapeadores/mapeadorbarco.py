from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorBarco(Mapeador):
    name = "mapeadorbarco"

    def column(self):
        return "BARCO"

    def backup_column(self):
        return "VALID_BARCO"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # http://diariooficial.pontealtadotocantins.to.gov.br/diariooficial
        # https://www.silvanopolis.to.gov.br/diariooficial

        lista = [
            f"{protocol}://diariooficial.{city}.{state_code}.gov.br/diariooficial",
            f"{protocol}://www.{city}.{state_code}.gov.br/diariooficial",
        ]
        return lista

    def validation(self, response):
        if "barcodigital.com.br" in response.text:
            if "Ultima Edição" in response.text or "Última Edição" in response.text:
                return True
        return False
