================

new_relic_sample

================

Takes in one or more file paths. Use a sliding window to split the text into triples.
A sliding window takes the sentence "one two three four five" and produces "one two three", "two three four", "three four five".
It returns the ranked values.

================

Description

================

First run the 
```run_tests.sh``` 
or
```run_tests.ps1```

This will install all dependencies and will create two files from project Gutengurg.
If you have proxy issues there is a fallback data generator, but it is anemic.
The files are generated to keep the git clone small.

Next run the package.
```
python src/__main__.py .\tests\data\some_words.txt .\tests\data\more_words.txt
```
================

Note

================

This project has been set up using PyScaffold 3.1. There is some unused boiler plate floating around.
