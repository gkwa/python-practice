import random, string
import simplejson as json

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

data_raw=open("Windows_Roles_And_Features.template").read()
data = json.loads(data_raw)

# pretty print
with open('t3_2.json', 'w') as outfile:
  json.dump(data, outfile, indent=2 * ' ')

dns = data['Resources']['myDNSRecord']['Properties']['Name']['Fn::Join'][1][0]
newdns = randomword(2)
data['Resources']['myDNSRecord']['Properties']['Name']['Fn::Join'][1][0] = newdns

# write out result
with open('t3_3.json', 'w') as outfile:
  json.dump(data, outfile, indent=2 * ' ')
