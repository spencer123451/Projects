# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WebItem(scrapy.Item):
    url = scrapy.Field()
    wikipedia_link = scrapy.Field()
    photo_url = scrapy.Field()
    lead_text = scrapy.Field()
    title = scrapy.Field()