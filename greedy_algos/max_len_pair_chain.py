from typing import List

arr = [[1,2],[7,8],[4,10],[4,5]]
e1 = [[1,2]]
e2 = [[1,2],  [3,5],  [3,4],  [1,4],    [3,6],  [5,6],  [7,9]]

def sort_arr(arr):
    print('sorting')
    arr.sort(key=(lambda x: x[1]))
    return arr

print(sort_arr(e2))

def findLongestChain(pairs: List[List[int]]) -> int:
    pairs.sort(key=(lambda x: (x[0], x[1])))
    last = pairs[-1][0]
    chain = 1
    for i in range(len(pairs)-2, -1, -1):
        if pairs[i][1] < last:
            chain += 1
            last = pairs[i][0]
    return chain

# print(findLongestChain(e1))



        
