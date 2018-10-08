# Run all tests by class
./dev_install.ps1
cd tests
python .\request_data.py
python -m unittest2
cd ..
