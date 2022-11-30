# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import accentoweb.newsarchivebehavior


class AccentowebNewsarchivebehaviorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=accentoweb.newsarchivebehavior)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'accentoweb.newsarchivebehavior:default')


ACCENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE = AccentowebNewsarchivebehaviorLayer()


ACCENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ACCENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE,),
    name='AccentowebNewsarchivebehaviorLayer:IntegrationTesting',
)


ACCENTOWEB_NEWSARCHIVEBEHAVIOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ACCENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE,),
    name='AccentowebNewsarchivebehaviorLayer:FunctionalTesting',
)


ACCENTOWEB_NEWSARCHIVEBEHAVIOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ACCENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='AccentowebNewsarchivebehaviorLayer:AcceptanceTesting',
)
