def quick_sort(start_index, end_index, array=[]):
    # 递归结束条件：start_index大于或等于end_index的时候
    if start_index >= end_index:
        return
    # 得到基准元素的位置
    pivot_index = partition_v1(start_index, end_index, array)
    # 根据基准元素，分成两部分递归排序
    quick_sort(start_index, pivot_index - 1, array)
    quick_sort(pivot_index + 1, end_index, array)

def partition_v1(start_index, end_index, array=[]):
    # 取第一个位置的元素作为基准元素（也可以选择随机位置）
    pivot = array[start_index]
    left = start_index
    right = end_index
    while left != right:
        # 控制right指针进行比较并左移
        while left < right and array[right] > pivot:
            right -= 1
        # 控制left指针进行比较并右移
        while left < right and array[left] <= pivot:
            left += 1
        # 交换left指针和right指针指向的元素
        if left < right:
            p = array[left]
            array[left] = array[right]
            array[right] = p
    array[start_index] = array[left]
    array[left] = pivot
    return left

my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
quick_sort(0, len(my_array)-1, my_array)
print(my_array)

def partition_v2(start_index, end_index, array=[]):
    # 取第一个位置的元素作为基准元素（也可以选择随机位置）
    pivot = array[start_index]
    mark = start_index
    for i in range(start_index+1, end_index+1):
        if array[i] < pivot:
            mark += 1
            p = array[mark]
            array[mark] = array[i]
            array[i] = p
    array[start_index] = array[mark]
    array[mark] = pivot
    return mark

my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
quick_sort(0, len(my_array)-1, my_array)
print(my_array)

def quick_sort_with_stack(start_index, end_index, array=[]):
    # 用一个集合栈来代替递归的函数栈
    quick_sort_stack = []
    root_param = {"startIndex": start_index, "endIndex": end_index}
    quick_sort_stack.append(root_param)
    # 循环结束条件：栈为空时结束
    while len(quick_sort_stack) > 0:
        # 栈顶元素出栈，得到起止下标
        param = quick_sort_stack.pop()
        # 得到基准元素位置
        pivot_index = partition_v2(param.get("startIndex"), param.get("endIndex"), array)
        # 根据基准元素分成两部分，把每一部分的起止下标入栈
        if param.get("startIndex") < pivot_index - 1:
            left_param = {"startIndex": param.get("startIndex"), "endIndex": pivot_index - 1}
            quick_sort_stack.append(left_param)
        if pivot_index + 1 < param.get("endIndex"):
            right_param = {"startIndex": pivot_index + 1, "endIndex": param.get("endIndex")}
            quick_sort_stack.append(right_param)
