from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorMaxima(Mapeador):
    name = "mapeadormaxima"

    custom_settings = {"CONCURRENT_REQUESTS": 75}

    def column(self):
        return "MAX_URL"

    def backup_column(self):
        return "VALID_MAX"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://assuncao.pb.gov.br/publicacoes/boletim-oficial
        # https://boqueirao.pb.gov.br/publicacoes/jornal-oficial
        # https://caturite.pb.gov.br/publicacoes/diario-oficial

        # TODO: notar que ao fim muda. Abstrai pra parte comum. Precisa validar se está bom, ou se tem que destrinchar os 3 casos.

        lista = [f"{protocol}://{city}.{state_code}.gov.br/publicacoes/"]
        return lista

    def validation(self, response):
        if (
            "col-md-4 col-sm-12 btn-group-vertical mb-4 nav-pub align-top d-table"
            in response.text
        ):
            return True
        return False
