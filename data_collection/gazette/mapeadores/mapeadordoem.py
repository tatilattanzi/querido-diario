from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorDoem(Mapeador):
    name = "mapeadordoem"

    custom_settings = {
        "CONCURRENT_REQUESTS": 100,
    }

    def column(self):
        return "DOEM_URL"

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
                        return True
        return False
