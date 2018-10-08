# Run all tests by class
.\dev_install.ps1
cd src
pylint -rn error.py
pylint -rn filer.py
pylint -rn utilities.py
pylint -rn __init__.py
pylint -rn __main__.py
cd ..\tests
python .\request_data.py
python -m unittest2
cd ..
