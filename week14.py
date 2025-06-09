import sys
#sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(node, key):  # 재귀 -> 반복
  new_node = TreeNode(key)
  if root is None:
    return new_node

  current = root
  while True:
    if key < current.val:  # 현재 노드 보다 새 노드 값이 작으면
      if current.left is None:  # 현재 노드의 왼쪽이 비어있으면
        current.left = new_node
        break
      current = current.left  # 왼쪽 노드로 current 변경 (이동)
    else:  # 현재 노드 보다 새 노드 값이 크면
      if current.right is None:  # 현재 노드의 오른쪽이 비어있으면
        current.right = new_node  # 새 노드 연결
        break
      current = current.right  # 오른쪽 노드로 current 변경 (이동)
  return root


def post_order(node):  # 재귀 -> 반복
  if node is None:
    return

  stack = list()
  output = list()
  stack.append(node)

  while stack:
    current = stack.pop()
    output.append(current.val)

    if current.left:
      stack.append(current.left)  # push
    if current.right:
      stack.append(current.right)  # push

  for value in reversed(output):
    print(value)


inputs = [50, 30, 24, 5, 28, 45, 98, 52, 60]  # preorder input
root = None
# for i in sys.stdin:
#   root = insert(root, int(i.strip()))
for i in inputs:
   root = insert(root, i)

post_order(root)
