#!/bin/bash
# Run all tests by class
./dev_install.sh
cd tests
python .\request_data.py
python -m unittest2
cd ..
