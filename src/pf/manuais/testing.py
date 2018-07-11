# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import pf.manuais


class PfManuaisLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=pf.manuais)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'pf.manuais:default')


PF_MANUAIS_FIXTURE = PfManuaisLayer()


PF_MANUAIS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PF_MANUAIS_FIXTURE,),
    name='PfManuaisLayer:IntegrationTesting'
)


PF_MANUAIS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PF_MANUAIS_FIXTURE,),
    name='PfManuaisLayer:FunctionalTesting'
)


PF_MANUAIS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PF_MANUAIS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PfManuaisLayer:AcceptanceTesting'
)
