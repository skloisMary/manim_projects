def adjust_heap(data, index, len):
    # 取出index位置的元素
    tmp = data[index] 
    # 从index节点的左子节点开始，也就是从2*index+1开始
    k = 2 * index + 1
    while k < len:
            #如果左子节点小于右子节点，k指向右子节点
        if (k+1) < len and data[k] < data[k+1]:
            k += 1
        # 如果子节点大于父节点，将子节点的值赋给父节点
        if data[k] > tmp:
            data[index] = data[k]
            index = k
        else:
            break
        k = 2*k + 1
    data[index] = tmp #将tmp值放到最终的位置

def heap_sort():
    data = [96,83,38,27,9,11,7]
    length = len(data)
    #构造大顶堆，从非叶子结点开始倒序遍历(自下而上)
    for i in range(length//2-1, -1, -1):
        adjust_heap(data, i, length)
    for j in range(length-1, -1, -1):
        #将堆顶元素与末尾元素进行交换
        tmp = data[0]
        data[0] = data[j]
        data[j] = tmp
        # 重新对堆进行调整
        adjust_heap(data, 0, j)
