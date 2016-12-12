#!/bin/sh

# Copyright(c) Gordon Elliott 2016

echo Top 10 from sample.txt
/usr/bin/python3 ./src/challenge/top_n.py 10 int sample.txt

echo Unittests
PYTHONPATH=./src:. /usr/bin/python3 -m unittest discover src/tests/challenge

echo Performance profiling
PYTHONPATH=./src:. /usr/bin/python3 ./src/tests/challenge/performance_test.py
