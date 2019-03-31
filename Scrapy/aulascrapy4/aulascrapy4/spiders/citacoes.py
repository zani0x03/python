import scrapy

class QuotesSpider(scrapy.Spider):
    name = "citacoes"
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'texto': quote.css('span.text::text').extract_first(),
                'autor': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        pagina = response.url.split("/")[-2]
        nome_arquivo = 'citacoes-%s.html' % pagina
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)

        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)