#!/bin/bash

./twits/test.py | python -mjson.tool | cdl
