#!/usr/bin/env python

from lxml import etree
from lxml.html import parse
from pprint import pprint
import pandas as pd
from pandas import *

import yaml
import pprint

s1 = {}
with open("list.yml", 'r') as stream:
    try:
        s1 = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

pp = pprint.PrettyPrinter(indent=2)
# pp.pprint(s1)

dfm=None
i=1
for server, file in s1.items():
    file = s1[server]
    xml = parse(file)
    dct = xml.xpath("//storage")[-1].attrib
    df = pd.DataFrame(dct.items(), columns=['Field', server])
    dfm = df if i==1 else pd.merge(dfm, df, on='Field', how='outer')
    i+=1

pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

print(dfm.T)
