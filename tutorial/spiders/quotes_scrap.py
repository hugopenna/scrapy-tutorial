import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # Passing an string to response.follow.
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        # Using selector direct on response.follow
        # for href in response.css('li.next a::attr(href)'):
            # yield response.follow(href, callback=self.parse)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)
