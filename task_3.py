def calculate(root):
    if root is None:
        return 0
    return root.key + calculate(root.left) + calculate(root.right)