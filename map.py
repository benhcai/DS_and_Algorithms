s = 'aba'
w = ['dog','cat','dog', 'dog', 'mouse', 'cat', 'mouse']
nums1 = [1,2,3]
nums2 = [10,20,30]

res = map(s.find, s)
bel = map(w.index, w)
print(list(res))
print(list(bel))
