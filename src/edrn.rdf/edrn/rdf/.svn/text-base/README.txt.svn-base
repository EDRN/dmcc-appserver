This package provides an RDF-based web service that describes the knowledge
assets of the Early Detection Research Network (EDRN).


Content Types
=============

The content types introduced in this package include the following:

RDF Folder
    A container to hold RDF service objects.
Body System
    An RDF service object that provides information on body systems.

The remainder of this document demonstrates the content types using a series
of functional tests.


Tests
=====

In order to execute these tests, we'll first need a test browser::

    >>> app = layer['app']
    >>> from plone.testing.z2 import Browser
    >>> from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
    >>> browser = Browser(app)
    >>> browser.handleErrors = False
    >>> browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD))
    >>> portal = layer['portal']    
    >>> portalURL = portal.absolute_url()

Here we go.


Addable Content
---------------

Here we'll exercise some of the content objects available in this project and
demonstrate their properties and constraints.


RDF Folder
~~~~~~~~~~

The RDF Folder is addable anywhere::

    >>> browser.open(portalURL)
    >>> l = browser.getLink(id='rdf-folder')
    >>> l.url.endswith('createObject?type_name=RDF+Folder')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My RDF Folder'
    >>> browser.getControl(name='description').value = u'A place to hold RDF service objects.'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-rdf-folder' in portal.objectIds()
    True
    >>> rdfFolder = portal['my-rdf-folder']
    >>> rdfFolder.title
    'My RDF Folder'
    >>> rdfFolder.description
    'A place to hold RDF service objects.'
    

Body Systems
~~~~~~~~~~~~

A Body System is an RDF service object that describes body systems such as
organs.  They can only be added to RDF Folders::

    >>> browser.open(portalURL)
    >>> browser.getLink(id='body-system')
    Traceback (most recent call last):
    ...
    LinkNotFoundError
    >>> browser.open(portalURL + '/my-rdf-folder')
    >>> l = browser.getLink(id='body-system')
    >>> l.url.endswith('createObject?type_name=Body+System')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My Body System'
    >>> browser.getControl(name='description').value = u'Provides body system descriptions.'
    >>> browser.getControl(name='uriPrefix').value = u'http://edrn/body-system/'
    >>> browser.getControl(name='typeURI').value = u'urn:edrn:types:body-system'
    >>> browser.getControl(name='titleURI').value = u'http://purl.org/dc/terms/title'
    >>> browser.getControl(name='descURI').value = u'http://purl.org/dc/terms/description'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-body-system' in rdfFolder.objectIds()
    True
    >>> bodySystem = rdfFolder['my-body-system']
    >>> bodySystem.title
    'My Body System'
    >>> bodySystem.description
    'Provides body system descriptions.'
    >>> bodySystem.uriPrefix
    'http://edrn/body-system/'
    >>> bodySystem.typeURI
    'urn:edrn:types:body-system'
    >>> bodySystem.titleURI
    'http://purl.org/dc/terms/title'
    >>> bodySystem.descURI
    'http://purl.org/dc/terms/description'
    
Of course, the whole point of this is to provide descriptions of body systems::

    >>> browser.open(portalURL + '/my-rdf-folder/my-body-system/rdf')
    >>> browser.isHtml
    False
    >>> browser.headers['content-type']
    'application/rdf+xml'
    >>> from rdflib import ConjunctiveGraph
    >>> from cStringIO import StringIO
    >>> c = ConjunctiveGraph()
    >>> c.parse(StringIO(browser.contents))
    <Graph...
    >>> len(c)
    66
    >>> for i in c.query('SELECT ?title WHERE { <http://edrn/body-system/11> <http://purl.org/dc/terms/title> ?title . }'):
    ...     print i[0]
    Head & neck, NOS
    
    
Diseases
~~~~~~~~

Diseases affect body systems. They can be added to RDF Folders only::

    >>> browser.open(portalURL)
    >>> browser.getLink(id='disease')
    Traceback (most recent call last):
    ...
    LinkNotFoundError
    >>> browser.open(portalURL + '/my-rdf-folder')
    >>> l = browser.getLink(id='disease')
    >>> l.url.endswith('createObject?type_name=Disease')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My Disease'
    >>> browser.getControl(name='description').value = u'Provides disease descriptions.'
    >>> browser.getControl(name='uriPrefix').value = u'http://edrn/diseases/'
    >>> browser.getControl(name='typeURI').value = u'urn:edrn:types:disease'
    >>> browser.getControl(name='titleURI').value = u'http://purl.org/dc/terms/title'
    >>> browser.getControl(name='descURI').value = u'http://purl.org/dc/terms/description'
    >>> browser.getControl(name='icd9URI').value = u'http://www.who.int/rdf/who.rdf#icd9'
    >>> browser.getControl(name='icd10URI').value = u'http://www.who.int/rdf/who.rdf#icd10'
    >>> browser.getControl(name='bodySysURI').value = u'http://edrn.nci.nih.gov/rdf/terms/body-system'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-disease' in rdfFolder.objectIds()
    True
    >>> disease = rdfFolder['my-disease']
    >>> disease.title
    'My Disease'
    >>> disease.description
    'Provides disease descriptions.'
    >>> disease.uriPrefix
    'http://edrn/diseases/'
    >>> disease.typeURI
    'urn:edrn:types:disease'
    >>> disease.titleURI
    'http://purl.org/dc/terms/title'
    >>> disease.descURI
    'http://purl.org/dc/terms/description'
    >>> disease.icd9URI
    'http://www.who.int/rdf/who.rdf#icd9'
    >>> disease.icd10URI
    'http://www.who.int/rdf/who.rdf#icd10'
    >>> disease.bodySysURI
    'http://edrn.nci.nih.gov/rdf/terms/body-system'    
    
