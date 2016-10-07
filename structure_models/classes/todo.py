from datetime import datetime
import fileinput

statuslistName = "statuslist.csv"
todofileName = "todolist.csv"

class toDoItem:
    def __init__(self, id, description, status, createdon, updatedon):
        self.id = id
        self.description = description
        self.status = status
        self.createdon = createdon
        self.updatedon = updatedon

class Status:
    def __init__(self, status):
        self.status = status
        self.listofitems = []

    def loadItems(self):
        reader = toDoReader()
        self.listofitems = reader.ReadFromFile(todofileName, self.status)

    def show_my_items(self):
        print "\nHere is the list of %s things: " % self.status
        for task in self.listofitems:
            print "%s, %s. Was created on: %s. Was last updated on: %s." % (task.id, task.description, task.createdon, task.updatedon)

class toDoAppend:
    def appendItem(self, item, filename):
        f = open(filename, "a")
        num_lines = sum(1 for line in open(filename) if line.rstrip())
        line = num_lines + 1
        description = item
        status = "Not_Done"
        createdon = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updatedon = createdon
        lineToAddIntoFile = "%s,%s,%s,%s,%s" % (line, description, status, createdon, updatedon)
        f.write(lineToAddIntoFile + '\n')
        f.flush()
        f.close()

class itemEditor:
    def edit(self, id, filename):
        f = open(filename, "a")
        old = raw_input("What phrase do you want to change?: ")
        new = raw_input("What do you want to put instead?: ")
        for line in fileinput.FileInput(filename, inplace=1):
            if line.startswith(id):
                line = line.replace(old, new)
                print line
        f.flush()
        f.close()
        
        
        # num_lines = sum(1 for line in open(filename) if line.rstrip())
        # line = num_lines + 1
        # description = item
        # status = "Not_Done"
        # createdon = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # updatedon = createdon
        # lineToAddIntoFile = "%s,%s,%s,%s,%s" % (line, description, status, createdon, updatedon)
        # f.write(lineToAddIntoFile + '\n')
        # f.flush()
        # f.close()


class toDoReader:
    def ReadFromFile(self, fileName, status):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            id, description, stat, createdon, updatedon = line.split(",")
            if status == stat:
                array.append(toDoItem(id, description, status, createdon, updatedon))
        f.close()
        return array

class StatusReader:
    def ReadFromFile(self, fileName):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            status = line
            array.append(Status(status))
        f.close()
        return array


def main():
    typeofaction = raw_input("What do you want to do with your list (add, edit, print)? ")
    if typeofaction == "add":
        item = raw_input("Type the description: ")
        item = item.replace (" ", "_")
        toDoAppend().appendItem(item, todofileName)
    
    if typeofaction == "edit":
        f = open(todofileName, "r")
        for line in f:
            print line
        id = raw_input("Type ID of the item you want to edit: ")
        f.close()
        itemEditor().edit(id, todofileName)




    if typeofaction == "print":
        statusReader = StatusReader()
        todolist = statusReader.ReadFromFile(statuslistName)
        
        for item in todolist:
            item.loadItems()

        for item in todolist:
            item.show_my_items()

if __name__ == "__main__":
    main()





# >>> from time import gmtime, strftime
# >>> strftime("%Y-%m-%d %H:%M:%S", gmtime())
# '2009-01-05 22:14:39'

# >>> from datetime import datetime
# >>> datetime.now().strftime('%Y-%m-%d %H:%M:%S')