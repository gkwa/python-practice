import simplejson as json

data_raw=open("t2_1.json").read()
data = json.loads(data_raw)

# pretty print
with open('t2_2.json', 'w') as outfile:
  json.dump(data, outfile, indent=2 * ' ')

# add key/value
for image in data['images']:
    image['viewurl'] = '/view?imagekey=%s' %(image['imagekey'])

# write out result
with open('t2_3.json', 'w') as outfile:
  json.dump(data, outfile, indent=2 * ' ')
