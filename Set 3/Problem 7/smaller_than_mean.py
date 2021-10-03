import statistics
a = [1, 2, 3, 4, 5, 6]
print(statistics.mean(a))

def binarysearchcount(a, n, k):
    left = 0
    right = n - 1
    count = 0
    while (left <= right):
        mid = int((right + left) / 2)
        if (a[mid] <= k):
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count
k = 3.5
n = len(a)
print(binarysearchcount(a, n, k))
