#!/usr/bin/env python
import sys
for line in sys.stdin:
	line=line.strip()
	columns=line.split(',')
	print "%s\t%s" % (columns[8],'1')