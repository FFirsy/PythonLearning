def apply_transaction(balance, amount):
    balance += amount
    return balance

def process_transactions(transactions):
    balance = 0
    for transaction in transactions:
        balance = apply_transaction(balance, transaction)
        if balance < 0:
            return "Overdraft"
    return balance

def main(transactions):
    balance = process_transactions(transactions)
    if balance == "Overdraft":
        print("Overdraft detected")
    else:
        print("Final balance:", balance)

if __name__ == '__main__':
    transactions = [100, -50, 20, -10, 30]
    main(transactions)


