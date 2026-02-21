def nextStep(num):
    """
    输入一个整数 num
    如果是偶数，返回 num // 2
    如果是奇数，返回 num - 1
    """
    if num % 2 == 0:
        return num // 2
    else:
        return num - 1


def numberOfSteps(num):
    steps = 0
    while num > 0:
        num = nextStep(num)
        steps += 1
    return steps
