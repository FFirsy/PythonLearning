def count_types(nums):
    d = {"pos": 0, "neg": 0, "zero": 0}
    for i in nums:
        if i == 0:
            d["zero"] += 1
        elif i > 0:
            d["pos"] += 1
        else:
            d["neg"] += 1
    return d

def has_consecutive(nums):
    if len(nums) < 2:
        return False

    t = nums[0]
    for i in range(1,len(nums)):
        if t == nums[i]:
            return True
        t = nums[i]

    return False

def main(nums):
    counts_result = count_types(nums)
    has_consecutive_result = has_consecutive(nums)

    return {
        "counts": counts_result,
        "has_consecutive": has_consecutive_result
    }


