# set up the environment
setup: _packages_installed

# create a source distribution
sdist:
	python3 setup.py sdist

# create a binary distribution
dist: bdist
bdist:
	python3 setup.py bdist_egg

# clean up
clean:
	rm -rf build dist pymongo_driver.egg-info
	find . -name '*.pyc' -delete

# run tests
test: pep8 unittest
pep8:
	pep8 --max-line-length=120 --show-source --show-pep8 --statistics --verbose 'pymongo_driver'
unittest:
	cd tests \
	&& PYTHONPATH=$$(dirname $$(pwd)):$$(pwd) python3 driver_test_case.py -v

# install requirements
_packages_installed: requirements.txt
	pip3 install --upgrade pip setuptools
	pip3 install -r requirements.txt
