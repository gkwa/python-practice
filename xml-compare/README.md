Use Python Pandas data frames to compare xml.
============================================
* http://pandas.pydata.org/

* 

```sh
lip | grep Live | grep -viE 'liveni|livedb' | awk '{print $1}' >servers
pslurp --timeout=60 --hosts servers --localdir s /c/sls_db/SLSServer.xml .
find s -type f | while IFS=/ read -r d server file; do echo $server: $d/$server/$file; done >list.yml
make df
```