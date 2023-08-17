from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorGeddoem(Mapeador):
    name = "mapeadorgeddoem"

    custom_settings = {
        "CONCURRENT_REQUESTS": 50,
    }

    def column(self):
        return "GEDDOEM_URL"

    def backup_column(self):
        return "VALID_GEDDOEM"  # ruim de fazer triagem pq tem mt site de transparencia

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://www.acessoinformacao.com.br/ba/jacobina/
        # https://acessoainformacao.coaraci.ba.gov.br/
        # https://transparencia.capimgrosso.ba.gov.br/

        lista = [
            f"{protocol}://www.acessoinformacao.com.br/{state_code}/{city}",
            f"{protocol}://acessoainformacao.{city}.{state_code}.gov.br",
            f"{protocol}://transparencia.{city}.{state_code}.gov.br",
        ]
        return lista

    def validation(self, response):
        if "ibdm" in response.text or "GEDDOEM" in response.text:
            if "Nenhum diário encontrado" in response.text:
                return True
        return False
