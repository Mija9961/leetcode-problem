# Find the maximum sum of the subarray from a given array

from typing import List

def max_sum(arr: List[int], k: int) -> int:
    n = len(arr)
    if k <= 0 or k > n:
        print("Invalid window size")
        return
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum + arr[i] - arr[i-k]
        
        max_sum = max(max_sum, window_sum)
    return max_sum

arr = [1,8,-8,4]
res = max_sum(arr, -2)

print("Res",res)
