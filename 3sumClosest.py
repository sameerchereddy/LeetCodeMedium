
def threeSumClosest(nums, target):
    a=nums
    t=target
    a.sort()
    b = sum(a[:3])
    n = len(a)
    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s == t:
                return s
            if abs(s - t) < abs(b - t):
                b = s
            if s < t:
                l += 1
            else:
                r -= 1
    return b

print(threeSumClosest([-1, 2, 1, -4],1))