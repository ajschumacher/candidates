#!/usr/bin/env python

import sys
import csv

r = csv.reader(sys.stdin, delimiter='|')
w = csv.writer(sys.stdout)
for line in r:
    w.writerow(line)
