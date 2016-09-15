words = raw_input("Type something: ")
wordsmass = words.split(" ")
len = len(wordsmass)
for word in range(0,len):
    if len(wordsmass(word)) > len(wordsmass(word+1)):
        wordsmass[word], wordsmass[word+1] = wordsmass[word+1], wordsmass[word]
