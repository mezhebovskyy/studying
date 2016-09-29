class CustomError(Exception):
    def __init__(self, value, url):
        self.value = value
        self.url = url
    def __str__(self):
        return "This is some custom exception with value: %s\r\n You can read more about the error here: %s"  % (self.value, self.url)
        
try:
    while(True):
        sometext = raw_input("Please type some shit: ")
        if(sometext == "blyat"):
            raise CustomError("Bad word error!", "https://docs.python.org/2/library/exceptions.html")
        elif(sometext == "exit"):
            print "Going out..."
            break
        else:
            print "Good boy!"
except CustomError as someException:
    print str(someException)