#判断一个列表中是否存在：连续两个相同的数字
def samenum(n):
    if len(n) < 2:
        return False

    t = n[0]
    for i in range(1,len(n)):
        if t == n[i]:
            return True
        t = n[i]

    return False