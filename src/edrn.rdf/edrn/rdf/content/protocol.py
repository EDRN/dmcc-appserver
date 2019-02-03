# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: Protocol
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from edrn.rdf.config import PROJECTNAME
from edrn.rdf.content import base
from edrn.rdf.interfaces import IProtocol
from Products.Archetypes import atapi
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from zope.interface import implements

ProtocolSchema = base.SourceSchema.copy() + atapi.Schema((
    atapi.StringField(
        'siteSpecURIPrefix',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Site-Specific URI Prefix'),
            description=_(u'Uniform Resource Identifier for the predicate that identifies site-specific protocol information.'),
        ),
    ),
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
        'abstractURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Abstract URI'),
            description=_(u'Uniform Resource Identifier for the abstract predicate.'),
        ),
    ),
    atapi.StringField(
        'involvedInvestigatorSiteURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Involved Investigator Site URI'),
            description=_(u'Uniform Resource Identifier for the involved investigator site predicate.'),
        ),
    ),
    atapi.StringField(
        'bmNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'BM Name URI'),
            description=_(u'Uniform Resource Identifier for the BM name predicate.'),
        ),
    ),
    atapi.StringField(
        'coordinateInvestigatorSiteURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Coordinating Investigator Site URI'),
            description=_(u'Uniform Resource Identifier for the coordinating site predicate.'),
        ),
    ),
    atapi.StringField(
        'leadInvestigatorSiteURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Lead Investigator Site URI'),
            description=_(u'Uniform Resource Identifier for the lead investigator site predicate.'),
        ),
    ),
    atapi.StringField(
        'collaborativeGroupTextURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Collaborative Group Text URI'),
            description=_(u'Uniform Resource Identifier for the collaborative group text predicate.'),
        ),
    ),
    atapi.StringField(
        'phasedStatusURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Phased Status URI'),
            description=_(u'Uniform Resource Identifier for the phased status predicate.'),
        ),
    ),
    atapi.StringField(
        'aimsURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Aims URI'),
            description=_(u'Uniform Resource Identifier for the aims predicate.'),
        ),
    ),
    atapi.StringField(
        'analyticMethodURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Analytic Method URI'),
            description=_(u'Uniform Resource Identifier for the analytic method predicate.'),
        ),
    ),
    atapi.StringField(
        'blindingURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Blinding URI'),
            description=_(u'Uniform Resource Identifier for the blinding predicate.'),
        ),
    ),
    atapi.StringField(
        'cancerTypeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Cancer Type URI'),
            description=_(u'Uniform Resource Identifier for the cancer type predicate.'),
        ),
    ),
    atapi.StringField(
        'commentsURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Comments URI'),
            description=_(u'Uniform Resource Identifier for the comments predicate.'),
        ),
    ),
    atapi.StringField(
        'dataSharingPlanURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Data Sharing Plan URI'),
            description=_(u'Uniform Resource Identifier for the data sharing plan predicate.'),
        ),
    ),
    atapi.StringField(
        'inSituDataSharingPlanURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'In-Situ Data Sharing Plan URI'),
            description=_(u'Uniform Resource Identifier for the in-situ data sharing plan predicate.'),
        ),
    ),
    atapi.StringField(
        'finishDateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Finish Date URI'),
            description=_(u'Uniform Resource Identifier for the finish date predicate.'),
        ),
    ),
    atapi.StringField(
        'estimatedFinishDateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Estimated Finish Date URI'),
            description=_(u'Uniform Resource Identifier for the estimated finish date predicate.'),
        ),
    ),
    atapi.StringField(
        'startDateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Start Date URI'),
            description=_(u'Uniform Resource Identifier for the start date predicate.'),
        ),
    ),
    atapi.StringField(
        'designURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Design URI'),
            description=_(u'Uniform Resource Identifier for the design predicate.'),
        ),
    ),
    atapi.StringField(
        'fieldOfResearchURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Field of Research URI'),
            description=_(u'Uniform Resource Identifier for the field of research predicate.'),
        ),
    ),
    atapi.StringField(
        'abbreviatedNameURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Abbreviated Name URI'),
            description=_(u'Uniform Resource Identifier for the abbreviated name predicate.'),
        ),
    ),
    atapi.StringField(
        'objectiveURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Objective URI'),
            description=_(u'Uniform Resource Identifier for the objective predicate.'),
        ),
    ),
    atapi.StringField(
        'projectFlagURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Project Flag URI'),
            description=_(u'Uniform Resource Identifier for the project flag predicate.'),
        ),
    ),
    atapi.StringField(
        'protocolTypeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Protocol Type URI'),
            description=_(u'Uniform Resource Identifier for the protocol type predicate.'),
        ),
    ),
    atapi.StringField(
        'publicationsURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Publications URI'),
            description=_(u'Uniform Resource Identifier for the publications predicate.'),
        ),
    ),
    atapi.StringField(
        'outcomeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Outcome URI'),
            description=_(u'Uniform Resource Identifier for the outcome predicate.'),
        ),
    ),
    atapi.StringField(
        'secureOutcomeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Secure Outcome URI'),
            description=_(u'Uniform Resource Identifier for the secure outcome predicate.'),
        ),
    ),
    atapi.StringField(
        'finalSampleSizeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Final Sample Size URI'),
            description=_(u'Uniform Resource Identifier for the final sample size predicate.'),
        ),
    ),
    atapi.StringField(
        'plannedSampleSizeURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Planend Sample Size URI'),
            description=_(u'Uniform Resource Identifier for the planned sample size predicate.'),
        ),
    ),
    atapi.StringField(
        'isAPilotForURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Is A Pilot URI'),
            description=_(u'Uniform Resource Identifier for the "is a pilot" predicate.'),
        ),
    ),
    atapi.StringField(
        'obtainsDataFromURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Obtains Data From URI'),
            description=_(u'Uniform Resource Identifier for the "obtains data from" predicate.'),
        ),
    ),
    atapi.StringField(
        'providesDataToURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Provides Data To URI'),
            description=_(u'Uniform Resource Identifier for the "provides data to" predicate.'),
        ),
    ),
    atapi.StringField(
        'contributesSpecimensURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Contributes Sepcimens URI'),
            description=_(u'Uniform Resource Identifier for the "contributes specimens" predicate.'),
        ),
    ),
    atapi.StringField(
        'obtainsSpecimensFromURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Obtains Specimens From URI'),
            description=_(u'Uniform Resource Identifier for the "obtains specimens from" predicate.'),
        ),
    ),
    atapi.StringField(
        'hasOtherRelationshipURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Has Other Relationship URI'),
            description=_(u'Uniform Resource Identifier for the "has other relationship" predicate.'),
        ),
    ),
    atapi.StringField(
        'animalSubjectTrainingReceivedURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Animal Subject Training Received URI'),
            description=_(u'Uniform Resource Identifier for the predicate that indicates if animal subject training as been received.'),
        ),
    ),
    atapi.StringField(
        'humanSubjectTrainingReceivedURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Human Subject Training Received URI'),
            description=_(u'Uniform Resource Identifier for the predicate that indicates if human subject training as been received.'),
        ),
    ),
    atapi.StringField(
        'irbApprovalNeededURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'IRB Approval Needed URI'),
            description=_(u'Uniform Resource Identifier for the predicate that indicates if IRB approval is still needed.'),
        ),
    ),
    atapi.StringField(
        'currentIRBApprovalDateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Current IRB Approval Date URI'),
            description=_(u'Uniform Resource Identifier for the predicate that tells the current IRB approval date.'),
        ),
    ),
    atapi.StringField(
        'originalIRBApprovalDateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Original IRB Approval Date URI'),
            description=_(u'Uniform Resource Identifier for the predicate that tells of the original date of IRB approval.'),
        ),
    ),
    atapi.StringField(
        'irbExpirationDateURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'IRB Expiration Date URI'),
            description=_(u'Uniform Resource Identifier for the predicate that tells when the IRB will expire.'),
        ),
    ),
    atapi.StringField(
        'generalIRBNotesURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'General IRB Notes URI'),
            description=_(u'Uniform Resource Identifier for the predicate that lists general notes about the IRB.'),
        ),
    ),
    atapi.StringField(
        'irbNumberURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'IRB Number URI'),
            description=_(u'Uniform Resource Identifier for the predicate that identifies the IRB number.'),
        ),
    ),
    atapi.StringField(
        'siteRoleURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Site Role URI'),
            description=_(u'Uniform Resource Identifier for the predicate that lists the roles the site particiaptes in.'),
        ),
    ),
    atapi.StringField(
        'reportingStageURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Report Stage URI'),
            description=_(u'Uniform Resource Identifier for the predicate that names the stages of reporting.'),
        ),
    ),
    atapi.StringField(
        'eligibilityCriteriaURI',
        required=True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u'Eligibility Criteria URI'),
            description=_(u'Uniform Resource Identifier for the predicate that identifies the eligibility criteria.'),
        ),
    ),
))

