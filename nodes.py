class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def append(self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
    
    def printList(self):
        temp = self.head
        while temp.next != None:
            print temp.value
            temp = temp.next

    def checkifinlist(self, number):
        if self.head == None:
            return False

        temp = self.head
        while temp.next != None:
            if temp.value == number:
                return True
                
            temp = temp.next
        return False
    
    def indexof(self, number):
        if self.head == None:
            return False
        
        index = -1
        while temp.next != None:
            if temp.value != numtofind:
                index = index + 1
            if temp.value == number:
                print "It has a %s index." % index
        
        return index = -1
        


linkedList = List()
while True:
    num = raw_input("Please enter the number: ")
    if(num == '.'):
        break
    linkedList.append(int(num))


numtofind = raw_input("What number do you want to find?: ")
#как обратиться к методу indexof отсюда?




#num = raw_input("What number do you want to check?: ")
#print linkedList.checkifinlist(int(num)) 
        
    
