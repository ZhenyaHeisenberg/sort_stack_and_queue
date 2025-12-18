import os
import sys
import logging

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
sys.path.insert(0, src_dir)


try: #pragma: no cover
    from common.config import LOGGING_CONFIG
except ImportError: #pragma: no cover
    from src.common.config import LOGGING_CONFIG 

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def sub_radix_sort(a: list[int], base: int) -> list[int]: # O(n*k)
    
    
    
    if len(a) == 0:
        return []
    
    rank = len(str(max(a)))
    
    arr = [str(int(x)) for x in a]
    
    for i in range(len(arr)):
        delta = rank - len(arr[i])
        arr[i] = "0" * delta + arr[i]
    
    sub_arr = []
    for index in range(rank-1, -1, -1):
        for counting in range(base):
            for i in arr:
                if int(i[index]) == counting:
                    sub_arr.append(i)

        arr = sub_arr
        sub_arr = []
    
    sub_arr = arr
    arr = [int(x) for x in sub_arr]
    
    return arr

def radix_sort(a: list[int], base: int) -> list[int]:
    
    if base == "":
        base = 10
    
    elif not isinstance(base, int) or base < 2:
        logger.error("base must a natural number >= 2")
        return "base must a natural number >= 2"

    
    negative_arr = [abs(x) for x in a if x<0]
    non_negative_arr = [x for x in a if x>=0]
    
    negative_arr = sub_radix_sort(negative_arr, base)
    negative_arr = negative_arr[::-1]
    non_negative_arr = sub_radix_sort(non_negative_arr, base)
    
    arr = []
    
    arr = [-1*x for x in negative_arr]
    
    for x in non_negative_arr:
        arr.append(x)
    
    return arr
