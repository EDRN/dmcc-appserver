# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Body System
'''

from edrn.rdf.config import PROJECTNAME
from edrn.rdf.interfaces import IBodySystem
from Products.Archetypes import atapi
from edrn.rdf.content import base
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements
from edrn.rdf import EDRNRDFMessageFactory as _

BodySystemSchema = base.SourceSchema.copy() + atapi.Schema((
    atapi.StringField(
        'titleURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Title URI'),
            description=_(u'Uniform Resource Identifier for the title predicate.'),
        ),
    ),
    atapi.StringField(
        'descURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Description URI'),
            description=_(u'Uniform Resource Identifier for the description predicate.'),
        ),
    ),
))
finalizeATCTSchema(BodySystemSchema, folderish=False, moveDiscussion=True)

class BodySystem(base.Source):
    '''Body system.'''
    implements(IBodySystem)
    portal_type               = 'Body System'
    _at_rename_after_creation = True
    schema                    = BodySystemSchema
    titleURI                  = atapi.ATFieldProperty('titleURI')
    descURI                   = atapi.ATFieldProperty('descURI')
    

atapi.registerType(BodySystem, PROJECTNAME)
