import scrapy

class SpiderCitacoes(scrapy.Spider):
    name = 'citacoes2'

    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]


    def parse(self, response):
        pagina = response.url.split("/")[-2]
        # nome_arquivo = f"citacoes-{pagina}.html"
        nome_arquivo = 'citacoes-%s.html' % pagina
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)

        self.log('Arquivo salvo %s' % pagina)
