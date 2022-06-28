from queue import Queue

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order_traversal(node):
    q = Queue()
    q.put(node)
    while not q.empty():
        node = q.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)
