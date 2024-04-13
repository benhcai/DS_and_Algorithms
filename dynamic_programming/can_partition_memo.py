def can_partition(nums):
    s = sum(nums)
    
    # The sum has to be even for two sets to exist. 
    if s % 2 != 0:
        return False
    
    dp = [[-1 for _sum in range(int(s/2)+1)] for _id in range(len(nums))]

    def recur(id, sum):
        if sum == 0:
            return 1
        if id == len(nums):
            return 0

        if dp[id][sum] != -1:
            return dp[id][sum]

        if sum - nums[id] >= 0:
            if recur(id+1, sum-nums[id]) == 1:
                print(sum-nums[id])
                dp[id][sum] = 1
                return 1

        dp[id][sum] = recur(id+1, sum)
        return dp[id][sum]
    
    res = recur(0, int(s/2))
    return res == 1

# print(can_partition([1,2,3,4]))
print(can_partition([1,1,3,4,7]))
# print(can_partition([2,3,4,6]))
