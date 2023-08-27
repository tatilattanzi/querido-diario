from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDoem(Mapeador):
    name = "mapeadordoem"

    def column(self):
        return "DOEM"

    def backup_column(self):
        return "VALID_DOEM"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://doem.org.br/ba/acajutiba
        # https://doem.org.br/ba/mascote

        return [f"{protocol}://doem.org.br/{state_code}/{city}"]

    def validation(self, response):
        if "doem.org.br" in response.text:
            if "está Indisponível" not in response.text:
                if "Não foi possível carregar o diário" not in response.text:
                    if "404 - Página não encontrada" not in response.text:
                        if "ibdm.org.br" not in response.url:
                            return True
        return False
