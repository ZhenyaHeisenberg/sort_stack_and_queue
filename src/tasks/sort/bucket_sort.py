from .bubble_sort import bubble_sort

def bucket_sort(arr: list[float], buckets: int | None = None) -> list[float] | str: 
    if buckets is None:
        n = len(arr)

        if n < 50:
            bucket_list = [[] for x in range(n)]
        elif n < 1000:
            bucket_list = [[] for x in range(n // 10)]
        else:
            bucket_list = [[] for x in range(round(n**0.5))]
    elif buckets < 1:
        return "The number of baskets must be >= 1"
    
    else:
        bucket_list = [[] for x in range(buckets)]
        
    if arr == []:
        return []

    bucket_count = (len(bucket_list))
    
    min_num = min(arr)
    
    bucket_size = len(arr) // bucket_count + 1
    
    for i in range(len(arr)):

        bucket_index = min(int((arr[i] - min_num) // bucket_size), bucket_count-1)
        bucket_list[bucket_index].append(arr[i])
    
    for i in range(bucket_count):
        bucket_list[i] = bubble_sort(bucket_list[i]) # Применение собственной функции сортировки
    
    arr = []
    
    for i in range(bucket_count):
        arr.extend(bucket_list[i])
    
    return arr
