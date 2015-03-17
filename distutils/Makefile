isolated_dir:=tmp_$(shell date +%Y-%m-%d-%s)
uname_s:=$(shell sh -c 'uname -s')
SUDO=

ifeq (Darwin,$(uname_s))
	SUDO=sudo
endif

bdist_wininst:
	python setup.py bdist_wininst

sdist:
	python setup.py sdist

test:
	$(MAKE) install
	mkdir -p $(isolated_dir) && cp test_foo.py $(isolated_dir) && cd $(isolated_dir) && python test_foo.py

install:
	$(SUDO) python setup.py install
	$(SUDO) chmod -R 777 build

help:
	python setup.py bdist --help-formats

clean:
	rm -f *.pyc
	rm -rf build
	rm -rf dist
	rm -f MANIFEST
	rm -rf tmp_*-*-*
