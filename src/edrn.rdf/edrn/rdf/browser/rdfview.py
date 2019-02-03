# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.
'''
EDRN RDF Service: body system UI.
'''

from Acquisition import aq_inner
from edrn.rdf.interfaces import IRDFDatabase, IBodySystem, ISite, IPublication, IRegisteredPerson
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from rdflib import ConjunctiveGraph, URIRef, Literal, RDF
from zope.component import getUtility

PIC_PREFIX = 'http://ginger.fhcrc.org/dmcc/staff-photographs/'

# Courtesy Greg Warnick:
_siteRoles = {
    '1':                  'Funding Source',
    '2':                  'Discovery',
    '3':                  'Reference',
    '4':                  'Coordinating Site',
    '5':                  'Specimen Contributing Site',
    '6':                  'Specimen Storage',
    '7':                  'Analysis Lab',
    '8':                  'Statistical Services',
    '9':                  'Consultant',
    '97':                 'Other, Specify',
}

# Courtesy Greg Warnick:
_reportingStages = {
    '1':                   'Development Stage',
    '2':                   'Funding Stage',
    '3':                   'Protocol Development Stage',
    '4':                   'Procedure Development Stage',
    '5':                   'Retrospective Sample Identification Stage',
    '6':                   'Recruitment Stage',
    '7':                   'Lab Processing Stage',
    '8':                   'Blinding Stage',
    '9':                   'Lab Analysis Stage',
    '10':                  'Publication Stage',
    '11':                  'Statistical Analysis Stage',
    '12':                  'Completed',
    '97':                  'Other, specify',
}

# Courtesy Greg Warnick:
_fieldsOfResearch = {
    '1': 'Genomics',
    '2': 'Epigenomics',
    '3': 'Proteomics',
    '4': 'Glycomics',
    '5': 'Nanotechnology',
    '6': 'Metabolomics',
    '7': 'Hypermethylation',
    '9': 'Other, Specify',
}

# These relationships correspond to the distinct values currently appearing in
# the Protocol_relationship_type column of the Protocol_protocol_relationship
# table. Should any new types appear that don't appear in this mapping as a
# key, the "Other, specify" key is used as a default.
_relationships = {
    'contributes specimens to': 'contributesSpecimensURI',
    'is a pilot for':           'isAPilotForURI',
    'obtains data from':        'obtainsDataFromURI',
    'obtains specimens from':   'obtainsSpecimensFromURI',
    'Other, specify':           'hasOtherRelationshipURI',
    'provides data to':         'providesDataToURI',
}

def toLiteral(text):
    '''The database seems to be using cp1252 (aka windows-1252) encoding.'''
    return Literal(unicode(text, 'cp1252'))
    

class BodySystemMissingError(Exception):
    '''Error indicating that no Body System object is available.'''

class SiteMissingError(Exception):
    '''Error indicating that no Site object is available.'''

class PublicationMissingError(Exception):
    '''Error indicating that no Publication object is available.'''

class RegisteredPersonMissingError(Exception):
    '''Error indicating that no RegisteredPerson object is available.'''

class SourceGenerator(BrowserView):
    '''Abstract RDF generator. Template-method design pattern.'''
    def __call__(self):
        connection = None
        try:
            db = getUtility(IRDFDatabase)
            connection = db.connect()
            graph = ConjunctiveGraph()
            self.populate(graph, connection, aq_inner(self.context))
            self.request.response.setHeader('Content-type', 'application/rdf+xml')
            return graph.serialize()
        finally:
            try:
                connection.close()
            except:
                pass
    def populate(self, graph, connection):
        '''Yield an appropriate conjunctive graph.'''
        raise NotImplementedError('Override me')
        

class BodySystemGenerator(SourceGenerator):
    '''Generates RDF for body systems.'''
    def populate(self, graph, connection, context):
        cursor = connection.cursor()
        titleURI, descURI = URIRef(context.titleURI), URIRef(context.descURI)
        cursor.execute('select Identifier, Title, Description from Body_System')
        for identifier, title, desc in cursor.fetchall():
            subjectURI = URIRef(context.uriPrefix + unicode(identifier))
            graph.add((subjectURI, RDF.type, URIRef(context.typeURI)))
            graph.add((subjectURI, titleURI, toLiteral(title)))
            if desc:
                graph.add((subjectURI, descURI, toLiteral(desc)))
    
    
