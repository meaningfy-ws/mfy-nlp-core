SHELL=/bin/bash -o pipefail
BUILD_PRINT = STEP: 


#-----------------------------------------------------------------------------
# PIP Install commands
#-----------------------------------------------------------------------------

install:
	@ echo "$(BUILD_PRINT)Installing the requirements"
	@ pip install --upgrade pip
	@ python setup.py install


#-----------------------------------------------------------------------------
# Testing commands
#-----------------------------------------------------------------------------

test:
	@ echo "$(BUILD_PRINT)Running the unit tests"
	@ py.test -s --html=report.html --self-contained-html

