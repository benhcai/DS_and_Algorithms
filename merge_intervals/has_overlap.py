def has_overlap(intervals):
    intervals.sort(key=lambda x: x[0])
    if not intervals:
        return intervals
    current = [intervals[0][0], intervals[0][1]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= current[1]:
            return True
        else:
            current = intervals[i]
    return False

a = [[1,4], [2,5], [7,9]]
b = [[1,2], [3, 4], [5, 9]]
c = [[1,2], [3,10], [4,9]]
d = [[12, 20], [4,8]]
d = [[12, 20], [4,15], [9, 30]]

print(has_overlap(a))
print(has_overlap(b))
print(has_overlap(c))
print(has_overlap(d))