class DiseaseGenerator(SourceGenerator):
    '''Generates RDF for diseases.'''
    def populate(self, graph, connection, context):
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IBodySystem.__identifier__)
        if len(results) == 0:
            raise BodySystemMissingError('No BodySystem object found')
        bodySysPrefix = results[0].getObject().uriPrefix
        cursor = connection.cursor()
        titleURI, descURI, bodySysURI = URIRef(context.titleURI), URIRef(context.descURI), URIRef(context.bodySysURI)
        icd9URI, icd10URI = URIRef(context.icd9URI), URIRef(context.icd10URI)
        cursor.execute('select Identifier, Title, Description, ICD9, ICD10, Body_System from Disease')
        for identifier, title, desc, icd9, icd10, bodySystems in cursor.fetchall():
            if not title:
                continue
            subjectURI = URIRef(context.uriPrefix + unicode(identifier))
            graph.add((subjectURI, RDF.type, URIRef(context.typeURI)))
            graph.add((subjectURI, titleURI, toLiteral(title)))
            if desc:
                graph.add((subjectURI, descURI, toLiteral(desc)))
            if icd9:
                graph.add((subjectURI, icd9URI, toLiteral(icd9)))
            if icd10:
                graph.add((subjectURI, icd10URI, toLiteral(icd10)))
            for bodySys in bodySystems.split(', '):
                graph.add((subjectURI, bodySysURI, URIRef(bodySysPrefix + bodySys)))
    
    
class SiteGenerator(SourceGenerator):
    '''Generates RDF for sites.'''
    def populate(self, graph, connection, context):
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IRegisteredPerson.__identifier__)
        if len(results) == 0:
            raise RegisteredPersonMissingError('No RegisteredPerson object found')
        personPrefix = results[0].getObject().uriPrefix
        cursor = connection.cursor()
        cursor.execute('select Identifier, Title, Associate_Members_Sponsor, ' \
            + 'EDRN_Funding_Date_Start, EDRN_Funding_Date_Finish, FWA_Number, ' \
            + 'ID_for_Principal_Investigator, IDs_for_CoPrincipalInvestigators, ' \
            + 'IDs_for_CoInvestigators, IDs_for_Investigators, IDs_for_Staff, ' \
            + 'Institution_Name_Abbrev, Site_Program_Description, Institution_URL, Member_Type, ' \
            + 'Member_Type_Historical_Notes from Site')
        for i, title, assocMemberSponsor, fundingDateStart, fundingDateFinish, fwaNumber, \
            pi, coPI, coi, investigators, staff, \
            abbrevName, program, url, memberType, histNotes in cursor.fetchall():
            if not title:
                continue
            subjectURI = URIRef(context.uriPrefix + unicode(i))
            graph.add((subjectURI, RDF.type, URIRef(context.typeURI)))
            graph.add((subjectURI, URIRef(context.titleURI), toLiteral(title)))
            if pi:
                graph.add((subjectURI, URIRef(context.piURI), URIRef(personPrefix + str(pi))))
            if coPI:
                for coPIID in coPI.split(', '):
                    graph.add((subjectURI, URIRef(context.coPIURI), URIRef(personPrefix + str(coPIID))))
            if coi:
                for coID in coi.split(', '):
                    graph.add((subjectURI, URIRef(context.coIURI), URIRef(personPrefix + coID)))
            if investigators:
                for investigatorID in investigators.split(', '):
                    graph.add((subjectURI, URIRef(context.investigatorURI), URIRef(personPrefix + investigatorID)))
            if staff:
                for staffID in staff.split(', '):
                    graph.add((subjectURI, URIRef(context.staffURI), URIRef(personPrefix + staffID)))
            if assocMemberSponsor:
                graph.add((subjectURI, URIRef(context.assocMemberSponsorURI),
                    URIRef(context.uriPrefix + unicode(assocMemberSponsor))))
            if fundingDateStart:
                graph.add((subjectURI, URIRef(context.fundingDateStartURI), Literal(fundingDateStart)))
            if fundingDateFinish:
                graph.add((subjectURI, URIRef(context.fundingDateFinishURI), Literal(fundingDateFinish)))
            if fwaNumber:
                graph.add((subjectURI, URIRef(context.fwaNumberURI), toLiteral(fwaNumber)))
            if abbrevName:
                graph.add((subjectURI, URIRef(context.abbrevNameURI), toLiteral(abbrevName)))
            if program:
                graph.add((subjectURI, URIRef(context.programURI), toLiteral(program)))
            if url:
                graph.add((subjectURI, URIRef(context.urlURI), toLiteral(url)))
            if memberType:
                graph.add((subjectURI, URIRef(context.memberTypeURI), toLiteral(memberType)))
            if histNotes:
                graph.add((subjectURI, URIRef(context.histNotesURI), toLiteral(histNotes)))
                

