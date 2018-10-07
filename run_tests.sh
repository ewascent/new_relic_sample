#!/bin/bash
# Run all tests by class
cd tests
python .\request_data.py
python -m unittest2
cd ..
