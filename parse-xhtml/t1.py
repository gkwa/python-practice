"""
http://lxml.de/1.3/tutorial.html
http://stackoverflow.com/questions/9919493/parsing-html-table-using-python-htmlparser-or-lxml
http://stackoverflow.com/questions/14570857/retrieve-an-xpath-text-contains-using-text
http://stackoverflow.com/questions/15022984/xpath-extract-first-part-of-span-with-strong-nested-inside
http://stackoverflow.com/questions/14570857/retrieve-an-xpath-text-contains-using-text
"""

from lxml import etree
from lxml.html import parse

page = parse('f.html')

# September
t = page.xpath("//span[1 and @class='c7' and .='Usage']/ancestor::table[@class='c17']")[1]
print etree.tostring(t,pretty_print=True)

# October
t = page.xpath("//span[2 and @class='c7' and .='Usage']/ancestor::table[@class='c17']")[0]
print etree.tostring(t,pretty_print=True)
