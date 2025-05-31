# Find the maximum sum of a subarray of size 3

def maxSum(arr: list[int], k: int) -> int:
    """"""
    n = len(arr)
    if k <= 0 or k > n:
        print("Invalid window size")
        return
    # Find the sum of 1st window
    windiw_sum = sum(arr[:k])
    max_sum = windiw_sum
    for i in range(n-k):
        windiw_sum = windiw_sum - arr[i] + arr[i+k]
        max_sum = max(windiw_sum, max_sum)

    return max_sum

arr = [11, 2, 3, 4, 5, 6, 12]

print(maxSum(arr, 0))