#!/usr/bin/env python

# Spartan, extendable static analyzer for JavaScript. Runs in Python 3+.
# Started writing during a class to demo SAST.

import argparse
import re
import os

# Run this script from the root of the directory structure 
# containing the files needing scanning. This lists all files 
# below the current directory, most of which should be text
# in a software project.
path = '.'
files = []
for r, d, f in os.walk(path):
	for file in f:
		if ((file.find('.') > 0) and (file.find('check.py') == -1)):
			files.append(os.path.join(r, file))

# Print header for output list
print("Type\tFile\tLine number\tItem")

# Iterate through all files added to list
for infile in files:
	#print("Scanning " + infile)
	f = open(infile, "r")
	linecount = 0
	for line in f:s
		linecount+=1

		# Augment following sections (or add new ones) for other risks.

		# Scan for likely IPv4 addresses
		s = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
		if len(s) > 0:
			for address in s:
				print("IP addr\t" + f.name + "\t" + str(linecount) + "\t" + address)

		# Scan for instances of "TODO" for debug code
		if ('TODO' in line):
			print("TODO\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# Scan for instances of "exec" for debug code
		if ('exec' in line):
			print("exec\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# Scan for console.debug calls
		if ('console.debug' in line):
			print("console.debug\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# Scan for console.warn calls
		if ('console.warn' in line):
			print("console.warn\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# Scan for console.info calls
		if ('console.info' in line):
			print("console.info\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# Scan for console.error calls
		if ('console.error' in line):
			print("console.error\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# Scan for console.log calls
		if ('console.log' in line):
			print("console.log\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# Scan for comments for debug code or some other fun
		if (('//' in line) \
			or ('/*' in line) \
			or ('<!--' in line)):
			print("Comments\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# Scan for test / debug variables
		if (('test' in line) \
			or (('debug' in line) and not ('console.debug')) \
			or ('temp' in line)):
			print("Test vars\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# Scan for questionable code
		if ('stackoverflow' in line.lower()):
			print("StackOverflow\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# Scan for profanities (expand as needed)
		if (('fuck' in line.lower()) \
			or ('shit' in line.lower()) \
			or ('crap' in line.lower()) \
			or ('damn' in line.lower()) \
			or ('bugger' in line.lower())):
			print("Comments\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

f.close()


