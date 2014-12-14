test:
	cat read_write.py | sed '/^\s*$$/d' | tr '\n' ';' >read_write_one_line.py
	cp puppet.conf.tmpl puppet.conf
	python read_write_one_line.py
	-diff -uw puppet.conf.tmpl puppet.conf
clean:
	rm -f puppet.conf
