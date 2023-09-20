import re

import scrapy
from dateutil.rrule import DAILY, rrule

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class BaseMunicipioOnlineSpider(BaseGazetteSpider):
    allowed_domains = ["municipioonline.com.br"]

    def start_requests(self):
        url = f"https://www.municipioonline.com.br/{self.url_uf}/prefeitura/{self.url_city}/cidadao/diariooficial"
        yield scrapy.Request(url)

    def parse(self, response):
        for dt in rrule(freq=DAILY, dtstart=self.start_date, until=self.end_date):
            formdata = {
                "__EVENTTARGET": "ctl00$body$txtDataEdicao",
                "ctl00$body$txtDataEdicao": dt.strftime("%d/%m/%Y"),
            }

            yield scrapy.FormRequest.from_response(
                response,
                formdata=formdata,
                callback=self.parse_page,
                cb_kwargs={"page_date": dt.date()},
            )

    def parse_page(self, response, page_date):
        editions_list = response.xpath("//*[@id='body_ddlEdicao']/option").getall()

        if "inexistente" not in editions_list[0]:
            for raw_edition in editions_list:
                edition_number = re.search(r">(\w*)/", raw_edition).group(1)
                url_path = re.search(r'"(.*).pdf"', raw_edition).group(1)
                gazette_url = response.urljoin(
                    f"diariooficial/diario?n=diario.pdf&l={url_path}"
                )

                yield Gazette(
                    date=page_date,
                    edition_number=edition_number,
                    file_urls=[gazette_url],
                    is_extra_edition=False,
                    power="executive",
                )
