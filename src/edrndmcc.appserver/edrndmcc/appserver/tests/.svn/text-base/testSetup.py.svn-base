# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
Tests for the setup of the site policy.
'''

import unittest
from edrndmcc.appserver.tests.base import PolicyTestCase
from Products.CMFCore.utils import getToolByName

class TestSetup(PolicyTestCase):
    '''Unit tests the setup of the site policy.'''
    
    def testPortalTitle(self):
        '''Test if the site's title is set correctly.'''
        self.assertEquals('EDRN DMCC Application Server', self.portal.getProperty('title'))
        
    def testPortalDescription(self):
        '''Test if the site's description is set correctly.'''
        self.assertEquals('Application server for the Data Management and Coordinating Center (DMCC) of the Early Detection Research Network (EDRN).', self.portal.getProperty('description'))
    
    def testNASAResponsibleParties(self):
        '''Test if the NASA-mandated responsible party names are set correctly.'''
        self.assertEquals('Sean Kelly', self.portal.getProperty('executive_editor'))
        self.assertEquals('Dan Crichton', self.portal.getProperty('nasa_official'))
    
    def testIfEDRNRDFServiceAvailable(self):
        types = getToolByName(self.portal, 'portal_types')
        self.failUnless('Body System' in types.objectIds())
    
    def testIfThemeInstalled(self):
      skins = getToolByName(self.portal, 'portal_skins')
      self.assertEquals('EDRN Theme', skins.getDefaultSkin())
    
    

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
    
