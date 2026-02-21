def save_balance(balance):
    with open("balance.txt", "w") as f:
        f.write(str(balance))

def load_balance():
    try:
        with open("balance.txt", "r") as f:
            content = f.read().strip()
            return float(content)
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

def apply_transaction(balance, amount):
    return balance + amount

def process_transactions(transactions):
    balance = load_balance()
    for transaction in transactions:
        new_balance = apply_transaction(balance, transaction)

        if new_balance < 0:
            return "Overdraft"

        balance = new_balance
        save_balance(balance)
    return balance

def main(transactions):
    balance = process_transactions(transactions)
    if balance == "Overdraft":
        print("Overdraft detected")
    else:
        print("Final balance:", balance)