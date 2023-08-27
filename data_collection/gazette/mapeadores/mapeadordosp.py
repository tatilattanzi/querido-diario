from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDosp(Mapeador):
    name = "mapeadordosp"

    def column(self):
        return "DOSP"

    def backup_column(self):
        return "VALID_DOSP"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://imprensaoficialmunicipal.com.br/adolfo
        # https://imprensaoficialmunicipal.com.br/guaracai

        return [f"{protocol}://www.imprensaoficialmunicipal.com.br/{city}"]

    def validation(self, response):
        if "dosp.com.br" in response.text:
            if "FILTRO POR DATA" in response.text:
                return True
        return False
