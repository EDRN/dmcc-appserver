# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: interfaces
'''

from edrn.rdf import EDRNRDFMessageFactory as _
from zope import schema
from zope.app.container.constraints import contains
from zope.interface import Interface

class IRDFDatabase(Interface):
    def connect():
        '''Yield an appropriate database connection.'''
        
    
class IRDFFolder(Interface):
    '''A folder containing RDF data sources.'''
    contains('edrn.rdf.source')
    title = schema.TextLine(title=_(u'Title'), description=_(u'The name of this folder.'))
    description = schema.Text(title=_(u'Description'), description=_(u'A short summary of this folder.'))
    

class ISource(Interface):
    '''An abstract source of RDF.'''
    title = schema.TextLine(title=_(u'Title'), description=_(u'The name of this RDF source.'))
    description = schema.Text(title=_(u'Description'), description=_(u'A short summary of this RDF source.'))
    uriPrefix = schema.TextLine(title=_(u'URI Prefix'), description=_(u'Uniform Resource Identifier to prepend to locations.'))
    typeURI = schema.TextLine(title=_(u'Type URI'), description=_(u"Uniform Resource Identifier of the source's type." ))


class IBodySystem(ISource):
    '''Body systems.'''
    titleURI = schema.TextLine(title=_(u'Title URI'), description=_(u'Uniform Resource Identifier for the title predicate.'))
    descURI = schema.TextLine(title=_(u'Description URI'),
        description=_(u'Uniform Resource Identifier for the description predicate.'))


class IDisease(ISource):
    '''Disease.'''
    titleURI = schema.TextLine(title=_(u'Title URI'), description=_(u'Uniform Resource Identifier for the title predicate.'))
    descURI = schema.TextLine(title=_(u'Description URI'),
        description=_(u'Uniform Resource Identifier for the description predicate.'))
    icd9URI = schema.TextLine(title=_(u'ICD9 URI'), description=_(u'Uniform Resource Identifier for the ICD9 predicate.'))
    icd10URI = schema.TextLine(title=_(u'ICD10 URI'), description=_(u'Uniform Resource Identifier for the ICD10 predicate.'))
    bodySysURI = schema.TextLine(title=_(u'Body System URI'),
        description=_(u'Uniform Resource Identifier for Body System predicates.'))

class ISite(ISource):
    '''Site.'''
    titleURI = schema.TextLine(title=_(u'Title URI'), description=_(u'Uniform Resource Identifier for the title predicate.'))
    abbrevNameURI = schema.TextLine(title=_(u'Abbreviated Name URI'),
        description=_(u'Uniform Resource Identifier for the abbreviated name predicate.'))   
    assocMemberSponsorURI = schema.TextLine(title=_(u'Associate Members Sponsor URI'),
        description=_(u'Uniform Resource Identifier fo the predicate that identifies the sponsor for a site.'))
    fundingDateStartURI = schema.TextLine(title=_(u'Funding Start Date URI'),
        description=_(u'Uniform Resource Identifier for the predicate that identifies the date funding started for the site.'))
    fundingDateFinishURI = schema.TextLine(title=_(u'Funding Finish Date URI'), 
        description=_(u'Uniform Resource Identifier for the predicate that identifies the date funding ended for the site.'))
    fwaNumberURI = schema.TextLine(title=_(u'FWA Number URI'),
        description=_(u'Uniform Resource Identifier for the FWA number predicate.'))
    piURI = schema.TextLine(title=_(u'PI URI'),
        description=_(u'Uniform Resource Identifier for the Primary Investigator predicate.'))
    coPIURI = schema.TextLine(title=_(u'Co-PI URI'),
        description=_(u'Uniform Resource Investigator for the Co-Primary Investigator predicate.'))
    coIURI = schema.TextLine(title=_(u'Co-I URI'),
        description=_(u'Uniform Resource Identifier for the Co-Investigator predicate.'))
    investigatorURI = schema.TextLine(title=_(u'Investigator URI'),
        description=_(u'Uniform Resource Identifier for the Investigator predicate.'))
    staffURI = schema.TextLine(title=_(u'Staff URI'),
        description=_(u'Uniform Resource Identifier for the staff predicate.'))
    programURI = schema.TextLine(title=_(u'Program URI'),
		description=_(u'Uniform Resource Identifier for predicate identifying the program description.'))
    urlURI = schema.TextLine(title=_(u'URL URI'),
		description=_(u'Uniform Resource Identifier for the predicate identifying the site home page.'))
    memberTypeURI = schema.TextLine(title=_(u'Member Type URI'),
		description=_(u'Uniform Resource Identifier for the predicate identifying the type of the EDRN member site.'))
    histNotesURI = schema.TextLine(title=_(u'Historical Notes URI'),
        description=_(u'Uniform Resource Identifier for the historical notes predicate.'))


class IPublication(ISource):
    '''Publication.'''
    titleURI = schema.TextLine(title=_(u'Title URI'), description=_(u'Uniform Resource Identifier for the title predicate.'))
    descURI = schema.TextLine(title=_(u'Description URI'),
        description=_(u'Uniform Resource Identifier for the description predicate.'))
    abstractURI = schema.TextLine(title=_(u'Abstract URI'), description=_(u'Uniform Resource Identifier for the abstract predicate.'))
    authorURI = schema.TextLine(title=_(u'Author URI'), description=_(u'Uniform Resource Identifier for the author predicate.'))
    issueURI = schema.TextLine(title=_(u'Issue URI'), description=_(u'Uniform Resource Identifier for the issue predicate.'))
    journalURI = schema.TextLine(title=_(u'Journal URI'), description=_(u'Uniform Resource Identifier for the journal predicate.'))
    pmidURI = schema.TextLine(title=_(u'PubMed ID URI'), description=_(u'Uniform Resource Identifier for the PubMed ID predicate.'))
    pubURLURI = schema.TextLine(title=_(u'Publication URL URI'),
        description=_(u'Uniform Resource Identifier for the publication URL predicate.'))
    volumeURI = schema.TextLine(title=_(u'Volume URI'), description=_(u'Uniform Resource Identifier for the volume predicate.'))
    yearURI = schema.TextLine(title=_(u'Year URI'), description=_(u'Uniform Resource Identifier for the year predicate.'))
    

class IProtocol(ISource):
    '''Protocol.'''
    siteSpecURIPrefix = schema.TextLine(
        title=_(u'Site-Specific URI Prefix'),
        description=_(u'Uniform Resource Identifier for the predicate that identifies site-specific protocol information.'),
        required=True,
    )
    titleURI = schema.TextLine(
        title=_(u'Title URI'),
        description=_(u'Uniform Resource Identifier for the title predicate.'),
        required=True,
    )
    abstractURI = schema.TextLine(
        title=_(u'Abstract URI'),
        description=_(u'Uniform Resource Identifier for the abstract predicate.'),
        required=True,
    )
    involvedInvestigatorSiteURI = schema.TextLine(
        title=_(u'Involved Investigator Site URI'),
        description=_(u'Uniform Resource Identifier for the involved investigator site predicate.'),
        required=True,
    )
    bmNameURI = schema.TextLine(
        title=_(u'BM Name URI'),
        description=_(u'Uniform Resource Identifier for the BM name predicate.'),
        required=True,
    )
    coordinateInvestigatorSiteURI = schema.TextLine(
        title=_(u'Coordinating Investigator Site URI'),
        description=_(u'Uniform Resource Identifier for the coordinating site predicate.'),
        required=True,
    )
    leadInvestigatorSiteURI = schema.TextLine(
        title=_(u'Lead Investigator Site URI'),
        description=_(u'Uniform Resource Identifier for the lead investigator site predicate.'),
        required=True,
    )
    collaborativeGroupTextURI = schema.TextLine(
        title=_(u'Collaborative Group Text URI'),
        description=_(u'Uniform Resource Identifier for the collaborative group text predicate.'),
        required=True,
    )
    phasedStatusURI = schema.TextLine(
        title=_(u'Phased Status URI'),
        description=_(u'Uniform Resource Identifier for the phased status predicate.'),
        required=True,
    )
    aimsURI = schema.TextLine(
        title=_(u'Aims URI'),
        description=_(u'Uniform Resource Identifier for the aims predicate.'),
        required=True,
    )
    analyticMethodURI = schema.TextLine(
        title=_(u'Analytic Method URI'),
        description=_(u'Uniform Resource Identifier for the analytic method predicate.'),
        required=True,
    )
    blindingURI = schema.TextLine(
        title=_(u'Blinding URI'),
        description=_(u'Uniform Resource Identifier for the blinding predicate.'),
        required=True,
    )
    cancerTypeURI = schema.TextLine(
        title=_(u'Cancer Type URI'),
        description=_(u'Uniform Resource Identifier for the cancer type predicate.'),
        required=True,
    )
    commentsURI = schema.TextLine(
        title=_(u'Comments URI'),
        description=_(u'Uniform Resource Identifier for the comments predicate.'),
        required=True,
    )
    dataSharingPlanURI = schema.TextLine(
        title=_(u'Data Sharing Plan URI'),
        description=_(u'Uniform Resource Identifier for the data sharing plan predicate.'),
        required=True,
    )
    inSituDataSharingPlanURI = schema.TextLine(
        title=_(u'In-Situ Data Sharing Plan URI'),
        description=_(u'Uniform Resource Identifier for the in-situ data sharing plan predicate.'),
        required=True,
    )
    finishDateURI = schema.TextLine(
        title=_(u'Finish Date URI'),
        description=_(u'Uniform Resource Identifier for the finish date predicate.'),
        required=True,
    )
    estimatedFinishDateURI = schema.TextLine(
        title=_(u'Estimated Finish Date URI'),
        description=_(u'Uniform Resource Identifier for the estimated finish date predicate.'),
        required=True,
    )
    startDateURI = schema.TextLine(
        title=_(u'Start Date URI'),
        description=_(u'Uniform Resource Identifier for the start date predicate.'),
        required=True,
    )
    designURI = schema.TextLine(
        title=_(u'Design URI'),
        description=_(u'Uniform Resource Identifier for the design predicate.'),
        required=True,
    )
    fieldOfResearchURI = schema.TextLine(
        title=_(u'Field of Research URI'),
        description=_(u'Uniform Resource Identifier for the field of research predicate.'),
        required=True,
    )
    abbreviatedNameURI = schema.TextLine(
        title=_(u'Abbreviated Name URI'),
        description=_(u'Uniform Resource Identifier for the abbreviated name predicate.'),
        required=True,
    )
    objectiveURI = schema.TextLine(
        title=_(u'Objective URI'),
        description=_(u'Uniform Resource Identifier for the objective predicate.'),
        required=True,
    )
    projectFlagURI = schema.TextLine(
        title=_(u'Project Flag URI'),
        description=_(u'Uniform Resource Identifier for the project flag predicate.'),
        required=True,
    )
    protocolTypeURI = schema.TextLine(
        title=_(u'Protocol Type URI'),
        description=_(u'Uniform Resource Identifier for the protocol type predicate.'),
        required=True,
    )
    publicationsURI = schema.TextLine(
        title=_(u'Publications URI'),
        description=_(u'Uniform Resource Identifier for the publications predicate.'),
        required=True,
    )
    outcomeURI = schema.TextLine(
        title=_(u'Outcome URI'),
        description=_(u'Uniform Resource Identifier for the outcome predicate.'),
        required=True,
    )
    secureOutcomeURI = schema.TextLine(
        title=_(u'Secure Outcome URI'),
        description=_(u'Uniform Resource Identifier for the secure outcome predicate.'),
        required=True,
    )
    finalSampleSizeURI = schema.TextLine(
        title=_(u'Final Sample Size URI'),
        description=_(u'Uniform Resource Identifier for the final sample size predicate.'),
        required=True,
    )
    plannedSampleSizeURI = schema.TextLine(
        title=_(u'Planend Sample Size URI'),
        description=_(u'Uniform Resource Identifier for the planned sample size predicate.'),
        required=True,
    )
    isAPilotForURI = schema.TextLine(
        title=_(u'Is A Pilot URI'),
        description=_(u'Uniform Resource Identifier for the "is a pilot" predicate.'),
        required=True,
    )
    obtainsDataFromURI = schema.TextLine(
        title=_(u'Obtains Data From URI'),
        description=_(u'Uniform Resource Identifier for the "obtains data from" predicate.'),
        required=True,
    )
    providesDataToURI = schema.TextLine(
        title=_(u'Provides Data To URI'),
        description=_(u'Uniform Resource Identifier for the "provides data to" predicate.'),
        required=True,
    )
    contributesSpecimensURI = schema.TextLine(
        title=_(u'Contributes Sepcimens URI'),
        description=_(u'Uniform Resource Identifier for the "contributes specimens" predicate.'),
        required=True,
    )
    obtainsSpecimensFromURI = schema.TextLine(
        title=_(u'Obtains Specimens From URI'),
        description=_(u'Uniform Resource Identifier for the "obtains specimens from" predicate.'),
        required=True,
    )
    hasOtherRelationshipURI = schema.TextLine(
        title=_(u'Has Other Relationship URI'),
        description=_(u'Uniform Resource Identifier for the "has other relationship" predicate.'),
        required=True,
    )
    animalSubjectTrainingReceivedURI = schema.TextLine(
        title=_(u'Animal Subject Training Received URI'),
        description=_(u'Uniform Resource Identifier for the predicate that indicates if animal subject training as been received.'),
        required=True,
    )
    humanSubjectTrainingReceivedURI = schema.TextLine(
        title=_(u'Human Subject Training Received URI'),
        description=_(u'Uniform Resource Identifier for the predicate that indicates if human subject training as been received.'),
        required=True,
    )
    irbApprovalNeededURI = schema.TextLine(
        title=_(u'IRB Approval Needed URI'),
        description=_(u'Uniform Resource Identifier for the predicate that indicates if IRB approval is still needed.'),
        required=True,
    )
    currentIRBApprovalDateURI = schema.TextLine(
        title=_(u'Current IRB Approval Date URI'),
        description=_(u'Uniform Resource Identifier for the predicate that tells the current IRB approval date.'),
        required=True,
    )
    originalIRBApprovalDateURI = schema.TextLine(
        title=_(u'Original IRB Approval Date URI'),
        description=_(u'Uniform Resource Identifier for the predicate that tells of the original date of IRB approval.'),
        required=True,
    )
    irbExpirationDateURI = schema.TextLine(
        title=_(u'IRB Expiration Date URI'),
        description=_(u'Uniform Resource Identifier for the predicate that tells when the IRB will expire.'),
        required=True,
    )
    generalIRBNotesURI = schema.TextLine(
        title=_(u'General IRB Notes URI'),
        description=_(u'Uniform Resource Identifier for the predicate that lists general notes about the IRB.'),
        required=True,
    )
    irbNumberURI = schema.TextLine(
        title=_(u'IRB Number URI'),
        description=_(u'Uniform Resource Identifier for the predicate that identifies the IRB number.'),
        required=True,
    )
    siteRoleURI = schema.TextLine(
        title=_(u'Site Role URI'),
        description=_(u'Uniform Resource Identifier for the predicate that lists the roles the site participates in.'),
        required=True,
    )
    reportingStageURI = schema.TextLine(
        title=_(u'Report Stage URI'),
        description=_(u'Uniform Resource Identifier for the predicate that names the stages of reporting.'),
        required=True,
    )
    eligibilityCriteriaURI = schema.TextLine(
        title=_(u'Eligibility Criteria URI'),
        description=_(u'Uniform Resource Identifier for the predicate that identifies the eligibility criteria.'),
        required=True,
    )
    

class IRegisteredPerson(ISource):
    '''Registered person.'''
    firstNameURI = schema.TextLine(
        title=_(u'First Name URI'),
        description=_(u'Uniform Resource Identifier for the first name predicate.'),
        required=True,
    )
    middleNameURI = schema.TextLine(
        title=_(u'Middle Name URI'),
        description=_(u'Uniform Resource Identifier for the middle name predicate.'),
        required=True,
    )
    lastNameURI = schema.TextLine(
        title=_(u'Last Name URI'),
        description=_(u'Uniform Resource Identifier for the last name predicate.'),
        required=True,
    )
    phoneURI = schema.TextLine(
        title=_(u'Phone URI'),
        description=_(u'Uniform Resource Identifier for the phone predicate.'),
        required=True,
    )
    emailURI = schema.TextLine(
        title=_(u'Email URI'),
        description=_(u'Uniform Resource Identifier for the email predicate.'),
        required=True,
    )
    faxURI = schema.TextLine(
        title=_(u'Fax URI'),
        description=_(u'Uniform Resource Identifier for the fax predicate.'),
        required=True,
    )
    specialtyURI = schema.TextLine(
        title=_(u'Specialty URI'),
        description=_(u'Uniform Resource Identifier for the speciality predicate.'),
        required=True,
    )
    photoURI = schema.TextLine(
        title=_(u'Photo URI'),
        description=_(u'Uniform Resource Identifier for the photograph predicate.'),
        required=True,
    )
    edrnTitleURI = schema.TextLine(
        title=_(u'EDRN Title URI'),
        description=_(u'Uniform Resource Identifier for the EDRN title predicate.'),
        required=True,
    )
    siteURI = schema.TextLine(
        title=_(u'Site URI'),
        description=_(u'Uniform Resource Identifier for the site predicate.'),
        required=False,
    )
    userIDURI = schema.TextLine(
        title=_(u'User ID URI'),
        description=_(u'Uniform Resource Identifier for the account name predicate.'),
        required=False,
    )
    addr1URI = schema.TextLine(title=_(u'Mailing Address Line 1 URI'),
        description=_(u'Uniform Resource Identifier for line 1 of the mailing address.'))
    addr2URI = schema.TextLine(title=_(u'Mailing Address Line 2 URI'),
        description=_(u'Uniform Resource Identifier for line 2 of the mailing address.'))
    cityURI = schema.TextLine(title=_(u'Mailing Address City URI'),
        description=_(u'Uniform Resource Identifier for the city of the mailing address predicate.'))
    stateURI = schema.TextLine(title=_(u'Mailing Address State URI'),
        description=_(u'Uniform Resource Identifier for the state of the mailing address predicate.'))
    zipURI = schema.TextLine(title=_(u'Mailing Address Post Code URI'),
        description=_(u'Uniform Resource Identifier for the post code (zip code) of the mailing address predicate.'))
    countryURI = schema.TextLine(title=_(u'Mailing Address Country URI'),
        description=_(u'Uniform Resource Identifier for the country of the mailing address predicate.'))


class ICommittee(ISource):
    '''Committee information generation'''
    titlePredicateURI = schema.TextLine(
        title=_(u'Title Predicate URI'),
        description=_(u'Uniform Resource Identifier for the title predicate.'),
        required=True,
    )
    abbreviatedNamePredicateURI = schema.TextLine(
        title=_(u'Abbreviated Name Predicate URI'),
        description=_(u'Uniform Resource Identifier for the abbreviated name predicate.'),
        required=True,
    )
    committeeTypePredicateURI = schema.TextLine(
        title=_(u'Committee Type Predicate URI'),
        description=_(u'Uniform Resource Identifier for the committee type predicate.'),
        required=True,
    )
    chairPredicateURI = schema.TextLine(
        title=_(u'Chair Predicate URI'),
        description=_(u'Uniform Resource Identifier for the chair predicate.'),
        required=True,
    )
    coChairPredicateURI = schema.TextLine(
        title=_(u'Co-Chair Predicate URI'),
        description=_(u'Uniform Resource Identifier for the co-chair predicate.'),
        required=True,
    )
    consultantPredicateURI = schema.TextLine(
        title=_(u'Consultant Predicate URI'),
        description=_(u'Uniform Resource Identifier for the consultant predicate.'),
        required=True,
    )
    memberPredicateURI = schema.TextLine(
        title=_(u'Member Predicate URI'),
        description=_(u'Uniform Resource Identifier for the member predicate.'),
        required=True,
    )
