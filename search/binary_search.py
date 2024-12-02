arr = [1,2,3,3,3,4,5,6,7,8,9]

def binary_search(arr, target):
    l,r = 0, len(arr)-1

    while l <= r:        
        m = l + (r - l) // 2

        if target > arr[m]:
            l = m + 1
        elif target < arr[m]:
            r = m - 1
        else:
            return m

    return -1
    
binary_search(arr, 5)