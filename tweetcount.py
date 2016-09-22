tweetLength = 10
fileName = "tweetspile.txt"

def main():
    while True:
        sentence = raw_input("Make us happy with your new thoughts using Twitter: ")
        if sentence == ".":
            break 
        elif len(sentence) > tweetLength:
            print "\n\t\t\t\tSorry!:(\n\nA tweet should be less or equal %s symbols. At now you have %s symbols.\n" % (tweetLength, len(sentence))
            continue
        savetofile(sentence)
        

def savetofile(sentence):
    print "Now saving to file %r" % fileName
    f = open(fileName, 'a')
    f.write(sentence + '\n')
    f.close


if __name__== "__main__":
    main()

