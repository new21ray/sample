class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Helper method to recursively insert a value."""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Search for a value in the BST. Returns True if found, False otherwise."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Helper method to recursively search for a value."""
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        """Return a list of values in inorder traversal (sorted)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)


if __name__ == '__main__':
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    for val in values:
        bst.insert(val)
    
    print('Inorder traversal:', bst.inorder_traversal())
    print('Search 40:', bst.search(40))
    print('Search 100:', bst.search(100))