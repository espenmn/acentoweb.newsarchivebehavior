# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import acentoweb.newsarchivebehavior


class AcentowebNewsarchivebehaviorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=acentoweb.newsarchivebehavior)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'acentoweb.newsarchivebehavior:default')


ACENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE = AcentowebNewsarchivebehaviorLayer()


ACENTOWEB_NEWSARCHIVEBEHAVIOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ACENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE,),
    name='AcentowebNewsarchivebehaviorLayer:IntegrationTesting',
)


ACENTOWEB_NEWSARCHIVEBEHAVIOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ACENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE,),
    name='AcentowebNewsarchivebehaviorLayer:FunctionalTesting',
)


ACENTOWEB_NEWSARCHIVEBEHAVIOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ACENTOWEB_NEWSARCHIVEBEHAVIOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='AcentowebNewsarchivebehaviorLayer:AcceptanceTesting',
)
