def bubblesort(l):
    for i in range(0,len(l)):
        for j in range(len(l)-1,i,-1):
            if len(l[j])<len(l[j-1]):
                l[j], l[j-1] = l[j-1], l[j]


def slovo(k):
    max = 0
    maxword = ""
    for word in k:
        if len(word) > max:
            max = len(word)
            maxword = word
    return maxword

words = raw_input("Type something: ")
wordsmass = words.split(" ")

bubblesort(wordsmass)

print wordsmass
print slovo(wordsmass)