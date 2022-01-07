import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'

    start_urls = ['https://www.amazon.com/s?k=laptop&crid=3N1X0COH4ZS6&sprefix=laptop%2Caps%2C592&ref=nb_sb_noss_1']

    def parse(self, response):
        items = AmazonItem()

        product_desc = response.css("#anonCarousel1 .a-color-base.a-text-normal , .a-size-medium.a-text-normal").css('::text').extract()
        product_price = response.css(".a-price-whole::text").extract()
        image_link = response.css(".s-image-fixed-height .s-image").css('::attr(src)').extract()

        items['decr'] = product_desc
        items['price'] = product_price
        items['image'] = image_link

        yield items