class PublicationGenerator(SourceGenerator):
    '''Generates RDF for publications.'''
    def populate(self, graph, connection, context):
        cursor = connection.cursor()
        cursor.execute('select Identifier, Abstract, Author, Description, Issue, Journal, PMID, Publication_URL, Title, Volume,' \
            + 'Year from Publication')
        for identifier, abstract, author, description, issue, journal, pmID, pubURL, title, volume, year in cursor.fetchall():
            subjectURI = URIRef(context.uriPrefix + unicode(identifier))
            graph.add((subjectURI, RDF.type, URIRef(context.typeURI)))
            graph.add((subjectURI, URIRef(context.titleURI), toLiteral(title)))
            if author:
                authorURI = URIRef(context.authorURI)
                for authorName in author.split(', '):
                    graph.add((subjectURI, authorURI, toLiteral(authorName)))
            if abstract:
                graph.add((subjectURI, URIRef(context.abstractURI), toLiteral(abstract)))
            if description:
                graph.add((subjectURI, URIRef(context.descURI), toLiteral(description)))
            if issue:
                graph.add((subjectURI, URIRef(context.issueURI), toLiteral(issue)))
            if journal:
                graph.add((subjectURI, URIRef(context.journalURI), toLiteral(journal)))
            if pmID:
                graph.add((subjectURI, URIRef(context.pmidURI), toLiteral(pmID)))
            if pubURL:
                graph.add((subjectURI, URIRef(context.pubURLURI), toLiteral(pubURL)))
            if volume:
                graph.add((subjectURI, URIRef(context.volumeURI), toLiteral(volume)))
            if year:
                graph.add((subjectURI, URIRef(context.yearURI), Literal(year)))


_slots = {
    'BiomarkerName':                        ('bmNameURI', toLiteral),
    'Eligibility_criteria':                 ('eligibilityCriteriaURI', toLiteral),
    'Protocol_5_Phase_Status':              ('phasedStatusURI', Literal),
    'Protocol_Aims':                        ('aimsURI', toLiteral),
    'Protocol_Analytic_Method':             ('analyticMethodURI', toLiteral),
    'Protocol_Blinding':                    ('blindingURI', toLiteral),
    'Protocol_Cancer_Type':                 ('cancerTypeURI', toLiteral),
    'Protocol_Collaborative_Group':         ('collaborativeGroupTextURI', toLiteral),
    'Protocol_Comments':                    ('commentsURI', toLiteral),
    'Protocol_Data_Sharing_Plan':           ('dataSharingPlanURI', toLiteral),
    'Protocol_Data_Sharing_Plan_In_Place':  ('inSituDataSharingPlanURI', toLiteral),
    'Protocol_Date_Finish':                 ('finishDateURI', Literal),
    'Protocol_Date_Finish_Estimate':        ('estimatedFinishDateURI', Literal),
    'Protocol_Date_Start':                  ('startDateURI', Literal),
    'Protocol_Design':                      ('designURI', toLiteral),
    'Protocol_Name_Abbrev':                 ('abbreviatedNameURI', toLiteral),
    'Protocol_Objective':                   ('objectiveURI', toLiteral),
    'Protocol_or_Project_Flag':             ('projectFlagURI', toLiteral),
    'Protocol_Results_Outcome':             ('outcomeURI', toLiteral),
    'Protocol_Results_Outcome_Secure_Site': ('secureOutcomeURI', toLiteral),
    'Protocol_Type':                        ('protocolTypeURI', toLiteral),
    'Sample_Size_Final':                    ('finalSampleSizeURI', toLiteral),
    'Sample_Size_Planned':                  ('plannedSampleSizeURI', toLiteral),
}

