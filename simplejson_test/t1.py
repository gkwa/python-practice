# -*- python, coding: utf-8  -*-

import simplejson as json
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], sort_keys=True, indent=2 * ' '))
