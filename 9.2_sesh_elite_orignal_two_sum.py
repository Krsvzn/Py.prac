nums = [2,7,11,15]
target = 9
result = False

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])
            break
    if result:
        break
