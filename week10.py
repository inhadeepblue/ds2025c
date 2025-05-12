class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def pre_order(node):
    if node is None:
        return
    print(node.data, end='->')
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end='->')
    in_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='->')


def insert(node, value):
    new_node = TreeNode()
    new_node.data = value

    if node is None:  # 첫 번째 노드 처리
        return new_node

    current = node
    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right  # move
    return node


def search(find_number):

    current = root
    while True:
        if find_number == current.data:
            return True
        elif find_number < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
            current = current.right


def delete(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else:  # 삭제할 노드 발견
        # 자식 노드가 1개 이거나 leaf노드인 경우
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

    return node


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 14]
    # numbers = [10, 15, 8, 3, 9, 1, 7, 100]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")

    post_order(root)  # 3->9->8->15->10
    print()
    in_order(root)  # 3->8->9->10->15
    print()
    pre_order(root)  # 10->8->3->9->15
    print()

    find_number = int(input("찾는 값 입력 : "))
    if search(find_number):
        print(f"{find_number}을(를) 찾았습니다")
    else:
        print(f"{find_number}이(가) 존재하지 않습니다")


    delete_number =  int(input("제거할 값 입력 : "))
    root = delete(root, delete_number)

    post_order(root)
    print()
    in_order(root)
    print()
    pre_order(root)
    print()