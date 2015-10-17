import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('/Users/demo/Downloads/testpython-f07fef62f83b.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

# wks = gc.open("Where is the money Lebowski?").sheet1
# wks = gc.open("test-python-spreadsheet").sheet1

# open by key:
# wks = gc.open_by_key("1t2g6kBjpL4a-Al6ZdIjA4SocozgsVBK0tT5Q0sJKRHE").sheet1

# open by url:
wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1GAMM-9MEPWkustx3HD7uh6tYvNIy3B5rlDUEafir4BU/edit#gid=0").sheet1

# wks.update_acell('B2', "it's down there somewhere, let me take another look.")


# list of lists / the whole spreadsheet
lol = wks.get_all_values()

import pprint
pprint.pprint(lol,width=200)


# Fetch a cell range
# cell_list = wks.range('A1:B7')
