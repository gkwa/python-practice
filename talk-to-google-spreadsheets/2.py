import json
import gspread
import pandas
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('/Users/demo/Downloads/testpython-f07fef62f83b.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)
wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1GAMM-9MEPWkustx3HD7uh6tYvNIy3B5rlDUEafir4BU/edit#gid=0").sheet1

df = pandas.DataFrame(wks.get_all_records())
pandas.set_option('display.line_width', 200)
# print(df['MAC -EHERNET'])
print(df['SERIAL'])


# This is what UI does seen from mysql.log
"""
INSERT INTO device ( device, token, ip, port, user_id, is_active, dt_update, jsdata ) VALUES( 'taylor-E15090103.7D','E15090103.7D','200.89.80.94','','1','1','2015-10-17 15:08:09','[]')
SELECT drm_id FROM drm WHERE ( is_active = '1' )  AND (( drm = '' ) ) -- evaluates to 115473
UPDATE tag SET is_active = ''  WHERE is_active = '1'  AND  tag_type = 'device.drm_id'  AND  node_id = '4703'
INSERT INTO tag ( tag, tag_type, node_id, user_id, is_active ) VALUES( '115473','device.drm_id','4703','1','1' )
"""

USER_ID=1 # give these units to systemadmin 'admin'
IS_ACTIVE=1

for serial in df['SERIAL'].values:
    device_name = 'Micro %s'%serial
    # INSERT INTO device ( device, token, ip, port, user_id, is_active, dt_update, jsdata ) VALUES( 'taylor-E15090103.7D','E15090103.7D','200.89.80.94','','1','1','2015-10-17 15:08:09','[]')
    here="""
SET @drmid=(SELECT drm_id FROM drm WHERE ( is_active = '{is_active}' )  AND (( drm = '' ) )); -- this is streambox system admin
INSERT INTO device ( device, token, ip, port, user_id, is_active, dt_update, jsdata ) VALUES ( '{device}', '{token}', '{ip}', '{port}', '{user_id}', '{is_active}', '{dt_update}', '{jsdata}');
SET @node_id = LAST_INSERT_ID();
UPDATE tag SET is_active = ''  WHERE is_active = '1'  AND  tag_type = 'device.drm_id'  AND  node_id = @node_id;
INSERT INTO tag ( tag, tag_type, node_id, user_id, is_active ) VALUES( {tag},'{tag_type}',{node_id},'{user_id}','{is_active}' );
""".format(
    device='Micro %s'%serial,
    token=serial,
    ip='127.0.0.1',
    port='',
    user_id=USER_ID,
    is_active=IS_ACTIVE,
    dt_update='NOW()',
    jsdata='[]',
    tag='@drmid',
    tag_type='device.drm_id',
    node_id='@node_id',
);
    print(here)
