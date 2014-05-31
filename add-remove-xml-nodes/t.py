# -*- python -*-

'''
python cElementTree first node
python cElementTree append node
python cElementTree iter index
python cElementTree first element
python cElementTree deepcopy
python cElementTree clone node
python cElementTree deepcopy find node
'''

from __future__ import print_function
import argparse
from copy import deepcopy
import sys
import xml.etree.cElementTree as ET
import ConfigParser
import random

config = ConfigParser.RawConfigParser()

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--rand", help="choose random project to move", action="store_true")
parser.add_argument("-f", "--file", help="file to add/remove note to/from")
parser.add_argument("-r", "--remove", help="node to remove")
parser.add_argument("-a", "--add", help="node to add")

args = parser.parse_args()

inputfile = args.file
if not inputfile:
    inputfile = "default.xml"

document = ET.parse(inputfile)
root = document.getroot()

if args.rand:
    projList = []
    for elem in document.iter('project'):
        projList.append(elem.attrib['name'])
    print(random.choice(projList))

# find a project element and remove it
if args.remove:
    for elem in document.iter('project'):
        if elem.attrib['name'] == args.remove:
            root.remove(elem)
            break

# add a project element
if args.add:
    warn=""
    for elem in document.iter('project'):
        if elem.attrib['name'] == args.add:
            warn = "WARNING: %s already exists, not adding" % elem.attrib['name']
            print (warn, file=sys.stderr)
    if warn == "":
        clone = deepcopy(root.find('project'))
        clone.attrib['name'] = args.add
        clone.attrib['path'] = args.add
        root.insert(1,clone)

document.write(inputfile, encoding='utf-8', xml_declaration=True)
