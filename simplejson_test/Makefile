# http://stackoverflow.com/questions/4859071/editing-existing-json-in-python
add_key_value:
	cat t2.json | python -m simplejson.tool >t2_1.json
	python t2_add_value_to_pre_existing.py
	-diff -uw t2_2.json t2_3.json

pretty:
	cat t2.json | python -m simplejson.tool

t:
	python t1.py

install:
	easy_install simplejson

clean:
	rm -f t2_?.json
