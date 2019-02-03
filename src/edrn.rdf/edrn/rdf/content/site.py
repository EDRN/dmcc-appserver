# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Site
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import ISite
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

SiteSchema = base.SourceSchema.copy() + atapi.Schema((
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
        'abbrevNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Abbreviated Name URI'),
            description=_(u'Uniform Resource Identifier for the abbreviated name predicate.'),
        ),
    ),
    atapi.StringField(
        'assocMemberSponsorURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Associate Members Sponsor URI'),
            description=_(u'Uniform Resource Identifier fo the predicate that identifies the sponsor for a site.'),
        ),
    ),
    atapi.StringField(
        'fundingDateStartURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Funding Start Date URI'),
            description=_(u'Uniform Resource Identifier for the predicate that identifies the date funding started for the site.'),
        ),
    ),
    atapi.StringField(
        'fundingDateFinishURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Funding Finish Date URI'),
            description=_(u'Uniform Resource Identifier for the predicate that identifies the date funding ended for the site.'),
        ),
    ),
    atapi.StringField(
        'fwaNumberURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'FWA Number URI'),
            description=_(u'Uniform Resource Identifier for the FWA number predicate.'),
        ),
    ),
    atapi.StringField(
        'piURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'PI URI'),
            description=_(u'Uniform Resource Identifier for the Primary Investigator predicate.'),
        ),
    ),
    atapi.StringField(
        'coPIURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Co-PI URI'),
            description=_(u'Uniform Resource Identifier for the Co-PI predicate.'),
        ),
    ),
    atapi.StringField(
        'coIURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Co-I URI'),
            description=_(u'Uniform Resource Identifier for the Co-Investigator predicate.'),
        ),
    ),
    atapi.StringField(
        'investigatorURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Investigator URI'),
            description=_(u'Uniform Resource Identifier for the Investigator predicate.'),
        ),
    ),
    atapi.StringField(
        'staffURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Staff URI'),
            description=_(u'Uniform Resource Identifier for the staff predicate.'),
        ),
    ),
    atapi.StringField(
        'programURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Program URI'),
            description=_(u'Uniform Resource Identifier for predicate identifying the site program description.'),
        ),
    ),
    atapi.StringField(
        'urlURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'URL URI'),
            description=_(u'Uniform Resource Identifier for the predicate identifying the site home page.'),
        ),
    ),
    atapi.StringField(
        'memberTypeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Member Type URI'),
            description=_(u'Uniform Resource Identifier for the predicate identifying the type of the EDRN member site.'),
        ),
    ),
    atapi.StringField(
        'histNotesURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Hisorical Notes URI'),
            description=_(u'Uniform Resource Identifier for the predicate identifying historical notes.'),
        ),
    ),
))

finalizeATCTSchema(SiteSchema, folderish=False, moveDiscussion=True)

class Site(base.Source):
    '''Site.'''
    implements(ISite)
    portal_type               = 'Site'
    _at_rename_after_creation = True
    schema                    = SiteSchema
    titleURI                  = atapi.ATFieldProperty('titleURI')
    abbrevNameURI             = atapi.ATFieldProperty('abbrevNameURI')
    assocMemberSponsorURI     = atapi.ATFieldProperty('assocMemberSponsorURI')
    fundingDateStartURI       = atapi.ATFieldProperty('fundingDateStartURI')
    fundingDateFinishURI      = atapi.ATFieldProperty('fundingDateFinishURI')
    fwaNumberURI              = atapi.ATFieldProperty('fwaNumberURI')
    piURI                     = atapi.ATFieldProperty('piURI')
    coPIURI                   = atapi.ATFieldProperty('coPIURI')
    coIURI                    = atapi.ATFieldProperty('coIURI')
    investigatorURI           = atapi.ATFieldProperty('investigatorURI')
    staffURI                  = atapi.ATFieldProperty('staffURI')
    programURI                = atapi.ATFieldProperty('programURI')
    urlURI                    = atapi.ATFieldProperty('urlURI')
    memberTypeURI             = atapi.ATFieldProperty('memberTypeURI')
    histNotesURI              = atapi.ATFieldProperty('histNotesURI')

atapi.registerType(Site, PROJECTNAME)
