df:
	python data_frame.py

hide:
	for xmlfile in *.xml ; do \
	python hide_secrets.py --file $$xmlfile ; \
	done

hst: hide_secrets_test
hide_secrets_test:
	python hide_secrets.py --file slsserver_autogen_LiveAU.xml

tidy:
	tidy -xml --tidy-mark no --doctype strict --vertical-space false --indent-attributes false --wrap-attributes false -wrap 60000 -q -i -c -modify *.xml
