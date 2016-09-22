tweetLength = 10
fileName = "tweetspile.txt"

def main():
    while True:
        sentence = raw_input("Make us happy with your new thoughts using Twitter: ")
        if sentence == ".":
            break
        if len(sentence) <= tweetLength:
            savetofile(sentence)
        if len(sentence) > tweetLength:
            tweetmass = [sentence[i:i+tweetLength] for i in range(0, len(sentence), tweetLength)]
            for i in tweetmass:
                savetofile(i)

def savetofile(lines):
    print "Now saving to file %r..." % fileName
    f = open(fileName, 'a')
    f.write(lines + '\n\n')
    f.close


if __name__== "__main__":
    main()

