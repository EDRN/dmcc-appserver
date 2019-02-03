# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: content base classes
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.interfaces import ISource
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base, schemata
from zope.interface import implements

SourceSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((
    atapi.StringField(
        'uriPrefix',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'URI Prefix'),
            description=_(u'Uniform Resource Identifier to prepend to locations.'),
        ),
    ),
    atapi.StringField(
        'typeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Type URI'),
            description=_(u"Uniform Resource Identifier of the source's type."),
        ),
    ),
))

SourceSchema['title'].storage = atapi.AnnotationStorage()
SourceSchema['description'].storage = atapi.AnnotationStorage()
schemata.finalizeATCTSchema(SourceSchema, folderish=True, moveDiscussion=True)

class Source(base.ATCTContent):
    '''Abstract source of RDF data.'''
    implements(ISource)
    _at_rename_after_creation = True
    schema                    = SourceSchema
    title                     = atapi.ATFieldProperty('title')
    description               = atapi.ATFieldProperty('description')
    uriPrefix                 = atapi.ATFieldProperty('uriPrefix')
    typeURI                   = atapi.ATFieldProperty('typeURI')
    
