# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Publication
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import IPublication
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

PublicationSchema = base.SourceSchema.copy() + atapi.Schema((
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
        'abstractURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Abstract URI'),
            description=_(u'Uniform Resource Identifier for the abstract predicate.'),
        ),
    ),
    atapi.StringField(
        'authorURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Author URI'),
            description=_(u'Uniform Resource Identifier for the author predicate.'),
        ),
    ),
    atapi.StringField(
        'issueURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Issue URI'),
            description=_(u'Uniform Resource Identifier for the issue predicate.'),
        ),
    ),
    atapi.StringField(
        'journalURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Journal URI'),
            description=_(u'Uniform Resource Identifier for the journal predicate.'),
        ),
    ),
    atapi.StringField(
        'pmidURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'PubMed ID URI'),
            description=_(u'Uniform Resource Identifier for the PubMed ID predicate.'),
        ),
    ),
    atapi.StringField(
        'pubURLURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Publication URL URI'),
            description=_(u'Uniform Resource Identifier for the publication URL predicate.'),
        ),
    ),
    atapi.StringField(
        'volumeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Volume URI'),
            description=_(u'Uniform Resource Identifier for the volume predicate.'),
        ),
    ),
    atapi.StringField(
        'yearURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Year URI'),
            description=_(u'Uniform Resource Identifier for the year predicate.'),
        ),
    ),
))

finalizeATCTSchema(PublicationSchema, folderish=False, moveDiscussion=True)

class Publication(base.Source):
    '''Publication.'''
    implements(IPublication)
    portal_type               = 'Publication'
    _at_rename_after_creation = True
    schema                    = PublicationSchema
    titleURI                  = atapi.ATFieldProperty('titleURI')
    descURI                   = atapi.ATFieldProperty('descURI')
    abstractURI               = atapi.ATFieldProperty('abstractURI')
    authorURI                 = atapi.ATFieldProperty('authorURI')
    issueURI                  = atapi.ATFieldProperty('issueURI')
    journalURI                = atapi.ATFieldProperty('journalURI')
    pmidURI                   = atapi.ATFieldProperty('pmidURI')
    pubURLURI                 = atapi.ATFieldProperty('pubURLURI')
    volumeURI                 = atapi.ATFieldProperty('volumeURI')
    yearURI                   = atapi.ATFieldProperty('yearURI')
    

atapi.registerType(Publication, PROJECTNAME)
