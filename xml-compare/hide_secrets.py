#!/usr/bin/env python
# -*- python -*-

import argparse
import os
from lxml import etree
from xml.etree.ElementTree import ElementTree

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file",help="xml file")
args = parser.parse_args()

parser = etree.XMLParser(strip_cdata=False)
t = etree.parse(args.file,parser)

for elem in t.iterfind('storage'):
    for att in [
            'mysql_backup_pass'
            ,'aws_s3_secret'
            ,'smtp_pass'
            ,'smtp_login'
            ,'bc_api_key'
            ,'bc_username'
            ,'slsreport_mysql_user'
            ,'slsreport_mysql_pass'
    ]:
        # print 'checking %s against %s' % (att,elem.attrib)
        if att in elem.attrib:
            # print 'found %s' % att
            del elem.attrib[att]

t.write(args.file,
        pretty_print=True,
        xml_declaration=True,
        encoding=t.docinfo.encoding,
        standalone=t.docinfo.standalone
)
