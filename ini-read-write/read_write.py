import ConfigParser

conf="puppet.conf"

c=ConfigParser.ConfigParser()
c.read(conf)

c.has_option("main","manifest") and c.remove_option("main","manifest")
c.set("main","certificate_revocation","false")
c.set("main","server","docker.streambox.com")
c.set("main","certname","docker.streambox.com")

cfgfile=open(conf, "wb")
c.write(cfgfile)
cfgfile.close()
