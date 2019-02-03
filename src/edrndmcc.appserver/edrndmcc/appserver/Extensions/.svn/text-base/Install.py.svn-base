# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from Products.CMFCore.utils import getToolByName
import transaction

PRODUCT_DEPENDENCIES = (
    'edrn.theme',
    'edrn.rdf',
)
EXTENSION_PROFILES = ('edrndmcc.appserver:default',)

def install(context, reinstall=False):
    quickInstaller = getToolByName(context, 'portal_quickinstaller')
    setupTool = getToolByName(context, 'portal_setup')
    for product in PRODUCT_DEPENDENCIES:
        if reinstall and quickInstaller.isProductInstalled(product):
            quickInstaller.reinstallProducts(product)
            transaction.savepoint()
        elif not quickInstaller.isProductInstalled(product):
            quickInstaller.installProduct(product)
            transaction.savepoint()
    for extensionID in EXTENSION_PROFILES:
        setupTool.runAllImportStepsFromProfile('profile-%s' % extensionID, purge_old=False)
        productName = extensionID.split(':')[0]
        quickInstaller.notifyInstalled(productName)
        transaction.savepoint()
    

