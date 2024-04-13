def pascal(numRows):
    row = 1
    prev = [1]
    ans = [prev]
    if numRows == 1:
        return prev
    while row < numRows:
        curr = []
        curr.append(1)
        for i in range(1, len(prev)):
            curr.append(prev[i-1] + prev[i])
        curr.append(1)
        ans.append(curr)
        prev = ans[row]
        row += 1
    return ans

print(pascal(5))
