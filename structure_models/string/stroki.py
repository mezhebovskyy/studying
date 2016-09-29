words = raw_input("Type something: ")
wordsmass = words.split(" ")

max = 0
maxword = ""
for word in wordsmass:
    if len(word) > max:
        max = len(word)
        maxword = word

print maxword      
        
       




