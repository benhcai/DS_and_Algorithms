def findKSmallest(list, k):
    # build heap
    # heapify
    for i in range(len(list)-1,-1,-1):
        j = i
        while j >= 0:
            left = 2*j + 1
            right = 2*j + 2
            smallest = j
            if left < len(list) and list[smallest] > list[left]:
                smallest = left
            if right < len(list) and list[smallest] > list[right]:
                smallest = right
            if smallest != j:
                temp = list[j]
                list[j] = list[smallest]
                list[smallest] = temp
                j = smallest
                continue
            break
    
    # remove min
    result = []
    for _ in range(3):
        result.append(list[0])
        list[0] = list[-1]
        del list[-1]            
        # heapify
        m = 0
        while m < len(list):
            left = 2*m + 1
            right = 2*m + 2
            smallest = m
            if left < len(list) and list[smallest] > list[left]:
                smallest = left
            if right< len(list) and list[smallest] > list[right]:
                smallest = right
            if smallest != m:
                temp = list[smallest]
                list[smallest] = list[m]
                list[m] = temp
                m = smallest
                continue
            break

    return result

print(findKSmallest([9, 4, 7, 1, -2, 6, 5], 3))
print('done')
    # remove min
