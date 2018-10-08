#!/bin/bash
# Run all tests by class
./dev_install.sh
cd src
pylint -rn error.py
pylint -rn filer.py
pylint -rn utilities.py
pylint -rn __init__.py
pylint -rn __main__.py
cd ../tests
python .\request_data.py
python -m unittest2
cd ..
