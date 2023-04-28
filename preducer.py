from operator import itemgetter
import sys
current_word=None
current_count=0
municipal=None
for line in sys.stdin:
	line=line.strip()
	municipal,count=line.split('\t',1)
	count=int(count)
	if current_word==municipal:
		current_count+=count
	else:
		if current_word:
			print "%s\t%s"% (current_word,current_count)
		current_count=count
		current_word=municipal
if current_word==municipal:
	print "%s\t%s" % (current_word,current_count)