def build_tree(arr, n, i): # O(n*log(n))
    root = i
    
    left_child = i*2 + 1
    right_child = i*2 + 2
    
        
    if left_child < n and arr[left_child] > arr[root]:
        root = left_child
    
    if right_child < n and arr[right_child] > arr[root]:
        root = right_child
    
    if root != i: # если меняли корень => нужно проверить ветки
        arr[i], arr[root] = arr[root], arr[i] 
        build_tree(arr, n, root)


def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        build_tree(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        build_tree(arr, i, 0)
    
    return arr