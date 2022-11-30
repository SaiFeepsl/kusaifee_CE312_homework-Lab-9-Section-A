def BinarySearch(arr, k, low, high):

    if high >= low:

        mid = low + (high - low)//2

        if arr[mid] == k:
            return mid

        elif arr[mid] > k:
            return BinarySearch(arr, k, low, mid-1)

        else:
            return BinarySearch(arr, k, mid + 1, high)

    else:
        return -1


arr = [1,4,5,7,9,10,11,13]
k = 5

result = BinarySearch(arr, k, 0, len(arr)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")