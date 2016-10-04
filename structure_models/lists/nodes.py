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
        while temp != None:
            print temp.value
            temp = temp.next

    def checkifinlist(self, number):
        if self.head == None:
            return

        temp = self.head
        while temp != None:
            if temp.value == number:
                return True
                
            temp = temp.next
        return False
    
    def indexof(self, number):
        if self.head == None:
            return False
        
        temp = self.head
        index = -1

        while temp != None:
            index = index + 1
            if temp.value == number:
                return index
            temp = temp.next
        return False

    def insert(self, i, number):
        if self.head == None:
            return
        temp = self.head
        node = Node(number)
        index = -1
          
        while temp != None:
            #if i == 0:
                #temp = node.next
                #node = temp
            index = index + 1
            if index == i-1 :
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next

    def remove(self, i):
        if self.head == None:
            return
        if i == 0:
            self.head = self.head.next
            return
        index = -1
        temp = self.head
        while temp != None:
            index = index + 1
            if index == i-1:
                temp.next = temp.next.next
                return
            temp = temp.next

linkedList = List()
while True:
    num = raw_input("Please enter the number: ")
    if(num == '.'):
        break
    linkedList.append(int(num))


# numtoinsert = raw_input("What number do you want to insert?: ")
# indexofnumber = raw_input("On what index do you want to insert a number?: ")
# linkedList.insert(int(indexofnumber), int(numtoinsert))
# linkedList.printList()

# numtofind = raw_input("What number do you want to find?: ")
# print linkedList.indexof(int(numtofind))

# num = raw_input("What number do you want to check?: ")
# print linkedList.checkifinlist(int(num))

# indtoremove = raw_input("What index in the list do you want to remove?: ")
# linkedList.remove(int(indtoremove))
# linkedList.printList()