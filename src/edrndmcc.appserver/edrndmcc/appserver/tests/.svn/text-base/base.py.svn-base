# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
Testing base code.
'''

from Products.Five import zcml
from Products.Five import fiveconfigure
from Testing import ZopeTestCase as ztc
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

# Traditional Products we have to load manually for test cases:
# (none at this time)

@onsetup
def setupedrndmccPolicy():
    '''Set up additional products required for the site policy.'''
    fiveconfigure.debug_mode = True
    import edrndmcc.appserver
    zcml.load_config('configure.zcml', edrndmcc.appserver)
    fiveconfigure.debug_mode = False
    ztc.installPackage('edrndmcc.appserver')
    ztc.installPackage('edrn.theme')
    ztc.installPackage('edrn.rdf')


setupedrndmccPolicy()
ptc.setupPloneSite(products=['edrndmcc.appserver'])

class PolicyTestCase(ptc.PloneTestCase):
    '''Base for tests in this package.'''
    pass
    

class PolicyFunctionalTestCase(ptc.FunctionalTestCase):
    '''Base class for functional (doc-)tests.'''
    pass
    

