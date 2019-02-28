from jinja2 import Template

q = '''
{%- set arr=['E4:43:4B:00:D1:1C', 'E4:43:4B:00:D1:1E', 'E4:43:4B:00:D1:3C','E4:43:4B:00:D1:3D'] -%}
{%- set comma = joiner("||") -%}
{%- for mac in arr -%}
 {{ comma() -}}
 {{ 'bootp.hw.mac_addr==%s' | format(mac) | lower }}
{%- endfor -%}
'''

print(Template(q).render())

q = '''
{%- set macs=['E4:43:4B:00:D1:1C', 'E4:43:4B:00:D1:1E', 'E4:43:4B:00:D1:3C','E4:43:4B:00:D1:3D'] -%}
{%- for mac in macs -%}
{{ 'bootp.hw.mac_addr==%s' | format(mac) | lower -}}
{{ '||' if not loop.last }}
{%- endfor -%}
'''

print(Template(q).render())

q = '''
{%- set macs=['E4:43:4B:00:D1:1C', 'E4:43:4B:00:D1:1E', 'E4:43:4B:00:D1:3C','E4:43:4B:00:D1:3D'] -%}
bootp.option.value==2 && ({%- for mac in macs -%}
{{ 'bootp.hw.mac_addr==%s' | format(mac) | lower -}}
{{ '||' if not loop.last }}
{%- endfor -%})
'''

print(Template(q).render())

"""
https://stackoverflow.com/questions/33685233/using-regex-in-jinja
https://groups.google.com/forum/#!topic/pocoo-libs/3yZl8vHJ9fI
https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/
http://jinja.octoprint.org/extensions.html
"""

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
{%- set arr = []  -%}
{% for key, value in macs.items() -%}
{%- if 'nic' in key or 'idrac_mac' in key or 'host.bond0Hostname'==key -%}
{{ arr.append(value) }}
{%- endif -%}
{%- endfor -%}

{{arr|join(',')}}
'''

print(Template(q).render())

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
{{ macs.keys() | list }}
'''

print(Template(q).render())

q = '''
{%- set arr=['E4:43:4B:00:D1:1C', 'E4:43:4B:00:D1:1E', 'E4:43:4B:00:D1:3C','E4:43:4B:00:D1:3D'] -%}
{%- set comma = joiner("||") -%}
{%- for mac in arr -%}
 {{ comma() -}}
 {{ 'bootp.hw.mac_addr==%s' | format(mac) | lower }}
{%- endfor -%}
'''

print(Template(q).render())

dct = {
    'serial': 'AAAAAAA',
    'idrac_mac': '54:48:10:f4:87:0c',
    'pumpkins': '54:48:10:f4:87:0c',
    'integrated_nic_1_port_1_partition_1': 'E4:43:4B:00:D1:1C',
    'integrated_nic_1_port_2_partition_1': 'E4:43:4B:00:D1:1E',
    'integrated_nic_1_port_3_partition_1': 'E4:43:4B:00:D1:3C',
    'integrated_nic_1_port_4_partition_1': 'E4:43:4B:00:D1:3D'
}

q = '''{#- jinja -#}
rm -f /tmp/$(hostname -s)_for_{{ host.serial }}_$(date +%s).pcap
# tcpdump for 10 minutes
tcpdump -G $((10*60)) -W 1 -w /tmp/$(hostname -s)_for_{{ host.serial }}_$(date +%s).pcap -i any 'net 172.18.53.0/24 and (port bootps or port bootpc)'
ls -tr /tmp/*_for_{{ host.serial }}*.pcap | tail -1 | xargs -r -I{} echo \# tshark -2 -r {} -R 'bootp.option.value==2 && (
 {%- set comma = joiner(' || ') -%}
 {%- for key, value in host.items() -%}
  {%- if 'nic' in key or 'idrac_mac' in key or 'host.bond0Hostname'==key -%}
  {{ comma() -}}
  {{ 'bootp.hw.mac_addr==%s' | format(value) | lower -}}
 {%- endif -%}
 {%- endfor -%}
)' -T fields -e ip.src -e bootp.ip.server -e bootp.option.hostname 2>/dev/null
'''

print(Template(q).render(host=dct))
