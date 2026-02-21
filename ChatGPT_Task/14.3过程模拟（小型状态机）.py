#模拟一个简单账户系统：给定一个交易列表：
def transaction_list(transactions):
    account = 0
    for i in transactions:
        account += i
        if account < 0:
            return "Overdraft"

    return account
