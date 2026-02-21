def countEven(nums):
    a = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0 :
            a += 1
    return a