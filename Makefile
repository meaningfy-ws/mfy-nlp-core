SHELL=/bin/bash -o pipefail
BUILD_PRINT = STEP: 


#-----------------------------------------------------------------------------
# PIP Install commands
#-----------------------------------------------------------------------------

install-spacy-model:
	@ echo "$(BUILD_PRINT)Installing the spacy model"
	@ pip install 'en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.2.0/en_core_web_md-3.2.0-py3-none-any.whl'

install-prod: install-spacy-model
	@ echo "$(BUILD_PRINT)Installing the prod requirements"
	@ pip install -r requirements/requirements-prod.txt

install-dev: install-test
	@ echo "$(BUILD_PRINT)Installing the dev requirements"
	@ pip install --upgrade pip
	@ pip install -r requirements/requirements-dev.txt

install-test: install-prod
	@ echo "$(BUILD_PRINT)Installing the test requirements"
	@ pip install -r requirements/requirements-test.txt

create-lock:
	@ echo "$(BUILD_PRINT)Create the lock requirements"
	@ pip install --upgrade pip
	@ pip freeze > tmp_pip_state_before_create_lock.txt
	@ pip uninstall -r tmp_pip_state_before_create_lock.txt -y
	@ pip install -r requirements/requirements-prod.txt
	@ pip freeze > requirements/requirements-lock.txt
	@ pip uninstall -r requirements/requirements-lock.txt -y
	@ pip install -r tmp_pip_state_before_create_lock.txt
	@ rm tmp_pip_state_before_create_lock.txt



#-----------------------------------------------------------------------------
# Testing commands
#-----------------------------------------------------------------------------

test:
	@ echo "$(BUILD_PRINT)Running the unit tests"
	@ py.test -s --html=report.html --self-contained-html

