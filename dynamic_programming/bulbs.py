class Solution:
    def bulbs(self, arr):
        count = 0
        if len(arr) > 1:
            for i in range(len(arr) - 1, 0, -1):
                left = arr[i-1] 
                right = arr[i]
                if left != right:
                    count += 1
        if arr[0] == 0:
            count += 1
        return count

solution = Solution()

print(solution.bulbs([0,1,0,1]))
print(solution.bulbs([1,0,1,0]))
print(solution.bulbs([0,1,0,0,1,1,0,1]))
print('Edge Cases')
print(solution.bulbs([0,0]))
print(solution.bulbs([0,1]))
print(solution.bulbs([1,0]))
print(solution.bulbs([1]))
print(solution.bulbs([0]))
