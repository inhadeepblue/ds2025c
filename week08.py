class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = 'hs'

node2 = TreeNode()
node2.data = 'sl'
node1.left = node2

node3 = TreeNode()
node3.data = 'mb'
node1.right = node3

node4 = TreeNode()
node4.data = 'hw'
node2.left = node4

node5 = TreeNode()
node5.data = 'zz'
node2.right = node5

node6 = TreeNode()
node6.data = 'sm'
node3.left = node6

print(node5.data)
print(node1.left.right.data)