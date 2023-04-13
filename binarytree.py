class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left),TreeNode.height((self.right)))

    def inorder(self):
        if isinstance(self, TreeNode):
            TreeNode.inorder(self.left)
            print(self.key)
            TreeNode.inorder(self.right)


    def preorder(self):
        if isinstance(self, TreeNode):
            print(self.key)
            TreeNode.preorder(self.left)
            TreeNode.preorder(self.right)

    def postorder(self):
        if isinstance(self, TreeNode):
            TreeNode.postorder(self.left)
            TreeNode.postorder(self.right)
            print(self.key)

    def remove_none(self, nums):
         return [x for x in nums if x is not None]

    def is_bst(self, root):
        if root is None:
            return True, None, None
        is_bst_l, min_l, max_l = self.is_bst(root.left)
        is_bst_r, min_r , max_r = self.is_bst(root.right)

        is_bst_node = (is_bst_l and is_bst_r and (max_l is None or root.key > max_l) and (min_r is None or root.key < min_r))

        min_key = min(self.remove_none([min_l, root.key, min_r]))
        max_key = max(self.remove_none([max_l, root.key, max_r]))
        return is_bst_node, min_key, max_key



tree_tuple = (("Aakash","Biraj","Hemanth"),"Jadhesh",("Siddhath","Sonaksh","Vishal"))

def parse_tuple(data):
    # print(data)
    if(isinstance(data,tuple) and len(data)==3):
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree = parse_tuple(tree_tuple)
print(tree.is_bst(tree))

# tree.inorder()





# def parse_tree(tree):
#     if isinstance(tree, TreeNode):
#
#         if tree.left is None and tree.right is None:
#             return tree.key
#         return (
#             parse_tree(tree.left),
#             tree.key,
#             parse_tree(tree.right)
#         )
#
# print(parse_tree(tree))