And generated RDF::

    >>> browser.open(portalURL + '/my-rdf-folder/my-disease/rdf')
    >>> browser.isHtml
    False
    >>> browser.headers['content-type']
    'application/rdf+xml'
    >>> c = ConjunctiveGraph()
    >>> c.parse(StringIO(browser.contents))
    <Graph...
    >>> len(c)
    154
    >>> for i in c.query('SELECT ?title WHERE { <http://edrn/diseases/29> <http://purl.org/dc/terms/title> ?title . }'):
    ...     print i[0]
    Malignant neoplasm of other and unspecified parts of mouth
    

Sites
~~~~~

Sites are the institutions that participant in EDRN.  They generate RDF
descriptions that largely deal with addresses of the place and a few other
details. They can be added to RDF Folders only::

    >>> browser.open(portalURL)
    >>> browser.getLink(id='site')
    Traceback (most recent call last):
    ...
    LinkNotFoundError
    >>> browser.open(portalURL + '/my-rdf-folder')
    >>> l = browser.getLink(id='site')
    >>> l.url.endswith('createObject?type_name=Site')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My Site'
    >>> browser.getControl(name='description').value = u'Provides RDF for sites.'
    >>> browser.getControl(name='uriPrefix').value = u'http://edrn/sites/'
    >>> browser.getControl(name='typeURI').value = u'urn:edrn:types:site'
    >>> browser.getControl(name='titleURI').value = u'http://purl.org/dc/terms/title'
    >>> browser.getControl(name='abbrevNameURI').value = u'http://edrn/rdf/rdfs/site.rdf#abbrevName'
    >>> browser.getControl(name='assocMemberSponsorURI').value = u'http://edrn/rdf/rdfs/site.rdf#assocMemberSponsorURI'
    >>> browser.getControl(name='piURI').value = 'http://edrn/rdf/rdfs/site.rdf#pi'
    >>> browser.getControl(name='coPIURI').value = 'http://edrn/rdf/rdfs/site.rdf#copi'
    >>> browser.getControl(name='coIURI').value = 'http://edrn/rdf/rdfs/site.rdf#coi'
    >>> browser.getControl(name='investigatorURI').value = 'http://edrn/rdf/rdfs/site.rdf#investigator'
    >>> browser.getControl(name='staffURI').value = 'http://edrn/rdf/rdfs/site.rdf#staff'
    >>> browser.getControl(name='fundingDateStartURI').value = u'http://edrn/rdf/rdfs/site.rdf#fundingDateStart'
    >>> browser.getControl(name='fundingDateFinishURI').value = u'http://edrn/rdf/rdfs/site.rdf#fundingDateFinish'
    >>> browser.getControl(name='fwaNumberURI').value = u'http://edrn/rdf/rdfs/site.rdf#fwaNumber'
    >>> browser.getControl(name='programURI').value = u'http://edrn/rdf/rdfs/site.rdf#program'
    >>> browser.getControl(name='urlURI').value = u'http://edrn/rdf/rdfs/site.rdf#url'
    >>> browser.getControl(name='memberTypeURI').value = u'http://edrn/rdf/rdfs/site.rdf#memberType'
    >>> browser.getControl(name='histNotesURI').value = u'http://edrn/rdf/rdfs/site.rdf#histNotes'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-site' in rdfFolder.objectIds()
    True
    >>> site = rdfFolder['my-site']
    >>> site.title
    'My Site'
    >>> site.description
    'Provides RDF for sites.'
    >>> site.uriPrefix
    'http://edrn/sites/'
    >>> site.typeURI
    'urn:edrn:types:site'
    >>> site.titleURI
    'http://purl.org/dc/terms/title'
    >>> site.abbrevNameURI
    'http://edrn/rdf/rdfs/site.rdf#abbrevName'
    >>> site.assocMemberSponsorURI
    'http://edrn/rdf/rdfs/site.rdf#assocMemberSponsorURI'
    >>> site.piURI
    'http://edrn/rdf/rdfs/site.rdf#pi'
    >>> site.coPIURI
    'http://edrn/rdf/rdfs/site.rdf#copi'
    >>> site.coIURI
    'http://edrn/rdf/rdfs/site.rdf#coi'
    >>> site.investigatorURI
    'http://edrn/rdf/rdfs/site.rdf#investigator'
    >>> site.staffURI
    'http://edrn/rdf/rdfs/site.rdf#staff'
    >>> site.fundingDateStartURI
    'http://edrn/rdf/rdfs/site.rdf#fundingDateStart'
    >>> site.fundingDateFinishURI
    'http://edrn/rdf/rdfs/site.rdf#fundingDateFinish'
    >>> site.fwaNumberURI
    'http://edrn/rdf/rdfs/site.rdf#fwaNumber'
    >>> site.programURI
    'http://edrn/rdf/rdfs/site.rdf#program'
    >>> site.urlURI
    'http://edrn/rdf/rdfs/site.rdf#url'
    >>> site.memberTypeURI
    'http://edrn/rdf/rdfs/site.rdf#memberType'
    >>> site.histNotesURI
    'http://edrn/rdf/rdfs/site.rdf#histNotes'

