def can_partition(nums):
    s = sum(nums)

    if s % 2 != 0:
        return False
    
    dp = [[-1 for _ in range(int(s/2)+1)] for _ in range(len(nums))]
    
    def recur(id, sum):
        if sum == 0:
            return 1
        if id == len(nums):
            return 0

        if dp[id][sum] != -1:
            return dp[id][sum]

        if sum - nums[id] >= 0:
            if recur(id + 1, sum - nums[id]) == 1:
                dp[id][sum] = 1
                return 1

        dp[id][sum] = recur(id + 1, sum)

        return dp[id][sum]
    
    ans = recur(0, int(s/2))
    return ans == 1
    
print("Can partition: " + str(can_partition([1, 2, 3, 4])))

def main():
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()