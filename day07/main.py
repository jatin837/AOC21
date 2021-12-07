from collections import Counter

c = Counter()

nums = list(map(int, input().split(',')))

nums.sort()

ans1 = 0
mid = nums[len(nums)//2]


for num in nums:
    ans1 += abs(num - mid)

# print(ans1)


res = []
m = max(nums)
for i in range(m+1):
    print("-"*10)
    n = 0
    temp = 0
    for j in range(len(nums)):
        n = abs(i - nums[j])
        print(int(0.5*n*(n+1)))
        temp += int(0.5*(n)*(n+1))

    res.append(temp)

print(res)

print(min(res))
            

    
