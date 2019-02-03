# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EDRN RDF Service: utilities.
'''

import pymssql
from edrn.rdf.interfaces import IRDFDatabase
from zope.interface import implements

class RDFDatabase(object):
    '''Default RDF databaes: provided by DMCC via SQL Server.'''
    implements(IRDFDatabase)
    def connect(self):
        return pymssql.connect(
            user='ekeuser',
            password='G00dby3!!*',
            host='localhost:1433',
            database='dbEKE'
        )
    
