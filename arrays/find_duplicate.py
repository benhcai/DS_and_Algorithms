def findDuplicate(arr):
    slow = 0; fast = arr[0] 
    print(arr[0], arr[arr[0]])
    while arr[slow] != arr[fast]:
        print('first', slow, fast)
        slow = arr[slow]
        fast = arr[arr[fast]]
    slow = 0
    print('done', slow, fast)
    return
    print(slow, fast)
    while arr[slow] != arr[fast]:
        slow = arr[slow]
        fast = arr[fast]
        print('second', slow, fast)
    return arr[slow]

print(findDuplicate([4,2,1,3,1]))
