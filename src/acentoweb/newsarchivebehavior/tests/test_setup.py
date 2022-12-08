# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from acentoweb.newsarchivebehavior.testing import ACENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that acentoweb.newsarchivebehavior is properly installed."""

    layer = ACENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if acentoweb.newsarchivebehavior is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'acentoweb.newsarchivebehavior'))

    def test_browserlayer(self):
        """Test that IAcentowebNewsarchivebehaviorLayer is registered."""
        from acentoweb.newsarchivebehavior.interfaces import (
            IAcentowebNewsarchivebehaviorLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IAcentowebNewsarchivebehaviorLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ACENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['acentoweb.newsarchivebehavior'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if acentoweb.newsarchivebehavior is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'acentoweb.newsarchivebehavior'))

    def test_browserlayer_removed(self):
        """Test that IAcentowebNewsarchivebehaviorLayer is removed."""
        from acentoweb.newsarchivebehavior.interfaces import \
            IAcentowebNewsarchivebehaviorLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IAcentowebNewsarchivebehaviorLayer,
            utils.registered_layers())
