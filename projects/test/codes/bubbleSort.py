#冒泡排序
def bubbleSort():
    # 无序序列
    arr = list([4, 1, 9, 3, 2, 7, 10, 6, 8, 5])
    length = len(arr)
    # 外部循环 (n-1)次
    for i in range(length - 1):
        # 内部循环
        for j in range(length - 1 - i):
            if arr[j] > arr[j+1]:
                # 交换
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j+1] = tmp
    return arr # 返回已排序好的序列
