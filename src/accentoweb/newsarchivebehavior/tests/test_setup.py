# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from accentoweb.newsarchivebehavior.testing import ACCENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that accentoweb.newsarchivebehavior is properly installed."""

    layer = ACCENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if accentoweb.newsarchivebehavior is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'accentoweb.newsarchivebehavior'))

    def test_browserlayer(self):
        """Test that IAccentowebNewsarchivebehaviorLayer is registered."""
        from accentoweb.newsarchivebehavior.interfaces import (
            IAccentowebNewsarchivebehaviorLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IAccentowebNewsarchivebehaviorLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ACCENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['accentoweb.newsarchivebehavior'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if accentoweb.newsarchivebehavior is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'accentoweb.newsarchivebehavior'))

    def test_browserlayer_removed(self):
        """Test that IAccentowebNewsarchivebehaviorLayer is removed."""
        from accentoweb.newsarchivebehavior.interfaces import \
            IAccentowebNewsarchivebehaviorLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IAccentowebNewsarchivebehaviorLayer,
            utils.registered_layers())
