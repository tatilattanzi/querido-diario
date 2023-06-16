from datetime import date
import datetime

import dateparser
from scrapy import Request

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

# Aqui o site oficial dos diários oficiais do município de Altamira-PA https://altamira.pa.gov.br/c/diario-oficial/
# Estrutura os diários da seguinte maneira: na página inicial, todos os arquivos disponíveis entre maio de 2021 e junho de 2023.
# A cada mês, os diários estão agrupados por dia, cada dia pode ter um ou mais arquivos (EXTRA).
# Ao clicar em no link de uma publicação, o usuário é redirecionado para uma página que contém o link de fato para o arquivo .pdf.

class PaAltamiraSpider(BaseGazetteSpider):

    TERRITORY_ID = "1500602"
    name = "pa_altamira"
    allowed_domains = ["altamira.pa.gov.br"]
    start_urls = ["https://altamira.pa.gov.br/diario-oficial/"]
    start_date = date(2015, 5, 13)
    FILE_ELEMENT_XPATH = "//a[contains(@title, 'Diário Oficial')]"
    PDF_ELEMENT_XPATH = "//a[contains(@href, '.pdf')]"
    DATE_FORMAT = "%d/%m/%Y"

    # Método secundário, responsável por buscar os links dos .pdf dos diários dentro da página da publicação específica
    def parse_pdf(self, response, gazette_date):
        # convert gazette_date to proper Gazette.date format
        gazette_date = datetime.datetime.strptime(gazette_date, self.DATE_FORMAT).date()
        print(f"→→→ formated date: {gazette_date}")
        for record in response.xpath(self.PDF_ELEMENT_XPATH):
            pdf_href_link = record.xpath('./@href').get()
            # Se o link contiver a palavra 'EXTRA', significa que é uma publicação extra, portanto, o atributo is_extra_edition é setado como True
            if pdf_href_link.find('EXTRA') != -1:
                yield Gazette(
                    date=gazette_date,
                    file_urls=[pdf_href_link],
                    is_extra_edition=True,
                    territory_id=self.TERRITORY_ID,
                    power="executive",
                )
            yield Gazette(
                date=gazette_date,
                file_urls=[pdf_href_link],
                is_extra_edition=False,
                territory_id=self.TERRITORY_ID,
                power="executive",
            )

    # Método inicial, responsável por buscar os links individuais para cada página de publicação, a partir da página inicial (start_url)
    def parse(self, response):
        # Procura na página principal de Diários Oficiais, os links para as páginas de cada publlicação individual, que contém de fato os links para os arquivos .pdf
        for record in response.xpath(self.FILE_ELEMENT_XPATH):
            # Selectiona todos os elementos do tipo hiperlink que contenham o texto 'Diário Oficial'
            href_link = record.xpath('./@href').get()
            # extract data from href_link
            # example link: https://altamira.pa.gov.br/diario-oficial-no-713-2023-12-01-2023/
            # Extract date from link considering the expected result is 12-01-2023
            if 'extra' in href_link:
                terms = href_link.split('-')
                date_passed = terms[-4] + '/' + terms[-3] + '/' + terms[-2]
            else:
                terms = href_link.split('-')
                # O último termo é o ano com um / no final, por isso o [:-1]
                date_passed = terms[-3] + '/' + terms[-2] + '/' + terms[-1][:-1]
            # Aqui a data da publicação já é fornecida ao método parse_pdf utilizando cb_kwargs e a variável gazette_date
            yield Request(href_link, callback=self.parse_pdf, cb_kwargs=dict(gazette_date=date_passed), dont_filter=True)

