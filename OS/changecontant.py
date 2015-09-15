#!/usr/bin/python

import fileinput
for line in fileinput.FileInput("test.txt",inplace=1):
   line = line.replace("kasun","ttttt")
   print line


