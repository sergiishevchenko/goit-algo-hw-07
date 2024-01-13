def get_max_value(root):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right
    return current.key
