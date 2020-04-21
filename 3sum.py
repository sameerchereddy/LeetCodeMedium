def threeSum(nums):
    l = len(nums)
    nums.sort()
    ans = set()
    for i in range(0,l-2):
        d = set()
        s = 0-nums[i]
        
        for j in range(i+1,l):
            x = s-nums[j]
            if x not in d:
                d.add(nums[j])
            else:
                ans.add((nums[i],nums[j],x))
    return list(ans)

print(threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))





