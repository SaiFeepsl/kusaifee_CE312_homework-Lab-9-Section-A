def LinearSearch(array, n, k):

    for j in range(0, n):

        if (array[j] == k):

            return j

    return -1

 
array = [1,4,5,7,9,10,11,13]

k = 7
n = len(array)

result = LinearSearch(array, n, k)

if(result == -1):

    print("Element not found")

else:

    print("Element found at index: ", result)