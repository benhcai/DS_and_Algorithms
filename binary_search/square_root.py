def sqrt(A):
        if not A:
            return A
        left = 0
        right = A
        mid = int(A/2)
        while left <= right:
            print(mid)
            if mid**2 == A:
                return mid
            if mid**2 < A and (mid+1)**2 > A:
                return mid
            if mid**2 < A:
                left = mid + 1
            else:
                right = mid - 1
            mid = left + int((right-left)/2)
        return A

print(sqrt(6))
