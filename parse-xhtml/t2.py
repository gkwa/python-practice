"""
"""

header_oct_price=5763.60
header_sept_price=4651.42

class Record:
    def __init__(self, month, region):
        self.month = month.strip()
        self.region = region.strip()
        self.product_title = ''
        self.product_price = 0

    def displayEmployee(self):
        print "Region : ", self.region

    def __repr__(self):
          return "<Record month:%s region:%s product:%s productPrice:%s RegionTotal:%s>" % (self.month, self.region, self.product_title, self.product_price, self.region_total)

    def __str__(self):
        return "From str method of Test: month is %s, region is %s" % (self.month, self.region)

from lxml import etree
from lxml.html import parse
from pprint import pprint

page = parse('f.html')

# September
tsept = ("September", page.xpath("//span[1 and @class='c7' and .='Usage']/ancestor::table[@class='c17']")[1])
# print etree.tostring(t,pretty_print=True)

# October
toct = ("October", page.xpath("//span[2 and @class='c7' and .='Usage']/ancestor::table[@class='c17']")[0])
# print etree.tostring(t,pretty_print=True)

records = []

for tpl in [toct,tsept]:
    month = tpl[0]
    obj = tpl[1]
    monthly_total=0
    for region in obj.xpath(".//th[@class='c6']"):

        region_table = region.xpath('ancestor::table[1]')[0]
        t1 = region_table.xpath(".//*[text()='Region Total:']")[0]
        t2 = t1.xpath('ancestor::tr[1]')[0]
        region_total = t2.xpath('./td[2]/strong')[0].text
        region_total = region_total.replace(',','').replace('$','')
        monthly_total+= float(region_total)

        # print len(totals)
        for total in region_table.xpath(".//*[text()='Total:']"):
            r = Record(month.strip(),region.text.strip())
            r.region_total = region_total.strip()
            prodtable = total.xpath('ancestor::table[1]')[0]
            r.product_title = prodtable.xpath('.//th[1]')[0].text.strip()
            tmp = prodtable.xpath(".//*[contains(.,'$')]")[-1].text
            r.product_price = tmp.replace('$','').replace(',','').strip()

            records.append(r)
    print "Monthly total for %s: $%s" %(month,monthly_total)
    print "Header price difference ($%s-$%s): %s" %(header_sept_price,header_oct_price,header_oct_price-header_sept_price)

pprint(records)

