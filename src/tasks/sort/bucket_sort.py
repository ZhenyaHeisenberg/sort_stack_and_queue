import sys
import os
import logging.config


sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from common.config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)


from .bubble_sort import bubble_sort


def bucket_sort(arr: list[float], buckets: int | None = None) -> list[float] | str: 
    if buckets == "":
        n = len(arr)

        if n < 50:
            bucket_list = [[] for x in range(n)]
        elif n < 1000:
            bucket_list = [[] for x in range(n // 10)]
        else:
            bucket_list = [[] for x in range(round(n**0.5))]
    elif isinstance(buckets, int) and buckets < 1:
        logger.error("The number of baskets must be a natural number >= 1")
        return "The number of baskets must be a natural number >= 1"
    
    elif isinstance(buckets, int):
        bucket_list = [[] for x in range(buckets)]
    else:
        logger.error("The number of baskets must be a natural number")
        return "The number of baskets must be a natural number"
        
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
