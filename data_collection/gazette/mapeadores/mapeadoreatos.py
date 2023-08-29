from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorEatos(Mapeador):
    name = "mapeadoreatos"

    def column(self):
        return "EATOS"

    def backup_column(self):
        return "VALID_EATOS"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://publicacoesmunicipais.com.br:8443/api/acts/campinadalagoa/1
        # https://publicacoesmunicipais.com.br:8443/api/acts/guamiranga/1
        # https://publicacoesmunicipais.com.br:8443/api/acts/ilhacomprida/1

        return [
            f"{protocol}://publicacoesmunicipais.com.br:8443/api/acts/{city}/1",
            f"{protocol}://publicacoesmunicipais.com.br:8443/api/acts/{city}/10",
            f"{protocol}://publicacoesmunicipais.com.br:8443/api/acts/{city}/100",
            f"{protocol}://publicacoesmunicipais.com.br:8443/api/acts/{city}/1000",
        ]

    def validation(self, response):
        return True
