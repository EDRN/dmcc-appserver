# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Disease
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import IDisease
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

DiseaseSchema = base.SourceSchema.copy() + atapi.Schema((
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
    atapi.StringField(
        'icd9URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'ICD9 URI'),
            description=_(u'Uniform Resource Identifier for the ICD9 predicate.'),
        ),
    ),
    atapi.StringField(
        'icd10URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'ICD10 URI'),
            description=_(u'Uniform Resource Identifier for the ICD10 predicate.'),
        ),
    ),
    atapi.StringField(
        'bodySysURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Body System URI'),
            description=_(u'Uniform Resource Identifier for Body System predicates.'),
        ),
    ),
))

finalizeATCTSchema(DiseaseSchema, folderish=False, moveDiscussion=True)

class Disease(base.Source):
    '''Disease.'''
    implements(IDisease)
    portal_type               = 'Disease'
    _at_rename_after_creation = True
    schema                    = DiseaseSchema
    titleURI                  = atapi.ATFieldProperty('titleURI')
    descURI                   = atapi.ATFieldProperty('descURI')
    icd9URI                   = atapi.ATFieldProperty('icd9URI')
    icd10URI                  = atapi.ATFieldProperty('icd10URI')
    bodySysURI                = atapi.ATFieldProperty('bodySysURI')
    

atapi.registerType(Disease, PROJECTNAME)
