class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs))]
        def recur(id, m, n):
            if id == len(strs) or (m == 0 and n == 0):
                return 0
            
            if dp[id][m][n] != -1:
                return dp[id][m][n]

            include = 0
            if id < len(strs):
                m_count = 0
                n_count = 0
                for char in strs[id]:
                    if char == "0":
                        m_count += 1
                    if char == "1":
                        n_count += 1
                if (m - m_count >= 0 and n - n_count >= 0):
                    include = 1 + recur(id + 1, m - m_count, n - n_count)
            
            exclude = recur(id + 1, m, n)

            most_subsets = max(include, exclude)
            dp[id][m][n] = most_subsets
            return dp[id][m][n]
        
        most = recur(0, m, n)
        return most

strs = ["011","1","11","0","010","1","10","1","1","0","0","0","01111","011","11","00","11","10","1","0","0","0","0","101","001110","1","0","1","0","0","10","00100","0","10","1","1","1","011","11","11","10","10","0000","01","1","10","0"]
m = 44
n = 39

solution = Solution()
print(solution.findMaxForm(strs,m,n))
