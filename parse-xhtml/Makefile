python=python

ifeq ($(OS),Windows_NT))
	python=cmd /c python
endif

summarize:
	$(python) summarize.py f.html

check:
	python check.py f.html
