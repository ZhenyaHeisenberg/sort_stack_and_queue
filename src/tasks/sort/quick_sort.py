def partition(a: list[int], start: int, end: int) -> int: # O(n*log(n)) | O(n^2)    
    v = a[(start + end) // 2]
    i = start
    j = end
    while (i <= j):
        while (a[i] < v):
            i += 1
        while (a[j] > v):
            j -= 1
        if (i >= j):
            break

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return j


def sub_quick_sort(a: list[int], start: int, end: int) -> list[int]:
    if start < end:
        pivot = partition(a, start, end)
        sub_quick_sort(a, start, pivot)
        sub_quick_sort(a, pivot+1, end)
    return a


def quick_sort(a: list[int]) -> list[int]:
    start = 0
    end = len(a)-1
    sub_quick_sort(a, start, end)
    return a
