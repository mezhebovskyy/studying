f = open("test.txt")
content = f.read()
f.close()

words = content.split()
print "There are %s words in the file." % format(len(words))


