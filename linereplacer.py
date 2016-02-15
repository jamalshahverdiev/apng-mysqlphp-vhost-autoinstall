#!/bin/env python

replacements = {'saytdb':'yenidb', 'saytuser':'yeniuser', 'freebsd':'yenipass'}
inputfile = '/root/apache-ng-project/tempindex.php'
outputfile = '/root/apache-ng-project/newindex.php'
with open('/root/apache-ng-project/newindex.php', 'w') as outfile:
	with open('/root/apache-ng-project/tempindex.php', 'r') as infile:
		for line in infile:
			for src, target in replacements.iteritems():
				line = line.replace(src, target)
			outfile.write(line)
