def load_data():
    """从文件加载交易记录，返回浮点数列表；文件不存在或内容非法时返回空列表"""
    transactions = []
    try:
        with open("ledger.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:  # 跳过空行
                    try:
                        transactions.append(float(line))
                    except ValueError:
                        # 忽略无法转换的行，也可以选择打印警告
                        continue
    except FileNotFoundError:
        # 文件不存在，返回空列表
        pass
    return transactions

def save_data(transactions):
    """将交易记录列表保存到文件，每行一个数字"""
    with open("ledger.txt", "w") as f:
        for amount in transactions:
            f.write(f"{amount}\n")

def add_income(transactions, amount):
    """添加一笔收入（正数），返回新的交易列表"""
    transactions.append(amount)
    return transactions

def add_expense(transactions, amount):
    """添加一笔支出（正数转换为负数后添加），返回新的交易列表"""
    transactions.append(-amount)  # 支出记为负数
    return transactions

def print_menu():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Exit")

def run_system():
    transactions = load_data()  # 此时 transactions 是一个列表
    while True:
        print_menu()
        choice = input("Enter your choice:").strip()

        if choice == "1":
            a = input("请输入本次收入：").strip()
            try:
                amount = float(a)
                if amount < 0:
                    print("收入金额不能为负数，请重新输入。")
                    continue
                transactions = add_income(transactions, amount)
                save_data(transactions)
                # 计算当前余额并显示
                balance = sum(transactions)
                print(f"收入{amount}元成功，当前余额：{balance:.2f} 元")
            except ValueError:
                print("输入无效，请输入数字")

        elif choice == "2":
            b = input("请输入本次支出：").strip()
            try:
                amount = float(b)
                if amount < 0:
                    print("支出金额不能为负数，请重新输入。")
                    continue
                transactions = add_expense(transactions, amount)
                save_data(transactions)
                balance = sum(transactions)
                print(f"支出{amount}元成功，当前余额：{balance:.2f} 元")
            except ValueError:
                print("输入无效，请输入数字")

        elif choice == "3":
            balance = sum(transactions) if transactions else 0.0
            print("balance:", balance)

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_system()