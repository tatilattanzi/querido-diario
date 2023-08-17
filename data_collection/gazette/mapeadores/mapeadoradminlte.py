from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorAdminLTE(Mapeador):
    name = "mapeadoradminlte"

    custom_settings = {"CONCURRENT_REQUESTS": 35}

    def column(self):
        return "ADMINLTE_URL"

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
        if "PRE-LOADER" in response.text:  # TODO: pode n ser um bom criterio
            return True
        return False
