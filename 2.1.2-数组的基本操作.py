# P28
class MyArray:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        # 判断下标是否超出范围
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围！")
        # 从右向左循环，逐个元素向右挪一位
        for i in range(self.size-1, index-1, -1):
            self.array[i+1] = self.array[i]
        
        # 腾出的位置放入新元素
        self.array[index] = element
        self.size += 1

    # 数组扩容（翻倍）
    def insert_v2(self, index, element):
        # 判断下标是否超出范围
        if index < 0 or index > self.size:
            raise Exception("超出数组实际元素范围！")
        if self.size >= len(self.array):
            new_array = [None] * self.size * 2
            for i in range(self.size):
                new_array[i] = self.array[i]
            self.array = new_array
        
        for i in range(self.size-1, index-1, -1):
            self.array[i+1] = self.array[i]
        
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        # 判断下标是否超出范围
        if index < 0 or index >= self.size:
            raise Exception("超出数组实际元素范围！")
        
        for i in range(index, self.size-1):
            self.array[i] = self.array[i+1]
        self.size -= 1

    
    def output(self):
        for i in range(self.size):
            print(self.array[i])

array = MyArray(4)
array.insert(0, 10)
array.insert(0, 11)
array.insert(0, 15)
array.insert(0, 16)
array.remove(1)
array.output()
        

