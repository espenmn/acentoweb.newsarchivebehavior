from plone.dexterity.interfaces import IDexterityContent
from plone.indexer.decorator import indexer
from acentoweb.newsarchivebehavior.behaviors.news_archive_behavior import INewsArchiveBehavior
#import datetime

@indexer(IDexterityContent)
def yearmonthIndexer(self):
    yearmonth = self.effective().strftime("%b %Y")
    return yearmonth
