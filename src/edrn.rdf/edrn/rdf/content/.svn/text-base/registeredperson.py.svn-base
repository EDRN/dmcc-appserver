# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Registered Person
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import IRegisteredPerson
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

RegisteredPersonSchema = base.SourceSchema.copy() + atapi.Schema((
    atapi.StringField(
        'firstNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'First Name URI'),
            description=_(u'Uniform Resource Identifier for the first name predicate.'),
        ),
    ),
    atapi.StringField(
        'middleNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Middle Name URI'),
            description=_(u'Uniform Resource Identifier for the middle name predicate.'),
        ),
    ),
    atapi.StringField(
        'lastNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Last Name URI'),
            description=_(u'Uniform Resource Identifier for the last name predicate.'),
        ),
    ),
    atapi.StringField(
        'phoneURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Phone URI'),
            description=_(u'Uniform Resource Identifier for the phone predicate.'),
        ),
    ),
    atapi.StringField(
        'emailURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Email URI'),
            description=_(u'Uniform Resource Identifier for the email predicate.'),
        ),
    ),
    atapi.StringField(
        'faxURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Fax URI'),
            description=_(u'Uniform Resource Identifier for the fax predicate.'),
        ),
    ),
    atapi.StringField(
        'specialtyURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Specialty URI'),
            description=_(u'Uniform Resource Identifier for the specialty predicate.'),
        ),
    ),
    atapi.StringField(
        'photoURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Photo URI'),
            description=_(u'Uniform Resource Identifier for the photograph predicate.'),
        ),
    ),
    atapi.StringField(
        'edrnTitleURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'EDRN Title URI'),
            description=_(u'Uniform Resource Identifier for the EDRN title predicate.'),
        ),
    ),
    atapi.StringField(
        'siteURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Site URI'),
            description=_(u'Uniform Resource Identifier for the site predicate.'),
        ),
    ),
    atapi.StringField(
        'userIDURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'User ID URI'),
            description=_(u'Uniform Resource Identifier for the account name predicate.'),
        ),
    ),
    atapi.StringField(
        'addr1URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Line 1 URI'),
            description=_(u'Uniform Resource Identifier for line 1 of the mailing address.'),
        ),
    ),
    atapi.StringField(
        'addr2URI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Line 2 URI'),
            description=_(u'Uniform Resource Identifier for line 2 of the mailing address.'),
        ),
    ),
    atapi.StringField(
        'cityURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address City URI'),
            description=_(u'Uniform Resource Identifier for the city of the mailing address predicate.'),
        ),
    ),
    atapi.StringField(
        'stateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address State URI'),
            description=_(u'Uniform Resource Identifier for the state of the mailing address predicate.'),
        ),
    ),
    atapi.StringField(
        'zipURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Post Code URI'),
            description=_(u'Uniform Resource Identifier for the post code (zip code) of the mailing address predicate.'),
        ),
    ),
    atapi.StringField(
        'countryURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Mailing Address Country URI'),
            description=_(u'Uniform Resource Identifier for the country of the mailing address predicate.'),
        ),
    ),
))

finalizeATCTSchema(RegisteredPersonSchema, folderish=False, moveDiscussion=True)

class RegisteredPerson(base.Source):
    '''Registered Person generator.'''
    implements(IRegisteredPerson)
    portal_type               = 'Registered Person'
    _at_rename_after_creation = True
    schema                    = RegisteredPersonSchema
    firstNameURI              = atapi.ATFieldProperty('firstNameURI')
    middleNameURI             = atapi.ATFieldProperty('middleNameURI')
    lastNameURI               = atapi.ATFieldProperty('lastNameURI')
    phoneURI                  = atapi.ATFieldProperty('phoneURI')
    emailURI                  = atapi.ATFieldProperty('emailURI')
    faxURI                    = atapi.ATFieldProperty('faxURI')
    specialtyURI              = atapi.ATFieldProperty('specialtyURI')
    photoURI                  = atapi.ATFieldProperty('photoURI')
    edrnTitleURI              = atapi.ATFieldProperty('edrnTitleURI')
    siteURI                   = atapi.ATFieldProperty('siteURI')
    userIDURI                 = atapi.ATFieldProperty('userIDURI')
    addr1URI                  = atapi.ATFieldProperty('addr1URI')
    addr2URI                  = atapi.ATFieldProperty('addr2URI')
    cityURI                   = atapi.ATFieldProperty('cityURI')
    stateURI                  = atapi.ATFieldProperty('stateURI')
    zipURI                    = atapi.ATFieldProperty('zipURI')
    countryURI                = atapi.ATFieldProperty('countryURI')

atapi.registerType(RegisteredPerson, PROJECTNAME)
