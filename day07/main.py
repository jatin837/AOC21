from collections import Counter

nums = list(map(int, input().split(',')))

nums.sort()

ans1 = 0
mid = nums[len(nums)//2]


for num in nums:
    ans1 += abs(num - mid)

# print(ans1)

ans2 = 10e5
n = 0

for i in range(len(nums)):
    temp = 0
    for j in range(len(nums)):
        if i != j:
            n = abs(nums[i] - nums[j])
            temp += int(n*(n+1)/2)
    ans2 = min(ans2, temp)
    print(i, ans2)

#print(ans2)
