
import scrapy
from ..issue_selection import sel_issue

# obtaining year and url for special issues
url = sel_issue(int(input('Issue number (e.g >>> 5) >>> ')))

class acs_cat(scrapy.Spider):
    name = 'acs_sp'
    start_urls = [url]
    # parsing the data
    def parse(self, response):
        for articles in response.css('div.issue-item_metadata'):
            yield {'Title':articles.css('a::text').get(),
                   'Link':'https://pubs.acs.org'+str(articles.css('a').attrib['href']),
                   'Author_list': [i for i in articles.css('span.hlFld-ContribAuthor::text').getall()]
                   }
            