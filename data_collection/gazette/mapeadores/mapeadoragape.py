from gazette.mapeadores.base.mapeador import Mapeador


class MapeadorAgape(Mapeador):
    name = "mapeadoragape"

    custom_settings = {
        "CONCURRENT_REQUESTS": 50,
    }

    def column(self):
        return "AGAPE_URL"

    def backup_column(self):
        return "VALID_AGAPE"

    def urls_pattern(self, protocol, city, state_code):
        # casos conhecidos
        # https://agportal.agapesistemas.com.br/DiarioOficial/?alias=pmRIACHUELO
        # https://agportal.agapesistemas.com.br/DiarioOficial/?alias=pmcumbe

        return [
            f"{protocol}://agportal.agapesistemas.com.br/DiarioOficial/?alias=pm{city}"
        ]

    def validation(self, response):
        if "agapesistemas.com.br" in response.text:
            return True
        return False
