from lxml import etree
from lxml.html import parse
from pprint import pprint
import pandas as pd
from pandas import *

pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

xml1 = parse('slsserver_autogen_LiveDE.xml')
dct1 = xml1.xpath("//storage")[1].attrib
df1 = pd.DataFrame(dct1.items(),columns=['Field', 'LiveDE'])

xml2 = parse('slsserver_autogen_LiveJP.xml')
dct2 = xml2.xpath("//storage")[1].attrib
df2 = pd.DataFrame(dct2.items(),columns=['Field', 'LiveJP'])
m1 = pd.merge(df1, df2, on='Field', how='outer')

xml3 = parse('slsserver_autogen_LiveIN.xml')
dct3 = xml3.xpath("//storage")[1].attrib
df3 = pd.DataFrame(dct3.items(),columns=['Field', 'LiveIN'])
m2 = pd.merge(m1, df3, on='Field', how='outer')

xml4 = parse('slsserver_autogen_LiveSA.xml')
dct4 = xml4.xpath("//storage")[1].attrib
df4 = pd.DataFrame(dct4.items(),columns=['Field', 'LiveSA'])
m3 = pd.merge(m2, df4, on='Field', how='outer')

xml5 = parse('slsserver_autogen_LiveAU.xml')
dct5 = xml5.xpath("//storage")[1].attrib
df5 = pd.DataFrame(dct5.items(),columns=['Field', 'LiveAU'])
m4 = pd.merge(m3, df5, on='Field', how='outer')

xml6 = parse('slsserver_autogen_LiveSG.xml')
dct6 = xml6.xpath("//storage")[1].attrib
df6 = pd.DataFrame(dct6.items(),columns=['Field', 'LiveSG'])
m5 = pd.merge(m4, df6, on='Field', how='outer')

xml7 = parse('slsserver_autogen_LiveEU.xml')
dct7 = xml7.xpath("//storage")[1].attrib
df7 = pd.DataFrame(dct7.items(),columns=['Field', 'LiveEU'])
m6 = pd.merge(m5, df7, on='Field', how='outer')

xml8 = parse('slsserver_autogen_LiveUSEast.xml')
dct8 = xml8.xpath("//storage")[1].attrib
df8 = pd.DataFrame(dct8.items(),columns=['Field', 'LiveUSEast'])
m7 = pd.merge(m6, df8, on='Field', how='outer')

xml9 = parse('slsserver_autogen_LiveUS.xml')
dct9 = xml9.xpath("//storage")[1].attrib
df9 = pd.DataFrame(dct9.items(),columns=['Field', 'LiveUS'])
m8 = pd.merge(m7, df9, on='Field', how='outer')

xml10 = parse('slsserver_autogen_LiveHK.xml')
dct10 = xml10.xpath("//storage")[1].attrib
df10 = pd.DataFrame(dct10.items(),columns=['Field', 'LiveHK'])
m9 = pd.merge(m8, df10, on='Field', how='outer')

m9 = m9
n1 = m9.T

print n1
print m9
