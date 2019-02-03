# encoding: utf-8
# Copyright 2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from edrn.rdf.interfaces import IRDFDatabase
from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting, PLONE_FIXTURE
from plone.testing import z2
from zope.interface import implements
from zope.component import provideUtility
import pkg_resources, SnakeSQL, tempfile, shutil

class TestDatabase(object):
    implements(IRDFDatabase)
    def __init__(self):
        self.dbdir = tempfile.mkdtemp()
        shutil.rmtree(self.dbdir)
        shutil.copytree(pkg_resources.resource_filename(__name__, 'tests/testdata'), self.dbdir)
    def close(self):
        shutil.rmtree(self.dbdir)
    def connect(self):
        return SnakeSQL.connect(database=self.dbdir, autoCreate=False)


class EDRN_RDF_Layer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import edrn.rdf
        self.loadZCML(package=edrn.rdf)
        z2.installProduct(app, 'edrn.rdf')
        self.testDatabase = TestDatabase()
        provideUtility(self.testDatabase)
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'edrn.rdf:default')
    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'edrn.rdf')
        self.testDatabase.close()
        del self.testDatabase

    
EDRN_RDF = EDRN_RDF_Layer()
EDRN_RDF_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDRN_RDF,),
    name='EDRN_RDF_Layer:Integration'
)
EDRN_RDF_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDRN_RDF,),
    name='EDRN_RDF_Layer:Functional'
)
