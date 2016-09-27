
class Car:
    def __init__(self, hp, mod):
        self.hp = hp
        self.mod = mod

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, mashina):
        new_node = Node(mashina)
        if self.root == None:
            self.root = new_node 
        else:
            temp_node = self.root
            while True:
                if int(new_node.mashina.hp) < int(temp_node.mashina.hp):
                    if temp_node.left == None:
                        new_node = temp_node.left
                    if temp_node.left != None:
                        temp_node = temp_node.left
                    new_node = temp_node.left
                if int(new_node.mashina.hp) >= int(temp_node.mashina.hp):
                    if temp_node.right == None:
                        new_node = temp_node.right
                    if temp_node.right != None:
                        temp_node = temp_node.right
                    new_node = temp_node.right

    def delete(self, x, y):
        temp_node = self.root
        if temp_node.car.hp == x:
            if temp_node.car.mod == y:
                temp_node.left == temp.node
        else:        
            if temp_node.left.car.hp == x:
                if temp_node.left.car.mod == y:
                    temp_node = temp_node.left
                else:
                    return
            if temp_node.right.car.hp == x:
                if temp_node.right.car.mod == y:
                    temp_node = temp_node.right
                else:
                    return
            else: 
                if int(x) < int(temp_node.right.car.hp):
                    if temp_node.left != None:
                        temp_node = temp_node.left
                    else:
                        return False
                if int(x) > int(temp_node.right.car.hp):
                    if temp_node.left != None:
                        temp_node = temp_node.right
                    else:
                        return False

    def find(self, x, y):
        temp_node = self.root
        if temp_node.car.hp == x:
            if temp_node.car.mod == y:
                return True
            return
        else:        
            if temp_node.left.car.hp == x:
                if temp_node.left.car.mod == y:
                    return True
                else:
                    return
            if temp_node.right.car.hp == x:
                if temp_node.right.car.mod == y:
                    return True
                else:
                    return
            else: 
                if int(x) < int(temp_node.right.car.hp):
                    if temp_node.left != None:
                        temp_node = temp_node.left
                    else:
                        return False
                if int(x) > int(temp_node.right.car.hp):
                    if temp_node.left != None:
                        temp_node = temp_node.right
                    else:
                        return False




database = Tree()
database.insert(Car(125, "jetta"))

database = Tree()
database.delete(Car(125, "jetta"))

database = Tree()
database.find(Car(125, "jetta"))