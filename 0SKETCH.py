def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()





def bread(func):
    def wrapper():
        print "</------\>"
        func()
        print "<\______/>"
    return wrapper
 
def ingredients(func):
    def wrapper():
        print "#помидоры#"
        func()
        print "~салат~"
    return wrapper

@bread
@ingredients
def sandwich(food="--ветчина--"):
    print food

# sandwich()

# sandwich = bread(ingredients(sandwich))
# sandwich()
