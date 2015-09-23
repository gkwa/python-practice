# FIXME: i'm skipping non-ascii urls in try/except



from __future__ import print_function
from lxml import etree
from lxml.html import parse
from pprint import pprint

f = open('out.csv','w')

data = parse('wwwdev5.xml')



# for urldata in data.xpath('//urldata')[10:20]:
for urldata in data.xpath('//urldata'):
    url_elem = urldata.xpath('./url')[0]
    url=url_elem.text.strip()

    dltime_list=urldata.xpath('.//dltime')
    dltime=''
    if 1==len(dltime_list):
        dltime = dltime_list[0].text.strip()

    name_list=urldata.xpath('.//name')
    name=''
    if 1==len(name_list):
        name = name_list[0].text.strip()

    parent_list=urldata.xpath('.//parent')
    parent_url=''
    if 1==len(parent_list):
        parent_url = parent_list[0].text.strip()

    valid_elem=urldata.xpath('.//valid')[0]
    status=valid_elem.get('result')

    try:
        print("{name}~{status}~{dltime}~{parent_url}~{url}".format(
            status=status
            ,dltime=dltime
            ,url=url
            ,name=name
            ,parent_url=parent_url
        ),file=f)
    except:
        pass
