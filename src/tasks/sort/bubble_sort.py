def bubble_sort(a: list[int]) -> list[int]:
    i = 0
    t = True
    while t:
        t = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                t = True
        i = i + 1
    return a
