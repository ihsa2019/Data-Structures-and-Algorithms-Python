class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def pre_order(root):
    if root:
        print(str(root.data) + "->", end="")
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    if root:
        in_order(root.left)
        print(str(root.data) + "->", end="")
        in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(str(root.data) + "->", end="")


def main():
    tree = Node(1)
    tree.left = Node(12)
    tree.right = Node(9)
    tree.left.left = Node(5)
    tree.left.right = Node(6)

    print("Tree in pre-order: ", end="")
    pre_order(tree)

    print("Tree in in-order: ", end="")
    in_order(tree)

    print("Tree in post-order: ", end="")
    post_order(tree)