class ProtocolGenerator(SourceGenerator):
    '''Generates RDF for protocols.'''
    def populate(self, graph, connection, context):
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=ISite.__identifier__)
        if len(results) == 0:
            raise SiteMissingError('No Site object found')
        sitePrefix = results[0].getObject().uriPrefix
        results = catalog(object_provides=IPublication.__identifier__)
        if len(results) == 0:
            raise PublicationMissingError('No Publication object found')
        publicationPrefix = results[0].getObject().uriPrefix
        cursor = connection.cursor()
        cursor.execute('select ' \
            + 'Protocol_or_study.Identifier, ' \
            + 'Protocol_or_study.Slot, ' \
            + 'Protocol_or_study.Value, ' \
            + 'EDRN_Protocol.Slot, ' \
            + 'EDRN_Protocol.Value ' \
            + 'from Protocol_or_study, EDRN_Protocol ' \
            + 'where Protocol_or_study.Identifier = EDRN_Protocol.Identifier')
        for identifier, studySlot, studyValue, protoSlot, protoValue in cursor.fetchall():
            subjectURI = URIRef(context.uriPrefix + unicode(identifier))
            graph.add((subjectURI, RDF.type, URIRef(context.typeURI)))
            if studySlot == 'Protocol_Abstract' and studyValue:
                graph.add((subjectURI, URIRef(context.abstractURI), toLiteral(studyValue)))
            elif studySlot == 'Title' and studyValue:
                graph.add((subjectURI, URIRef(context.titleURI), toLiteral(studyValue)))
            if not protoValue:
                continue
            if protoSlot == 'Involved_Investigator_Site_ID':
                for siteID in protoValue.split(', '):
                    graph.add((subjectURI, URIRef(context.involvedInvestigatorSiteURI), URIRef(sitePrefix + unicode(siteID))))
                    siteID = int(siteID)
                    siteSpecCursor = connection.cursor()
                    siteSpecCursor.execute('select ' \
                        + 'Animal_Subject_Training_Received, ' \
                        + 'Human_Subject_Training_Recieved, ' \
                        + 'IRB_Approval_Needed, ' \
                        + 'IRB_Date_Current_Approval_Date, ' \
                        + 'IRB_Date_Original_Approval_Date, ' \
                        + 'IRB_Expiration_Date, ' \
                        + 'IRB_General_Notes, ' \
                        + 'IRB_Number, ' \
                        + 'Protocol_Site_Roles, ' \
                        + 'Reporting_Stages ' \
                        + 'from Protocol_site_specifics where Protocol_ID = %d and Site_ID = %d' % (identifier, siteID))
                    if siteSpecCursor.rowcount != 1:
                        continue
                    animalSubjectTrainingReceived, humanSubjectTrainingReceived, irbApprovalNeeded, currentIRBApprovalDate, \
                    originalIRBApprovalDate, irbExpirationDate, generalIRBNotes, irbNumber, siteRoles, reportingStages \
                        = siteSpecCursor.fetchone()
                    siteSpecSubject = URIRef(context.siteSpecURIPrefix + unicode(identifier) + u'-' + unicode(siteID))
                    if animalSubjectTrainingReceived:
                        graph.add((siteSpecSubject, URIRef(context.animalSubjectTrainingReceivedURI),
                            toLiteral(animalSubjectTrainingReceived)))
                    if humanSubjectTrainingReceived:
                        graph.add((siteSpecSubject, URIRef(context.humanSubjectTrainingReceivedURI),
                            toLiteral(humanSubjectTrainingReceived)))
                    if irbApprovalNeeded:
                        graph.add((siteSpecSubject, URIRef(context.irbApprovalNeededURI), toLiteral(irbApprovalNeeded)))
                    if currentIRBApprovalDate:
                        graph.add((siteSpecSubject, URIRef(context.currentIRBApprovalDateURI), Literal(currentIRBApprovalDate)))
                    if originalIRBApprovalDate:
                        graph.add((siteSpecSubject, URIRef(context.originalIRBApprovalDateURI), Literal(originalIRBApprovalDate)))
                    if irbExpirationDate:
                        graph.add((siteSpecSubject, URIRef(context.irbExpirationDateURI), Literal(irbExpirationDate)))
                    if generalIRBNotes:
                        graph.add((siteSpecSubject, URIRef(context.generalIRBNotesURI), toLiteral(generalIRBNotes)))
                    if irbNumber:
                        graph.add((siteSpecSubject, URIRef(context.irbNumberURI), toLiteral(irbNumber)))
                    if siteRoles:
                        for siteRole in siteRoles.split(', '):
                            graph.add((siteSpecSubject, URIRef(context.siteRoleURI), Literal(_siteRoles.get(siteRole, u'UNKNOWN'))))
                    if reportingStages:
                        for rs in reportingStages.split(', '):
                            graph.add((siteSpecSubject, URIRef(context.reportingStageURI),
                                Literal(_reportingStages.get(rs, u'UNKNOWN'))))
            elif protoSlot == 'Protocol_Publications':
                for protoID in protoValue.split(', '):
                    graph.add((subjectURI, URIRef(context.publicationsURI), URIRef(publicationPrefix + protoID)))
            elif protoSlot == 'Coordinating_Investigator_Site_ID':
                graph.add((subjectURI, URIRef(context.coordinateInvestigatorSiteURI), URIRef(sitePrefix + unicode(protoValue))))
            elif protoSlot == 'Lead_Investigator_Site_ID':
                graph.add((subjectURI, URIRef(context.leadInvestigatorSiteURI), URIRef(sitePrefix + unicode(protoValue))))
            elif protoSlot == 'Protocol_Field_of_Research':
                for fieldID in protoValue.split(', '):
                    graph.add((subjectURI, URIRef(context.fieldOfResearchURI), Literal(_fieldsOfResearch.get(fieldID, u'UNKNOWN'))))
            else:
                uriFieldName, converterFunc = _slots[protoSlot]
                predicateURIAccessor = context.getField(uriFieldName).getAccessor(context)
                predicateURI = URIRef(predicateURIAccessor())
                graph.add((subjectURI, predicateURI, converterFunc(protoValue)))
            relationCursor = connection.cursor()
            relationCursor.execute('select Protocol_2_Identifier, Protocol_relationship_type from Protocol_protocol_relationship' \
                + ' where Protocol_1_Identifier = %d' % identifier)
            for protoID, relType in relationCursor.fetchall():
                fieldName = _relationships.get(relType.strip(), 'hasOtherRelationshipURI')
                fieldValue = getattr(context, fieldName, None)
                if not fieldValue:
                    continue
                graph.add((subjectURI, URIRef(fieldValue), URIRef(context.uriPrefix + unicode(protoID))))
        

