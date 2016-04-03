TIDY_ARGS  = -xml
TIDY_ARGS += --tidy-mark no
TIDY_ARGS += --doctype strict
TIDY_ARGS += --vertical-space false
TIDY_ARGS += --indent-attributes false
TIDY_ARGS += --wrap-attributes false
TIDY_ARGS += -wrap 60000
TIDY_ARGS += -q
TIDY_ARGS += -i
TIDY_ARGS += -c
TIDY_ARGS += -modify

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
	tidy $(TIDY_ARGS) *.xml
