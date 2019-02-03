# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: RDF Folder
'''

from edrn.rdf.config import PROJECTNAME
from edrn.rdf.interfaces import IRDFFolder
from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

RDFFolderSchema = folder.ATFolderSchema.copy() + atapi.Schema((
    # No other attributes
))
RDFFolderSchema['title'].storage = atapi.AnnotationStorage()
RDFFolderSchema['description'].storage = atapi.AnnotationStorage()
finalizeATCTSchema(RDFFolderSchema, folderish=True, moveDiscussion=True)

class RDFFolder(folder.ATFolder):
    '''RDF Folder.'''
    implements(IRDFFolder)
    portal_type               = 'RDF Folder'
    _at_rename_after_creation = True
    schema                    = RDFFolderSchema
    title                     = atapi.ATFieldProperty('title')
    description               = atapi.ATFieldProperty('description')
    

atapi.registerType(RDFFolder, PROJECTNAME)