class RegisteredPersonGenerator(SourceGenerator):
    '''Generates RDF for registered people.'''
    def populate(self, graph, connection, context):
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=ISite.__identifier__)
        if len(results) == 0:
            raise SiteMissingError('No Site object found')
        sitePrefix = results[0].getObject().uriPrefix
        cursor = connection.cursor()
        firstNameURI, middleNameURI, lastNameURI = \
            URIRef(context.firstNameURI), URIRef(context.middleNameURI), URIRef(context.lastNameURI)
        phoneURI, emailURI, siteURI = URIRef(context.phoneURI), URIRef(context.emailURI), URIRef(context.siteURI)
        faxURI, specialtyURI = URIRef(context.faxURI), URIRef(context.specialtyURI)
        photoURI, edrnTitleURI, userIDURI = URIRef(context.photoURI), URIRef(context.edrnTitleURI), URIRef(context.userIDURI)
        addr1URI, addr2URI, cityURI, stateURI = \
            URIRef(context.addr1URI), URIRef(context.addr2URI), URIRef(context.cityURI), URIRef(context.stateURI)
        zipURI, countryURI = URIRef(context.zipURI), URIRef(context.countryURI)
        cursor.execute('select Identifier, Name_First, Name_Middle, Name_Last, Secure_site_siteid, Phone, Email, Fax, Specialty,' \
            + 'Photo_file_name, EDRN_Title, userID, Mailing_Address1, Mailing_Address2, Mailing_City, Mailing_State,' \
            + 'Mailing_Zip, Mailing_Country from Registered_Person')
        for identifier, first, middle, last, siteID, phone, email, fax, specialty, photo, edrnTitle, userID, addr1, addr2, \
            city, state, zipCode, country in cursor.fetchall():
            subjectURI = URIRef(context.uriPrefix + unicode(identifier))
            graph.add((subjectURI, RDF.type, URIRef(context.typeURI)))
            if first and first.strip():
                graph.add((subjectURI, firstNameURI, toLiteral(first)))
            if middle and middle.strip():
                graph.add((subjectURI, middleNameURI, toLiteral(middle)))
            if last and last.strip():
                graph.add((subjectURI, lastNameURI, toLiteral(last)))
            if phone:
                graph.add((subjectURI, phoneURI, toLiteral(phone)))
            if email:
                graph.add((subjectURI, emailURI, toLiteral('mailto:' + email)))
            if siteID:
                graph.add((subjectURI, siteURI, URIRef(sitePrefix + unicode(siteID))))
            if fax:
                graph.add((subjectURI, faxURI, toLiteral(fax)))
            if specialty:
                graph.add((subjectURI, specialtyURI, toLiteral(specialty)))
            if photo:
                graph.add((subjectURI, photoURI, URIRef(PIC_PREFIX + unicode(photo))))
            if edrnTitle:
                graph.add((subjectURI, edrnTitleURI, toLiteral(edrnTitle)))
            if userID:
                graph.add((subjectURI, userIDURI, toLiteral(userID)))
            if addr1:
                graph.add((subjectURI, addr1URI, toLiteral(addr1)))
            if addr2:
                graph.add((subjectURI, addr2URI, toLiteral(addr2)))
            if city:
                graph.add((subjectURI, cityURI, toLiteral(city)))
            if state:
                graph.add((subjectURI, stateURI, toLiteral(state)))
            if zipCode:
                graph.add((subjectURI, zipURI, toLiteral(zipCode)))
            if country:
                graph.add((subjectURI, countryURI, toLiteral(country)))