finalizeATCTSchema(ProtocolSchema, folderish=False, moveDiscussion=True)

class Protocol(base.Source):
    '''Protocol.'''
    implements(IProtocol)
    portal_type                      = 'Protocol'
    _at_rename_after_creation        = True
    schema                           = ProtocolSchema
    siteSpecURIPrefix                = atapi.ATFieldProperty('siteSpecURIPrefix')
    titleURI                         = atapi.ATFieldProperty('titleURI')
    abstractURI                      = atapi.ATFieldProperty('abstractURI')
    involvedInvestigatorSiteURI      = atapi.ATFieldProperty('involvedInvestigatorSiteURI')
    bmNameURI                        = atapi.ATFieldProperty('bmNameURI')
    coordinateInvestigatorSiteURI    = atapi.ATFieldProperty('coordinateInvestigatorSiteURI')
    leadInvestigatorSiteURI          = atapi.ATFieldProperty('leadInvestigatorSiteURI')
    collaborativeGroupTextURI        = atapi.ATFieldProperty('collaborativeGroupTextURI')
    phasedStatusURI                  = atapi.ATFieldProperty('phasedStatusURI')
    aimsURI                          = atapi.ATFieldProperty('aimsURI')
    analyticMethodURI                = atapi.ATFieldProperty('analyticMethodURI')
    blindingURI                      = atapi.ATFieldProperty('blindingURI')
    cancerTypeURI                    = atapi.ATFieldProperty('cancerTypeURI')
    commentsURI                      = atapi.ATFieldProperty('commentsURI')
    dataSharingPlanURI               = atapi.ATFieldProperty('dataSharingPlanURI')
    inSituDataSharingPlanURI         = atapi.ATFieldProperty('inSituDataSharingPlanURI')
    finishDateURI                    = atapi.ATFieldProperty('finishDateURI')
    estimatedFinishDateURI           = atapi.ATFieldProperty('estimatedFinishDateURI')
    startDateURI                     = atapi.ATFieldProperty('startDateURI')
    designURI                        = atapi.ATFieldProperty('designURI')
    fieldOfResearchURI               = atapi.ATFieldProperty('fieldOfResearchURI')
    abbreviatedNameURI               = atapi.ATFieldProperty('abbreviatedNameURI')
    objectiveURI                     = atapi.ATFieldProperty('objectiveURI')
    projectFlagURI                   = atapi.ATFieldProperty('projectFlagURI')
    protocolTypeURI                  = atapi.ATFieldProperty('protocolTypeURI')
    publicationsURI                  = atapi.ATFieldProperty('publicationsURI')
    outcomeURI                       = atapi.ATFieldProperty('outcomeURI')
    secureOutcomeURI                 = atapi.ATFieldProperty('secureOutcomeURI')
    finalSampleSizeURI               = atapi.ATFieldProperty('finalSampleSizeURI')
    plannedSampleSizeURI             = atapi.ATFieldProperty('plannedSampleSizeURI')
    isAPilotForURI                   = atapi.ATFieldProperty('isAPilotForURI')
    obtainsDataFromURI               = atapi.ATFieldProperty('obtainsDataFromURI')
    providesDataToURI                = atapi.ATFieldProperty('providesDataToURI')
    contributesSpecimensURI          = atapi.ATFieldProperty('contributesSpecimensURI')
    obtainsSpecimensFromURI          = atapi.ATFieldProperty('obtainsSpecimensFromURI')
    hasOtherRelationshipURI          = atapi.ATFieldProperty('hasOtherRelationshipURI')
    animalSubjectTrainingReceivedURI = atapi.ATFieldProperty('animalSubjectTrainingReceivedURI')
    humanSubjectTrainingReceivedURI  = atapi.ATFieldProperty('humanSubjectTrainingReceivedURI')
    irbApprovalNeededURI             = atapi.ATFieldProperty('irbApprovalNeededURI')
    currentIRBApprovalDateURI        = atapi.ATFieldProperty('currentIRBApprovalDateURI')
    originalIRBApprovalDateURI       = atapi.ATFieldProperty('originalIRBApprovalDateURI')
    irbExpirationDateURI             = atapi.ATFieldProperty('irbExpirationDateURI')
    generalIRBNotesURI               = atapi.ATFieldProperty('generalIRBNotesURI')
    irbNumberURI                     = atapi.ATFieldProperty('irbNumberURI')
    siteRoleURI                      = atapi.ATFieldProperty('siteRoleURI')
    reportingStageURI                = atapi.ATFieldProperty('reportingStageURI')
    eligibilityCriteriaURI           = atapi.ATFieldProperty('eligibilityCriteriaURI')

atapi.registerType(Protocol, PROJECTNAME)
