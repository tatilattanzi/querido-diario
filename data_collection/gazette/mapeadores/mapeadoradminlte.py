from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorAdminLTE(Mapeador):
    name = "mapeadoradminlte"

    def column(self):
        return "ADMINLTE"

    def backup_column(self):
        return "VALID_ADMINLTE"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # http://diariooficial.gurupi.to.gov.br/
        # https://diariooficial.pmsaraguaia.pa.gov.br/

        lista = [
            f"{protocol}://diariooficial.{city}.{state_code}.gov.br/",
            f"{protocol}://diariooficial.pm{city}.{state_code}.gov.br/",
        ]
        return lista

    def validation(self, response):
        if "PRE-LOADER" in response.text:
            if "col-sm-5" in response.text:
                if "col-sm-7" in response.text:
                    if (
                        'data-original-title="Baixar a Última Edição Normal">Acessar</a>'
                        in response.text
                    ):
                        return True
        return False
