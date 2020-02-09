#!/usr/bin/env python

# Spartan static analyzer for JavaScript. Runs in Python 3+.
# Started writing during a class I taught to demo SAST ca. 2015.

import argparse
import re
import os

path = '.'
files = []
for r, d, f in os.walk(path):
	for file in f:
		if ((file.find('.') > 0) and (file.find('check.py') == -1)):
			files.append(os.path.join(r, file))

print("Type\tFile\tLine number\tItem")
for infile in files:
	#print("Scanning " + infile)
	f = open(infile, "r")
	linecount = 0
	for line in f:
		linecount+=1

		# find likely IPv4 addresses
		s = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
		if len(s) > 0:
			for address in s:
				print("IP addr\t" + f.name + "\t" + str(linecount) + "\t" + address)

		# find instances of "TODO" for debug code
		if ('TODO' in line):
			print("TODO\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# find instances of "exec" for debug code
		if ('exec' in line):
			print("exec\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# find console.debug calls
		if ('console.debug' in line):
			print("console.debug\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# find console.warn calls
		if ('console.warn' in line):
			print("console.warn\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# find console.info calls
		if ('console.info' in line):
			print("console.info\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# find console.error calls
		if ('console.error' in line):
			print("console.error\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])
		# find console.log calls
		if ('console.log' in line):
			print("console.log\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# find comments for debug code or some other fun
		if (('//' in line) \
			or ('/*' in line) \
			or ('<!--' in line)):
			print("Comments\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# find test / debug variables
		if (('test' in line) \
			or (('debug' in line) and not ('console.debug')) \
			or ('temp' in line)):
			print("Test vars\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# find questionable code
		if ('stackoverflow' in line.lower()):
			print("StackOverflow\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

		# find profanities (expand as needed)
		if (('fuck' in line.lower()) \
			or ('shit' in line.lower()) \
			or ('crap' in line.lower()) \
			or ('damn' in line.lower()) \
			or ('bugger' in line.lower())):
			print("Comments\t" + f.name + "\t" + str(linecount) + "\t" + line[:-1])

f.close()


