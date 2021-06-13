import scrapy
from ..issue_selection import issues

# obtaining year and url for special issues
# year, url = issues()
url = 'https://pubs.acs.org/toc/accacs/11/1'
# scraping

class acs_cat(scrapy.Spider):
    name = 'acs_sp'
    start_url = url
    
    def parse(self, response):
        for articles in response.cssresponse.css('div.issue-item_metadata'):
            yield {'Title':articles.css('a::text').get()}
            
            



















