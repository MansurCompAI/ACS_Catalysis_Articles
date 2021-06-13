# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# from issue_selection import issues

class AcsCatalysisPipeline:
    
    # def __init__(self):
    #     self.issue_sel()
        
    def process_item(self, item, spider):
        # print('pipeline')
        return item
