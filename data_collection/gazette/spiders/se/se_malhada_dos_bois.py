from datetime import date

from gazette.spiders.base.municipioonline import BaseMunicipioOnlineSpider


class SeMalhadaDosBoisSpider(BaseMunicipioOnlineSpider):
    TERRITORY_ID = "2803807"
    name = "se_malhada_dos_bois"
    start_date = date(2020, 1, 13)
    url_uf = "se"
    url_city = "malhadadosbois"
