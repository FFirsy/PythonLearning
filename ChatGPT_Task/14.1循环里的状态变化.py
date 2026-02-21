#计算：正数个数,负数个数,0 的个数
def numstpye(nums):
    d = {"pos": 0, "neg": 0, "zero": 0}
    for i in nums:
        if i == 0:
            d["zero"] += 1
        elif i > 0:
            d["pos"] += 1
        else:
            d["neg"] += 1
    return d
