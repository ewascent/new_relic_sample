# install dev only libraries for linbting, building, and testing
python -m pip install --user --upgrade setuptools wheel
pip install nose pylint coverage unittest2 junit2html nosetests-json-extended urllib3
nosetests --plugins
