print ('Hello World')

#get name of file and open
name= input('Enter file:')
handle= open(name, 'r')

# count word frequency with a histogram
counts=dict()
for line in handle:
	words=line.split()
	for word in words:
		counds[word]=counts.get(word,0)+1

# Find most common word
bigcount=None
bigword=None
for word, count in list(counts.items(()):
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count

print(bigword, bigcount)

#code http://www.py4e.com/code3/words.py
