update_key_value:
	cat Windows_Roles_And_Features.template | python -m simplejson.tool >t3_1.json
	python t3_update_key_value.py
	-diff -uw t3_2.json t3_3.json

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
	rm -f t?_?.json
