




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None 

    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围！")

        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise Exception("超出链表节点范围！")

        node = Node(data)

        if self.size == 0:
            # 空链表
            self.head = node
            self.last = node
        elif index == 0:
            # 插入头部
            node.next = self.head
            self.head = node
        elif index == self.size:
            # 插入尾部
            self.last.next = node
            self.last = node
        else:
            # 插入中间
            prev_node = self.get(index-1)
            node.next = prev_node.next
            prev_node.next = node.next
        self.size += 1 

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("超出链表节点范围！")
        
        removed_node = None # 暂存被删除的节点，用于返回
        if index == 0:
            # 删除头节点
            removed_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            # 删除尾部
            removed_node = self.last
            self.last = self.get(index-1)
            self.last.next = None
        else:
            # 删除中间
            prev_node = self.get(index-1)
            removed_node = prev_node.next
            prev_node.next = removed_node.next


        self.size -= 1
        return removed_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

linkedList = LinkedList()
linkedList.insert(3, 0)
linkedList.insert(4, 0)
linkedList.insert(9, 2)
linkedList.insert(5, 3)
linkedList.insert(6, 1)
linkedList.remove(0)
linkedList.output()


