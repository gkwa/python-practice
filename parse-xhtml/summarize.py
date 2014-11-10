"""
http://lxml.de/1.3/tutorial.html
http://stackoverflow.com/questions/9919493/parsing-html-table-using-python-htmlparser-or-lxml
http://stackoverflow.com/questions/14570857/retrieve-an-xpath-text-contains-using-text
http://stackoverflow.com/questions/15022984/xpath-extract-first-part-of-span-with-strong-nested-inside
http://stackoverflow.com/questions/14570857/retrieve-an-xpath-text-contains-using-text

Class help:
http://stackoverflow.com/questions/1535327/python-how-to-print-a-class-or-objects-of-class-using-print

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
          return "<Record month:%s region:%s product:%s productPrice:%s RegionTotal:%s>" % (self.month, self.region, self.product_title, self.product_price,  self.region_total)

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

for tpl in [tsept, toct]:
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

# pprint(records)

from sets import Set

prods = Set()
for r in records:
    prods.add(r.product_title)

# print "\n".join(sorted(str(e) for e in prods))

regions = Set()
for r in records:
    regions.add(r.region)

months = ['September','October']

print "Product\tRegion\t%s\t%s" %(months[0],months[1])

summary={}
for prod in sorted(str(p) for p in prods):
    for region in sorted(str(r) for r in regions):
        key = "%s\t%s" %(prod,region)
        if not key in summary:
            summary[key] = { months[0]: 0, months[1]: 0}
        for month in months:
            for record in records:
                if (record.month == month) and (record.product_title == prod) and (record.region == region):
                    summary[key][month] = record.product_price

for key in summary:
    print "%s\t%s\t%s" %(key,summary[key][months[0]],summary[key][months[1]])
