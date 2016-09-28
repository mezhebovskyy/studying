
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

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node 
        else:
            temp_node = self.root
            while True:
                if int(new_node.data.hp) < int(temp_node.data.hp):
                    if temp_node.left == None:
                        print "inserting to the left"
                        temp_node.left = new_node 
                        break
                    if temp_node.left != None:
                        temp_node = temp_node.left
                if int(new_node.data.hp) >= int(temp_node.data.hp):
                    if temp_node.right == None:
                        print "inserting to the right"
                        temp_node.right = new_node
                        break
                    if temp_node.right != None:
                        temp_node = temp_node.right

    def delete(self, hp, model):
        return self.delete_rec(self.root, hp, model)

    def delete_rec(self, root, hp, model):
        if root == None:
            return None
        if hp < root.data.hp:
            root.left = self.delete_rec(root.left, hp, model)
        elif hp > root.data.hp:
            root.right = self.delete_rec(root.right, hp, model)
        elif root.left != None and root.right != None:
            root.data = self.minimum(root.right).data
            root.right = self.delete_rec(root.right, root.data.hp, root.data.mod)
        else:
            if root.left != None: 
                root = root.left
            else:
                root = root.right
        return root

    def minimum(self, root):
        if root.left == None:
            return root
        return self.minimum(root.left)


    def find(self, hp, model):
        temp_node = self.root
        while True:
            if temp_node.data.hp == hp and temp_node.data.mod == model:
                print True
                break
            if int(hp) < int(temp_node.data.hp):
                if temp_node.left != None:
                    temp_node = temp_node.left
                else:
                    print False
                    break
            elif int(hp) > int(temp_node.data.hp):
                if temp_node.right != None:
                    temp_node = temp_node.right
                else:
                    print False
                    break
            else:
                print False
                break




database = Tree()
database.insert(Car(125, "jetta"))
database.insert(Car(119, "jetta1"))
database.insert(Car(111, "jetta2"))
database.insert(Car(150, "jetta3"))
database.insert(Car(145, "jetta4"))
database.insert(Car(155, "jetta5"))
database.insert(Car(152, "jetta6"))
database.insert(Car(153, "jetta7"))

#database.delete(150, "jetta3")

database.find(160, "jetta5")
