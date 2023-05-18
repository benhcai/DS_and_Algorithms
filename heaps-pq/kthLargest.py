class KthLargest:
    def __init__(self, k, nums):
        self.stream = set()
        self.recursiveAdd(nums)

    def add(self, val: int) -> int:
        self.recursiveAdd(val)
        return list(self.stream).index(val)

    def recursiveAdd(self, el):
        if type(el) is int:
            self.stream.add(el)
        else:
            for i in el:
                self.recursiveAdd(i)

test = [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

sol = KthLargest(4, test)
print(sol.stream)
