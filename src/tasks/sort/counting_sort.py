def counting_sort(arr: list[int]) -> list[int]: # O(n + k)
    
    if len(arr) == 0:
        return []
    s = dict()

    min_num = min(arr)
    max_num = max(arr)
    for i in range(len(arr)):
        if arr[i] in s:
            s[arr[i]] += 1
        else:
            s[arr[i]] = 1
    arr = []

    for i in range(int(min_num), int(max_num)+1):
        if i in s:
            for k in range(s[i]):
                arr.append(i)
    return arr
