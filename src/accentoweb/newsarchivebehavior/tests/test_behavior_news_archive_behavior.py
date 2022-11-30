# -*- coding: utf-8 -*-
from accentoweb.newsarchivebehavior.behaviors.news_archive_behavior import INewsArchiveBehaviorMarker
from accentoweb.newsarchivebehavior.testing import ACCENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class NewsArchiveBehaviorIntegrationTest(unittest.TestCase):

    layer = ACCENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_news_archive_behavior(self):
        behavior = getUtility(IBehavior, 'accentoweb.newsarchivebehavior.news_archive_behavior')
        self.assertEqual(
            behavior.marker,
            INewsArchiveBehaviorMarker,
        )
