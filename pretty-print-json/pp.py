# -*- python -*-

# http://stackoverflow.com/questions/12943819/how-to-python-prettyprint-a-json-file

import json

filename='pp.dat'

#load file into jsonstring variable
jsonstring=''
with open (filename, "r") as myfile: jsonstring=myfile.read()

jsonParsed = json.loads(jsonstring)
print json.dumps(jsonParsed,indent=2)
