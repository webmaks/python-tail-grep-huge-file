#!/usr/bin/env python3

import re
import os
import sys
import fun

file = "file.log"


# Get last three lines from file 'sample.txt'
last_lines = fun.get_last_n_lines(file, 99)
print('Last N lines of File:')
# Iterate over the list of last 3 lines and print one by one
for line in last_lines:
    if re.search('xclip:amd64', line):
        print(line)


