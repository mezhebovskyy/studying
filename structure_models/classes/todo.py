from datetime import datetime
import fileinput

statuslistName = "statuslist.csv"
todofileName = "todolist.csv"

class ToDoItem:
    def __init__(self, id, description, status, createdon, updatedon):
        self.id = id
        self.description = description
        self.status = status
        self.createdon = createdon
        self.updatedon = updatedon

class ToDoList:
    def __init__(self):
        self.listofitems = []

    def appendItem(self, item):
        array = self.listofitems
        ID = len(array) + 1
        description = item
        status = "not_done"
        createdon = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updatedon = createdon
        self.listofitems.append(ToDoItem(ID, description, status, createdon, updatedon))

    def edit(self, number):
        for task in self.listofitems:
            if number == task.id:
                choice = raw_input("What do you want to change (description or status)?: ")
                if choice == "description":
                    new_description = raw_input("Type new description: ")
                    new_description = new_description.replace (" ", "_")
                    task.description = new_description
                if choice == "status":
                    new_status = raw_input("Type in new status (done or not done): ")
                    new_status = new_status.replace (" ", "_")
                    task.status = new_status
                task.updatedon = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def loadItems(self):
        reader = ToDoReader()
        self.listofitems = reader.ReadFromFile(todofileName, self.status)

    def show_my_items(self, status):
        print "\nHere is the list of %s things: " % status
        for task in self.listofitems:
            if task.status == status:
                print "%s, %s. Was created on: %s. Was last updated on: %s." % (task.id, task.description, task.createdon, task.updatedon)


class ToDoReader:
    def ReadFromFile(self, fileName, status):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            id, description, stat, createdon, updatedon = line.split(",")
            if status == stat:
                array.append(ToDoItem(id, description, status, createdon, updatedon))
        f.close()
        return array

def main():
    todolist = ToDoList()

    f = open(todofileName, "r")
    for line in f:
        line = line.replace('\n','')
        id, description, status, createdon, updatedon = line.split(",")
        item = ToDoItem(id, description, status, createdon, updatedon)
        todolist.listofitems.append(item)
    f.close()

    while(True):
        typeofaction = raw_input("What do you want to do with your list (add, edit, print, exit)? ")
        if typeofaction == "add":
            item = raw_input("Type the description: ")
            item = item.replace (" ", "_")
            todolist.appendItem(item)

        if typeofaction == "edit":
            for item in todolist.listofitems:
                print "%s,%s,%s,%s,%s" % (item.id, item.description, item.status, item.createdon, item.updatedon)
            number = raw_input("Type ID of the item you want to edit: ")
            todolist.edit(number)

        if typeofaction == "print":
            s = raw_input("Items of which status do you want to print (done, not done)?: ")
            s = s.replace (" ", "_")
            todolist.show_my_items(s)
            
        if typeofaction == "exit":
            open(todofileName, "w").close()
            f = open(todofileName, "a")
            for item in todolist.listofitems:
                linetoadd = "%s,%s,%s,%s,%s\n" % (item.id, item.description, item.status, item.createdon, item.updatedon)
                f.write(linetoadd)
            f.flush()
            f.close()
            break

if __name__ == "__main__":
    main()