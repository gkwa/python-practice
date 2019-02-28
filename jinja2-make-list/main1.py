import re

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("tests", "templates")
)


def highlight(txt):
    return "**%s**" % txt


def format_list(list_, pattern):
    return [pattern % s for s in list_]


env.filters["highlight"] = highlight
env.filters['format_list'] = format_list

q = '''
{%-
set macs={
  'idrac_mac': '54:48:10:f4:87:0c',
  'integrated_nic_1_port_1_partition_1': 'E4:43:4B:00:D1:1C',
  'integrated_nic_1_port_2_partition_1': 'E4:43:4B:00:D1:1E',
  'integrated_nic_1_port_3_partition_1': 'E4:43:4B:00:D1:3C',
  'integrated_nic_1_port_4_partition_1': 'E4:43:4B:00:D1:3D'
}
-%}
{{ macs.keys() | map('replace', '(.*)', 'rabbitmq@\\1') | list }}
'''

tpl = env.from_string(q)
print(tpl.render())


def select_nics(list_, pattern):
    return [pattern % s for s in list_ if 'nic' in s]


env.filters['select_nics'] = select_nics

q = '''
{%-
set macs={
  'idrac_mac': '54:48:10:f4:87:0c',
  'integrated_nic_1_port_1_partition_1': 'E4:43:4B:00:D1:1C',
  'integrated_nic_1_port_2_partition_1': 'E4:43:4B:00:D1:1E',
  'integrated_nic_1_port_3_partition_1': 'E4:43:4B:00:D1:3C',
  'integrated_nic_1_port_4_partition_1': 'E4:43:4B:00:D1:3D'
}
-%}
{{ macs.keys() | format_list('rabbitmq@%s') }}
{{ macs.keys() | select_nics('%s') }}
'''

tpl = env.from_string(q)
print(tpl.render())

q = '''
{%-
set macs={
  'idrac_mac': '54:48:10:f4:87:0c',
  'integrated_nic_1_port_1_partition_1': 'E4:43:4B:00:D1:1C',
  'integrated_nic_1_port_2_partition_1': 'E4:43:4B:00:D1:1E',
  'integrated_nic_1_port_3_partition_1': 'E4:43:4B:00:D1:3C',
  'integrated_nic_1_port_4_partition_1': 'E4:43:4B:00:D1:3D'
}
-%}
{{ macs.keys() | select('in', '*nic*') | list }}
'''

tpl = env.from_string(q)
print(tpl.render())

q = '''
{%-
set macs={
  'idrac_mac': '54:48:10:f4:87:0c',
  'integrated_nic_1_port_1_partition_1': 'E4:43:4B:00:D1:1C',
  'integrated_nic_1_port_2_partition_1': 'E4:43:4B:00:D1:1E',
  'integrated_nic_1_port_3_partition_1': 'E4:43:4B:00:D1:3C',
  'integrated_nic_1_port_4_partition_1': 'E4:43:4B:00:D1:3D'
}
-%}
{{ macs.keys() | select('in', '*nic*') | list }}
'''

tpl = env.from_string(q)
print(tpl.render())