We'll save RDF generation for later since it depends on a People RDF source
being present.


Publications
~~~~~~~~~~~~

Publications generate RDF descriptions of the various articles, journal
entries, and other publications produced by EDRN's members.  As with other RDF
sources, they can be added only to RDF folders::

    >>> browser.open(portalURL)
    >>> browser.getLink(id='publication')
    Traceback (most recent call last):
    ...
    LinkNotFoundError
    >>> browser.open(portalURL + '/my-rdf-folder')
    >>> l = browser.getLink(id='publication')
    >>> l.url.endswith('createObject?type_name=Publication')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My Publication'
    >>> browser.getControl(name='description').value = u'Provides RDF for publications.'
    >>> browser.getControl(name='uriPrefix').value = u'http://edrn/pubs/'
    >>> browser.getControl(name='typeURI').value = u'urn:edrn:types:pub'
    >>> browser.getControl(name='titleURI').value = u'http://purl.org/dc/terms/title'
    >>> browser.getControl(name='descURI').value = u'http://purl.org/dc/terms/description'
    >>> browser.getControl(name='abstractURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#abstract'
    >>> browser.getControl(name='authorURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#author'
    >>> browser.getControl(name='issueURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#issue'
    >>> browser.getControl(name='journalURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#journal'
    >>> browser.getControl(name='pmidURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#pmid'
    >>> browser.getControl(name='pubURLURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#pubURL'
    >>> browser.getControl(name='volumeURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#volume'
    >>> browser.getControl(name='yearURI').value = u'http://edrn/rdf/rdfs/pubs.rdf#year'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-publication' in rdfFolder.objectIds()
    True
    >>> pub = rdfFolder['my-publication']
    >>> pub.title
    'My Publication'
    >>> pub.description
    'Provides RDF for publications.'
    >>> pub.uriPrefix
    'http://edrn/pubs/'
    >>> pub.typeURI
    'urn:edrn:types:pub'
    >>> pub.titleURI
    'http://purl.org/dc/terms/title'
    >>> pub.descURI
    'http://purl.org/dc/terms/description'
    >>> pub.abstractURI
    'http://edrn/rdf/rdfs/pubs.rdf#abstract'
    >>> pub.authorURI
    'http://edrn/rdf/rdfs/pubs.rdf#author'
    >>> pub.issueURI
    'http://edrn/rdf/rdfs/pubs.rdf#issue'
    >>> pub.journalURI
    'http://edrn/rdf/rdfs/pubs.rdf#journal'
    >>> pub.pmidURI
    'http://edrn/rdf/rdfs/pubs.rdf#pmid'
    >>> pub.pubURLURI
    'http://edrn/rdf/rdfs/pubs.rdf#pubURL'
    >>> pub.volumeURI
    'http://edrn/rdf/rdfs/pubs.rdf#volume'
    >>> pub.yearURI
    'http://edrn/rdf/rdfs/pubs.rdf#year'

A Publication object provides RDF of course::

    >>> browser.open(portalURL + '/my-rdf-folder/my-publication/rdf')
    >>> browser.isHtml
    False
    >>> browser.headers['content-type']
    'application/rdf+xml'
    >>> c = ConjunctiveGraph()
    >>> c.parse(StringIO(browser.contents))
    <Graph...
    >>> len(c)
    2854
    >>> for i in c.query('SELECT ?title WHERE { <http://edrn/pubs/196> <http://purl.org/dc/terms/title> ?title . }'):
    ...     print i[0]
    Aberrant methylation during cervical carcinogenesis

Where are the author names? CA-582 found that those were missing.

	>>> q = 'SELECT ?author WHERE { <http://edrn/pubs/196> <http://edrn/rdf/rdfs/pubs.rdf#author> ?author . }'
    >>> n = [unicode(i[0]) for i in c.query(q)]
    >>> n.sort()
    >>> n
    [u'Gazdar AF', u'Mathis M', u'Muller C', u'Rathi A', u'Virmani AK', u'Zoechbauer-Mueller S']

Looks like they're fixed.


Protocols
~~~~~~~~~

Protocols generate RDF descriptions of the studies, projects, and other
protocols carried out by EDRN and its cohorts.  As with other RDF sources,
they can be added only to RDF folders::

    >>> browser.open(portalURL)
    >>> browser.getLink(id='protocol')
    Traceback (most recent call last):
    ...
    LinkNotFoundError
    >>> browser.open(portalURL + '/my-rdf-folder')
    >>> l = browser.getLink(id='protocol')
    >>> l.url.endswith('createObject?type_name=Protocol')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My Protocol'
    >>> browser.getControl(name='description').value = u'Provides RDF for protocols.'
    >>> browser.getControl(name='uriPrefix').value = u'http://edrn/protocols/'
    >>> browser.getControl(name='siteSpecURIPrefix').value = u'http://edrn/proto-site-spec/'
    >>> browser.getControl(name='typeURI').value = u'urn:edrn:types:protocol'
    >>> browser.getControl(name='titleURI').value = u'http://purl.org/dc/terms/title'
    >>> browser.getControl(name='abstractURI').value = 'http://edrn/rdf/rdfs/pubs.rdf#abstract'
    >>> browser.getControl(name='involvedInvestigatorSiteURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#involvedInvestigatorSite'
    >>> browser.getControl(name='bmNameURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#bmName'
    >>> browser.getControl(name='coordinateInvestigatorSiteURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#coordinateInvestigatorSite'
    >>> browser.getControl(name='leadInvestigatorSiteURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#leadInvestigatorSite'
    >>> browser.getControl(name='collaborativeGroupTextURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#collaborativeGroupText'
    >>> browser.getControl(name='phasedStatusURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#phasedStatus'
    >>> browser.getControl(name='aimsURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#aims'
    >>> browser.getControl(name='analyticMethodURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#analyticMethod'
    >>> browser.getControl(name='blindingURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#blinding'
    >>> browser.getControl(name='cancerTypeURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#cancerType'
    >>> browser.getControl(name='commentsURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#comments'
    >>> browser.getControl(name='dataSharingPlanURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#dataSharingPlan'
    >>> browser.getControl(name='inSituDataSharingPlanURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#inSituDataSharingPlan'
    >>> browser.getControl(name='finishDateURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#finishDate'
    >>> browser.getControl(name='estimatedFinishDateURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#estimatedFinishDate'
    >>> browser.getControl(name='startDateURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#startDate'
    >>> browser.getControl(name='designURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#design'
    >>> browser.getControl(name='fieldOfResearchURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#fieldOfResearch'
    >>> browser.getControl(name='abbreviatedNameURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#abbreviatedName'
    >>> browser.getControl(name='objectiveURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#objective'
    >>> browser.getControl(name='projectFlagURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#projectFlag'
    >>> browser.getControl(name='protocolTypeURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#protocolType'
    >>> browser.getControl(name='publicationsURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#publications'
    >>> browser.getControl(name='outcomeURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#outcome'
    >>> browser.getControl(name='secureOutcomeURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#secureOutcome'
    >>> browser.getControl(name='finalSampleSizeURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#finalSampleSize'
    >>> browser.getControl(name='plannedSampleSizeURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#plannedSampleSize'
    >>> browser.getControl(name='isAPilotForURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#isAPilotFor'
    >>> browser.getControl(name='obtainsDataFromURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#obtainsDataFrom'
    >>> browser.getControl(name='providesDataToURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#providesDataTo'
    >>> browser.getControl(name='contributesSpecimensURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#contributesSpecimens'
    >>> browser.getControl(name='obtainsSpecimensFromURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#obtainsSpecimensFrom'
    >>> browser.getControl(name='hasOtherRelationshipURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#hasOtherRelationship'
    >>> browser.getControl(name='animalSubjectTrainingReceivedURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#animalSubjectTrainingReceived'
    >>> browser.getControl(name='humanSubjectTrainingReceivedURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#humanSubjectTrainingReceived'
    >>> browser.getControl(name='irbApprovalNeededURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#irbApprovalNeeded'
    >>> browser.getControl(name='currentIRBApprovalDateURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#currentIRBApprovalDate'
    >>> browser.getControl(name='originalIRBApprovalDateURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#originalIRBApprovalDate'
    >>> browser.getControl(name='irbExpirationDateURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#irbExpirationDate'
    >>> browser.getControl(name='generalIRBNotesURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#generalIRBNotes'
    >>> browser.getControl(name='irbNumberURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#irbNumber'
    >>> browser.getControl(name='siteRoleURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#siteRole'
    >>> browser.getControl(name='reportingStageURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#reportingStage'
    >>> browser.getControl(name='eligibilityCriteriaURI').value = 'http://edrn/rdf/rdfs/protocols.rdf#eligibilityCriteria'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-protocol' in rdfFolder.objectIds()
    True
    >>> proto = rdfFolder['my-protocol']
    >>> proto.title
    'My Protocol'
    >>> proto.description
    'Provides RDF for protocols.'
    >>> proto.uriPrefix
    'http://edrn/protocols/'
    >>> proto.siteSpecURIPrefix
    'http://edrn/proto-site-spec/'
    >>> proto.typeURI
    'urn:edrn:types:protocol'
    >>> proto.titleURI
    'http://purl.org/dc/terms/title'
    >>> proto.abstractURI
    'http://edrn/rdf/rdfs/pubs.rdf#abstract'
    >>> proto.involvedInvestigatorSiteURI
    'http://edrn/rdf/rdfs/protocols.rdf#involvedInvestigatorSite'
    >>> proto.bmNameURI
    'http://edrn/rdf/rdfs/protocols.rdf#bmName'
    >>> proto.coordinateInvestigatorSiteURI
    'http://edrn/rdf/rdfs/protocols.rdf#coordinateInvestigatorSite'
    >>> proto.leadInvestigatorSiteURI
    'http://edrn/rdf/rdfs/protocols.rdf#leadInvestigatorSite'
    >>> proto.collaborativeGroupTextURI
    'http://edrn/rdf/rdfs/protocols.rdf#collaborativeGroupText'
    >>> proto.phasedStatusURI
    'http://edrn/rdf/rdfs/protocols.rdf#phasedStatus'
    >>> proto.aimsURI
    'http://edrn/rdf/rdfs/protocols.rdf#aims'
    >>> proto.analyticMethodURI
    'http://edrn/rdf/rdfs/protocols.rdf#analyticMethod'
    >>> proto.blindingURI
    'http://edrn/rdf/rdfs/protocols.rdf#blinding'
    >>> proto.cancerTypeURI
    'http://edrn/rdf/rdfs/protocols.rdf#cancerType'
    >>> proto.commentsURI
    'http://edrn/rdf/rdfs/protocols.rdf#comments'
    >>> proto.dataSharingPlanURI
    'http://edrn/rdf/rdfs/protocols.rdf#dataSharingPlan'
    >>> proto.inSituDataSharingPlanURI
    'http://edrn/rdf/rdfs/protocols.rdf#inSituDataSharingPlan'
    >>> proto.finishDateURI
    'http://edrn/rdf/rdfs/protocols.rdf#finishDate'
    >>> proto.estimatedFinishDateURI
    'http://edrn/rdf/rdfs/protocols.rdf#estimatedFinishDate'
    >>> proto.startDateURI
    'http://edrn/rdf/rdfs/protocols.rdf#startDate'
    >>> proto.designURI
    'http://edrn/rdf/rdfs/protocols.rdf#design'
    >>> proto.fieldOfResearchURI
    'http://edrn/rdf/rdfs/protocols.rdf#fieldOfResearch'
    >>> proto.abbreviatedNameURI
    'http://edrn/rdf/rdfs/protocols.rdf#abbreviatedName'
    >>> proto.objectiveURI
    'http://edrn/rdf/rdfs/protocols.rdf#objective'
    >>> proto.projectFlagURI
    'http://edrn/rdf/rdfs/protocols.rdf#projectFlag'
    >>> proto.protocolTypeURI
    'http://edrn/rdf/rdfs/protocols.rdf#protocolType'
    >>> proto.publicationsURI
    'http://edrn/rdf/rdfs/protocols.rdf#publications'
    >>> proto.outcomeURI
    'http://edrn/rdf/rdfs/protocols.rdf#outcome'
    >>> proto.secureOutcomeURI
    'http://edrn/rdf/rdfs/protocols.rdf#secureOutcome'
    >>> proto.finalSampleSizeURI
    'http://edrn/rdf/rdfs/protocols.rdf#finalSampleSize'
    >>> proto.plannedSampleSizeURI
    'http://edrn/rdf/rdfs/protocols.rdf#plannedSampleSize'
    >>> proto.isAPilotForURI
    'http://edrn/rdf/rdfs/protocols.rdf#isAPilotFor'
    >>> proto.obtainsDataFromURI
    'http://edrn/rdf/rdfs/protocols.rdf#obtainsDataFrom'
    >>> proto.providesDataToURI
    'http://edrn/rdf/rdfs/protocols.rdf#providesDataTo'
    >>> proto.contributesSpecimensURI
    'http://edrn/rdf/rdfs/protocols.rdf#contributesSpecimens'
    >>> proto.obtainsSpecimensFromURI
    'http://edrn/rdf/rdfs/protocols.rdf#obtainsSpecimensFrom'
    >>> proto.hasOtherRelationshipURI
    'http://edrn/rdf/rdfs/protocols.rdf#hasOtherRelationship'
    >>> proto.animalSubjectTrainingReceivedURI
    'http://edrn/rdf/rdfs/protocols.rdf#animalSubjectTrainingReceived'
    >>> proto.humanSubjectTrainingReceivedURI
    'http://edrn/rdf/rdfs/protocols.rdf#humanSubjectTrainingReceived'
    >>> proto.irbApprovalNeededURI
    'http://edrn/rdf/rdfs/protocols.rdf#irbApprovalNeeded'
    >>> proto.currentIRBApprovalDateURI
    'http://edrn/rdf/rdfs/protocols.rdf#currentIRBApprovalDate'
    >>> proto.originalIRBApprovalDateURI
    'http://edrn/rdf/rdfs/protocols.rdf#originalIRBApprovalDate'
    >>> proto.irbExpirationDateURI
    'http://edrn/rdf/rdfs/protocols.rdf#irbExpirationDate'
    >>> proto.generalIRBNotesURI
    'http://edrn/rdf/rdfs/protocols.rdf#generalIRBNotes'
    >>> proto.irbNumberURI
    'http://edrn/rdf/rdfs/protocols.rdf#irbNumber'
    >>> proto.siteRoleURI
    'http://edrn/rdf/rdfs/protocols.rdf#siteRole'
    >>> proto.reportingStageURI
    'http://edrn/rdf/rdfs/protocols.rdf#reportingStage'
    >>> proto.eligibilityCriteriaURI
    'http://edrn/rdf/rdfs/protocols.rdf#eligibilityCriteria'

A Protocol also provides RDF, as a matter of course::

    >>> browser.open(portalURL + '/my-rdf-folder/my-protocol/rdf')
    >>> browser.isHtml
    False
    >>> browser.headers['content-type']
    'application/rdf+xml'
    >>> c = ConjunctiveGraph()
    >>> c.parse(StringIO(browser.contents))
    <Graph...
    >>> len(c)
    720
    >>> for i in c.query('SELECT ?title WHERE { <http://edrn/protocols/36> <http://purl.org/dc/terms/title> ?title . }'):
    ...     print i[0]
    Preliminary Clinical Characterization of Serum Biomarkers for Colorectal Neoplasms
    >>> for i in c.query('SELECT ?irbNumber WHERE { <http://edrn/proto-site-spec/93-92> <http://edrn/rdf/rdfs/protocols.rdf#irbNumber> ?irbNumber . }'):
    ...     print i[0]
    06-10-92-0053

Issue CA-285 complained that there were numeric codes instead of descriptive
names for the fields of research in a protocol.  Checking::

    >>> results = c.query('SELECT ?for WHERE { <http://edrn/protocols/67> <http://edrn/rdf/rdfs/protocols.rdf#fieldOfResearch> ?for . }')
    >>> results = [str(i[0]) for i in results]
    >>> results.sort()
    >>> results
    ['Genomics', 'Metabolomics', 'Proteomics']

See? All better!  But what about involved investigator sites?

    >>> browser.open(portalURL + '/my-rdf-folder/my-protocol/rdf')
    >>> results = [i[0] for i in c.query('SELECT ?involvedInvestigatorSite WHERE { <http://edrn/protocols/99> <http://edrn/rdf/rdfs/protocols.rdf#involvedInvestigatorSite> ?involvedInvestigatorSite . }')]
    >>> results.sort()
    >>> results
    [rdflib.URIRef('http://edrn/sites/66'), rdflib.URIRef('http://edrn/sites/67')]


People
~~~~~~

A Registered Person generates RDF descriptions of people who are registered
with EDRN.  Just like all the other RDF sources, they too too may be added
solely to RDF folders::

    >>> browser.open(portalURL)
    >>> browser.getLink(id='registered-person')
    Traceback (most recent call last):
    ...
    LinkNotFoundError
    >>> browser.open(portalURL + '/my-rdf-folder')
    >>> l = browser.getLink(id='registered-person')
    >>> l.url.endswith('createObject?type_name=Registered+Person')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My Registered Person Generator'
    >>> browser.getControl(name='description').value = u'Provides RDF for registered people.'
    >>> browser.getControl(name='uriPrefix').value = u'http://edrn/registered-person/'
    >>> browser.getControl(name='typeURI').value = u'urn:edrn:types:registered-person'
    >>> browser.getControl(name='firstNameURI').value = 'http://xmlns.com/foaf/0.1/givenname'
    >>> browser.getControl(name='middleNameURI').value = 'http://edrn.rdf/rdfs/people.rdf#middleName'
    >>> browser.getControl(name='lastNameURI').value = 'http://xmlns.com/foaf/0.1/surname'
    >>> browser.getControl(name='phoneURI').value = 'http://xmlns.com/foaf/0.1/phone'
    >>> browser.getControl(name='emailURI').value = 'http://xmlns.com/foaf/0.1/mbox'
    >>> browser.getControl(name='faxURI').value = 'http://www.w3.org/2001/vcard-rdf/3.0#fax'
    >>> browser.getControl(name='specialtyURI').value = 'http://edrn.rdf/rdfs/people.rdf#specialty'
    >>> browser.getControl(name='photoURI').value = 'http://xmlns.com/foaf/0.1/img'
    >>> browser.getControl(name='edrnTitleURI').value = 'http://edrn.rdf/rdfs/people.rdf#edrnTitle'
    >>> browser.getControl(name='siteURI').value = 'http://edrn.rdf/rdfs/people.rdf#site'
    >>> browser.getControl(name='userIDURI').value = 'http://xmlns.com/foaf/0.1/accountName'
    >>> browser.getControl(name='addr1URI').value = u'http://edrn/rdf/rdfs/site.rdf#addr1'
    >>> browser.getControl(name='addr2URI').value = u'http://edrn/rdf/rdfs/site.rdf#addr2'
    >>> browser.getControl(name='cityURI').value = u'http://edrn/rdf/rdfs/site.rdf#city'
    >>> browser.getControl(name='stateURI').value = u'http://edrn/rdf/rdfs/site.rdf#state'
    >>> browser.getControl(name='zipURI').value = u'http://edrn/rdf/rdfs/site.rdf#zip'
    >>> browser.getControl(name='countryURI').value = u'http://edrn/rdf/rdfs/site.rdf#country'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-registered-person-generator' in rdfFolder.objectIds()
    True
    >>> mrpg = rdfFolder['my-registered-person-generator']
    >>> mrpg.title
    'My Registered Person Generator'
    >>> mrpg.description
    'Provides RDF for registered people.'
    >>> mrpg.uriPrefix
    'http://edrn/registered-person/'
    >>> mrpg.typeURI
    'urn:edrn:types:registered-person'
    >>> mrpg.firstNameURI
    'http://xmlns.com/foaf/0.1/givenname'
    >>> mrpg.middleNameURI
    'http://edrn.rdf/rdfs/people.rdf#middleName'
    >>> mrpg.lastNameURI
    'http://xmlns.com/foaf/0.1/surname'
    >>> mrpg.phoneURI
    'http://xmlns.com/foaf/0.1/phone'
    >>> mrpg.emailURI
    'http://xmlns.com/foaf/0.1/mbox'
    >>> mrpg.faxURI
    'http://www.w3.org/2001/vcard-rdf/3.0#fax'
    >>> mrpg.specialtyURI
    'http://edrn.rdf/rdfs/people.rdf#specialty'
    >>> mrpg.photoURI
    'http://xmlns.com/foaf/0.1/img'
    >>> mrpg.edrnTitleURI
    'http://edrn.rdf/rdfs/people.rdf#edrnTitle'
    >>> mrpg.siteURI
    'http://edrn.rdf/rdfs/people.rdf#site'
    >>> mrpg.userIDURI
    'http://xmlns.com/foaf/0.1/accountName'
    >>> mrpg.addr1URI
    'http://edrn/rdf/rdfs/site.rdf#addr1'
    >>> mrpg.addr2URI
    'http://edrn/rdf/rdfs/site.rdf#addr2'
    >>> mrpg.cityURI
    'http://edrn/rdf/rdfs/site.rdf#city'
    >>> mrpg.stateURI
    'http://edrn/rdf/rdfs/site.rdf#state'
    >>> mrpg.zipURI
    'http://edrn/rdf/rdfs/site.rdf#zip'
    >>> mrpg.countryURI
    'http://edrn/rdf/rdfs/site.rdf#country'

RDF generation? You got it::

    >>> browser.open(portalURL + '/my-rdf-folder/my-registered-person-generator/rdf')
    >>> browser.isHtml
    False
    >>> browser.headers['content-type']
    'application/rdf+xml'
    >>> c = ConjunctiveGraph()
    >>> c.parse(StringIO(browser.contents))
    <Graph...
    >>> len(c)
    66
    >>> for i in c.query('SELECT ?givenname WHERE { <http://edrn/registered-person/29> <http://xmlns.com/foaf/0.1/givenname> ?givenname . }'):
    ...     print i[0]
    Mark
    >>> for i in c.query('SELECT ?accountName WHERE { <http://edrn/registered-person/51> <http://xmlns.com/foaf/0.1/accountName> ?accountName . }'):
    ...     print i[0]
    cedelste
    

New Site Fields: Investigators and Staff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recently, fields were added to the Site view in the RDF database that linked
to people, identifying the PI, Co-Is, and other staff.  RDF generation for
sites should contain rdf:resource links to those people.  Checking::
    
    >>> browser.open(portalURL + '/my-rdf-folder/my-site/rdf')
    >>> browser.isHtml
    False
    >>> browser.headers['content-type']
    'application/rdf+xml'
    >>> c = ConjunctiveGraph()
    >>> c.parse(StringIO(browser.contents))
    <Graph...
    >>> len(c)
    517
    >>> for i in c.query('SELECT ?title WHERE { <http://edrn/sites/87> <http://purl.org/dc/terms/title> ?title . }'):
    ...     print i[0]
    National Cancer Institute
    >>> for i in c.query('SELECT ?pi WHERE { <http://edrn/sites/87> <http://edrn/rdf/rdfs/site.rdf#pi> ?pi . }'):
    ...     print i[0]
    http://edrn/registered-person/1015


Committees
~~~~~~~~~~

Committees are groups of registered people who work together to delay in
accomplishing some task.  They can be added solely to RDF Folders::

    >>> browser.open(portalURL)
    >>> browser.getLink(id='committee')
    Traceback (most recent call last):
    ...
    LinkNotFoundError
    >>> browser.open(portalURL + '/my-rdf-folder')
    >>> l = browser.getLink(id='committee')
    >>> l.url.endswith('createObject?type_name=Committee')
    True
    >>> l.click()
    >>> browser.getControl(name='title').value = u'My Committees'
    >>> browser.getControl(name='description').value = u'Provides committee descriptions.'
    >>> browser.getControl(name='uriPrefix').value = u'http://edrn/committees/'
    >>> browser.getControl(name='typeURI').value = u'urn:edrn:types:committee'
    >>> browser.getControl(name='titlePredicateURI').value = u'http://purl.org/dc/terms/title'
    >>> browser.getControl(name='abbreviatedNamePredicateURI').value = u'http://edrn/rdf/rdfs/site.rdf#abbreviatedName'
    >>> browser.getControl(name='committeeTypePredicateURI').value = u'http://edrn/rdf/rdfs/site.rdf#committeeType'
    >>> browser.getControl(name='chairPredicateURI').value = u'http://edrn/rdf/rdfs/site.rdf#chair'
    >>> browser.getControl(name='coChairPredicateURI').value = u'http://edrn/rdf/rdfs/site.rdf#coChair'
    >>> browser.getControl(name='consultantPredicateURI').value = u'http://edrn/rdf/rdfs/site.rdf#consultant'
    >>> browser.getControl(name='memberPredicateURI').value = u'http://edrn/rdf/rdfs/site.rdf#member'
    >>> browser.getControl(name='form.button.save').click()
    >>> 'my-committees' in rdfFolder.objectIds()
    True
    >>> committees = rdfFolder['my-committees']
    >>> committees.title
    'My Committees'
    >>> committees.description
    'Provides committee descriptions.'
    >>> committees.uriPrefix
    'http://edrn/committees/'
    >>> committees.typeURI
    'urn:edrn:types:committee'
    >>> committees.titlePredicateURI
    'http://purl.org/dc/terms/title'
    >>> committees.abbreviatedNamePredicateURI
    'http://edrn/rdf/rdfs/site.rdf#abbreviatedName'
    >>> committees.committeeTypePredicateURI
    'http://edrn/rdf/rdfs/site.rdf#committeeType'
    >>> committees.chairPredicateURI
    'http://edrn/rdf/rdfs/site.rdf#chair'
    >>> committees.coChairPredicateURI
    'http://edrn/rdf/rdfs/site.rdf#coChair'
    >>> committees.consultantPredicateURI
    'http://edrn/rdf/rdfs/site.rdf#consultant'
    >>> committees.memberPredicateURI
    'http://edrn/rdf/rdfs/site.rdf#member'
    
And generated RDF::

    >>> browser.open(portalURL + '/my-rdf-folder/my-committees/rdf')
    >>> browser.isHtml
    False
    >>> browser.headers['content-type']
    'application/rdf+xml'
    >>> c = ConjunctiveGraph()
    >>> c.parse(StringIO(browser.contents))
    <Graph...
    >>> len(c)
    12
    >>> for i in c.query('SELECT ?title WHERE { <http://edrn/committees/8> <http://purl.org/dc/terms/title> ?title . }'):
    ...     print i[0]
    Data Sharing and Informatics Subcommittee

That's it.
