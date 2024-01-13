def get_min_value(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.key