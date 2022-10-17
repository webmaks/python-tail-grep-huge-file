#!/usr/bin/env python3

import re

file = "file.log"

with open(file) as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        if re.search('base-files_12ubuntu4_amd64.deb', data):
            print(data)





