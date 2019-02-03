# encoding: utf-8
# Copyright 2010 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.


'''EDRN RDF Service: Committee generation.
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import ICommittee
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

CommitteeSchema = base.SourceSchema.copy() + atapi.Schema((
    atapi.StringField(
        'titlePredicateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Title Predicate URI'),
            description=_(u'Uniform Resource Identifier for the title predicate.'),
        ),
    ),
    atapi.StringField(
        'abbreviatedNamePredicateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Abbreviated Name Predicate URI'),
            description=_(u'Uniform Resource Identifier for the abbreviated name predicate.'),
        ),
    ),
    atapi.StringField(
        'committeeTypePredicateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Committee Type Predicate URI'),
            description=_(u'Uniform Resource Identifier for the committee type predicate.'),
        ),
    ),
    atapi.StringField(
        'chairPredicateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Chair Predicate URI'),
            description=_(u'Uniform Resource Identifier for the chair predicate.'),
        ),
    ),
    atapi.StringField(
        'coChairPredicateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Co-Chair Predicate URI'),
            description=_(u'Uniform Resource Identifier for the co-chair predicate.'),
        ),
    ),
    atapi.StringField(
        'consultantPredicateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Consultant Predicate URI'),
            description=_(u'Uniform Resource Identifier for the consultant predicate.'),
        ),
    ),
    atapi.StringField(
        'memberPredicateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Member Predicate URI'),
            description=_(u'Uniform Resource Identifier for the member predicate.'),
        ),
    ),
))

finalizeATCTSchema(CommitteeSchema, folderish=False, moveDiscussion=True)

class Committee(base.Source):
    '''Committee generator.'''
    implements(ICommittee)
    schema                      = CommitteeSchema
    titlePredicateURI           = atapi.ATFieldProperty('titlePredicateURI')
    abbreviatedNamePredicateURI = atapi.ATFieldProperty('abbreviatedNamePredicateURI')
    committeeTypePredicateURI   = atapi.ATFieldProperty('committeeTypePredicateURI')
    chairPredicateURI           = atapi.ATFieldProperty('chairPredicateURI')
    coChairPredicateURI         = atapi.ATFieldProperty('coChairPredicateURI')
    consultantPredicateURI      = atapi.ATFieldProperty('consultantPredicateURI')
    memberPredicateURI          = atapi.ATFieldProperty('memberPredicateURI')

atapi.registerType(Committee, PROJECTNAME)
