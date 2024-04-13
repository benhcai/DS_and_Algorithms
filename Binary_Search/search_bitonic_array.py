def solve(A, B):
    # Find peak
    left = 0
    right = len(A) - 1
    mid = len(A) // 2
    while left < right:
        mid = left + (right-left) // 2
        if A[mid] < A[mid+1]:
            left = mid + 1
        else:
            right = mid
    peak = left
    print(peak, A[peak])
    
    # Binary Search in 2 left and right side arrays
    left = 0
    right = peak
    while left <= right:
        mid = left + (right-left) // 2
        if A[mid] == B:
            return mid
        if A[mid] < B:
            left = mid + 1
        else:
            right = mid - 1
    
    left = peak
    right = len(A) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if A[mid] == B:
            return mid
        if A[mid] < B:
            right = mid - 1
        else:
            left = left + 1

    return -1

print(solve([1,2,3,4,5,20,19,18,17,16], 18))
