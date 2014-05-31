TIDY_SW =
TIDY_SW += --force-output true
TIDY_SW += --tidy-mark no
TIDY_SW += --doctype strict
TIDY_SW += -indent
TIDY_SW += -xml
TIDY_SW += -quiet
TIDY_SW += -wrap 99999999
TIDY_SW += -f $@.err

date=$(shell sh -c date +"%Y-%m-%d %H:%M:%S" | tr ' ' '-')

trand: test_rand
test_rand: default.xml
	python t.py -f default.xml --rand

tr: test_remove
test_remove: proj='7z_practice'
test_remove: default.xml
	python t.py -f default.xml --remove $(proj)
	-diff -uw default.xml.prestine default.xml

tni: test_no_inputfile
test_no_inputfile: proj='7z_practice'
test_no_inputfile: default.xml
	python t.py --remove $(proj)
	-diff -uw default.xml.prestine default.xml

ta: test_add
test_add: proj=proj_$(date)
test_add: default.xml
	python t.py -f default.xml --add $(proj)
	-diff -uw default.xml.prestine default.xml

tad: test_add_duplicate
test_add_duplicate: proj='wedu-control'
test_add_duplicate: default.xml
	python t.py -f default.xml --add $(proj)
	-diff -uw default.xml.prestine default.xml

default.xml: template.xml
	tidy $(TIDY_SW) -output $@ $^
	cp $@ $@.prestine

clean:
	rm -f default.xml.err
	rm -f default.xml
	rm -f default.xml.prestine
