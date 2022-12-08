# -*- coding: utf-8 -*-

from acentoweb.newsarchivebehavior import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
import datetime


#from zope.interface import alsoProvides


class INewsArchiveBehaviorMarker(Interface):
    pass

@provider(IFormFieldProvider)
class INewsArchiveBehavior(model.Schema):
    """
    """

    monthyear = schema.TextLine(
        title=_(u'Publishing month'),
        required=False,
        readonly=True,
    )


@implementer(INewsArchiveBehavior)
@adapter(INewsArchiveBehaviorMarker)
class NewsArchiveBehavior(object):
    def __init__(self, context):
        self.context = context

    @property
    def monthyear(self):
        #return datetime.datetime.today().strftime("%b %Y")
        if hasattr(self.context, 'monthyear'):
            if  self.context.monthyear != None:
                return self.context.monthyear
        self.context.monthyear = datetime(self.context.created).strftime("%b %Y")
        return self.context.monthyear

    #@monthyear.setter
    #def monthyear(self):
    #    #self.context.monthyear = value
    #    import pdb; pdb.set_trace();
    #    self.context.monthyear = datetime.datetime.today().strftime("%b %Y")

#alsoProvides(INewsArchiveBehavior, IFormFieldProvider)

#    @property
#    def monthyear(self):
#        return datetime.today().strftime("%m %Y")
