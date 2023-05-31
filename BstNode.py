class User:
    def __init__(self,username,name,email):
        self.username = username
        self.name = name
        self.email = email

    def introduce(self,guest_name):
        print("Hello {}! Contact me at {} .".format(guest_name,self.email))



anand = User("anand","Anand Verma", "averma8@umd.edu")
bulbul = User("bulbul","Bulbul Verma", "bulbul@umd.edu")
champ = User("champ","Champ Steve", "champ@umd.edu")
Fin = User("fin","Fin Rogers", "Fin@umd.edu")
Siddharth = User("sidd","Siddharth Ajmera", "Siddharth@umd.edu")
tarun = User("tarun3","Tharun Reddy", "tarun@umd.edu")
vikas = User("vikky","Vikas Patidar", "vikas@umd.edu")


class BSTNode:
    def __init__(self,key,value=0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def inorder(self):
        if isinstance(self, BSTNode):
            BSTNode.inorder(self.left)
            print(self.key)
            BSTNode.inorder(self.right)

    def preorder(self):

        if isinstance(self, BSTNode):
            print(self.key)
            BSTNode.preorder(self.left)
            BSTNode.preorder(self.right)

    def postorder(self):
        if isinstance(self, BSTNode):
            BSTNode.postorder(self.left)
            BSTNode.postorder(self.right)
            print(self.key)
    def depthFirstSearch(root):
        arr = []
        res = []
        arr.append(root)

        while len(arr) > 0:
            current = arr.pop()

            res.append(current.key)

            if current.right is not None:

                arr.append(current.right)


            if current.left is not None:

                arr.append(current.left)


        return res
    def breadthFirstSearch(root):
        arr = res = []
        arr.append(root)
        while len(arr) > 0:
            current = arr.pop(0)

            res.append(current)
            if root.right is not None:
                arr.append(root.right)
            if root.left is not None:
                arr.append(root.left)
        return res

    def height(root):
        if root is None:
            return 0
        return 1 + max(BSTNode.height(root.left),BSTNode.height(root.right))

    def insert(root, key, value):
        if root is None:
            root = BSTNode(key, value)
        elif key < root.key:
            root.left = BSTNode.insert( root.left, key, value)
            root.left.parent = root
        elif key > root.key:
            root.right = BSTNode.insert( root.right, key, value)
            root.right.parent = root
        return  root

    def find(root,key):
        if root is None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            return BSTNode.find(root.left,key)
        if key > root.key:
            return BSTNode.find(root.right, key)

    def diameterOfBinaryTree(root) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is not None:
            return 1 + BSTNode.diameterOfBinaryTree( root.left) + BSTNode.diameterOfBinaryTree( root.right)
        elif root.left is None:
            return BSTNode.diameterOfBinaryTree( root.right)
        elif root.left is None:
            return BSTNode.diameterOfBinaryTree( root.left)
    def update(node, key, value):
        target = BSTNode.find(node, key)
        if target is not None:
            target.value = value

tree = BSTNode.insert(None, Fin.username, Fin)
BSTNode.insert(tree, bulbul.username, bulbul)
BSTNode.insert(tree, champ.username, champ)
BSTNode.insert(tree, tarun.username, tarun)
BSTNode.insert(tree, Siddharth.username, Siddharth)
BSTNode.insert(tree, vikas.username, vikas)
BSTNode.insert(tree, anand.username, anand)

# print(BSTNode.height(tree))
# print(BSTNode.find(tree,Siddharth.username).value)

# BSTNode.update(tree, 'anand', User('anandji','Anand verma', 'anandverma552@gmail.com'))

# n = tree.left.left.value
# print(n.username)

print(BSTNode.depthFirstSearch(tree))
print(BSTNode.diameterOfBinaryTree(tree))
BSTNode.preorder(tree)


