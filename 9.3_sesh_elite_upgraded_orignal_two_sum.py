nums = [2,7,11,15]
target = 9
seen = {}

for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        print(f"[{seen[diff]}] ,[{i}]")
        break
    seen[num] = i
