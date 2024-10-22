def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i -1
        while (j >= 0 and arr[j+1] < arr[j]):
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j -= 1
    
    print(arr)

insertion_sort([2,3,4,1,6])