class CommitteeGenerator(SourceGenerator):
    '''Generates RDF for committees'''
    def populate(self, graph, connection, context):
        catalog = getToolByName(context, 'portal_catalog')
        results = catalog(object_provides=IRegisteredPerson.__identifier__)
        if len(results) == 0:
            raise RegisteredPersonMissingError('No Registered Person object found')
        personPrefix                = results[0].getObject().uriPrefix
        cursor                      = connection.cursor()
        titlePredicateURI           = URIRef(context.titlePredicateURI)
        abbreviatedNamePredicateURI = URIRef(context.abbreviatedNamePredicateURI)
        committeeTypePredicateURI   = URIRef(context.committeeTypePredicateURI)
        chairPredicateURI           = URIRef(context.chairPredicateURI)
        coChairPredicateURI         = URIRef(context.coChairPredicateURI)
        consultantPredicateURI      = URIRef(context.consultantPredicateURI)
        memberPredicateURI          = URIRef(context.memberPredicateURI)
        cursor.execute('select Committees.Identifier, Committees.Committee_name, Committees.Committee_name_short, Committees.Committee_type, Committee_Membership.Registered_Person_Identifer, Committee_Membership.RoleName from Committees, Committee_Membership where Committees.Identifier = Committee_Membership.Committee_Identifier')
        lastIdentifier = None
        for identifier, title, abbrev, committeeType, personID, role in cursor.fetchall():
            if lastIdentifier != identifier:
                subjectURI = URIRef(context.uriPrefix + unicode(identifier))
                graph.add((subjectURI, RDF.type, URIRef(context.typeURI)))
                if title: graph.add((subjectURI, titlePredicateURI, toLiteral(title.strip())))
                if abbrev: graph.add((subjectURI, abbreviatedNamePredicateURI, toLiteral(abbrev.strip())))
                if committeeType: graph.add((subjectURI, committeeTypePredicateURI, toLiteral(committeeType.strip())))
                lastIdentifier = identifier
            if role:
                role = role.strip().lower()
                person = URIRef(personPrefix + unicode(personID))
                if role == 'chair':
                    predicate = chairPredicateURI
                elif role == 'co-chair':
                    predicate = coChairPredicateURI
                elif role == 'consultant':
                    predicate = consultantPredicateURI
                else:
                    predicate = memberPredicateURI
                graph.add((subjectURI, predicate, person))

                