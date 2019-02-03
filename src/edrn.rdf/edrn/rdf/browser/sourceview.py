# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.
'''
EDRN RDF Service: body system UI.
'''

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SourceView(BrowserView):
    '''Abstract view base for RDF data sources.'''


class BodySystemView(SourceView):
    '''Default view for a Body System.'''
    __call__ = ViewPageTemplateFile('templates/bodysystem.pt')
    

class DiseaseView(SourceView):
    '''Default view for a Disease.'''
    __call__ = ViewPageTemplateFile('templates/disease.pt')
    

class SiteView(SourceView):
    '''Default view for a Site.'''
    __call__ = ViewPageTemplateFile('templates/site.pt')
    
    
class PublicationView(SourceView):
    '''Default view for a Publication'''
    __call__ = ViewPageTemplateFile('templates/publication.pt')
    

class ProtocolView(SourceView):
    '''Default view for a Protocol'''
    __call__ = ViewPageTemplateFile('templates/protocol.pt')
    
class RegisteredPersonView(SourceView):
    '''Default view for a Registered Person'''
    __call__ = ViewPageTemplateFile('templates/registeredperson.pt')

class CommitteeView(SourceView):
    '''Default view for a Committee'''
    __call__ = ViewPageTemplateFile('templates/committee.pt')
