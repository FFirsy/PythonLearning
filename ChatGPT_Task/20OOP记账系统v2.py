#数据结构升级
#存储方式改为 JSON
#支持时间戳和备注

import json
from datetime import datetime


class Ledger:
    def __init__(self, filename="ledger.json"):
        self.filename = filename
        self.transactions = []
        self.load()

    # ================= 数据层 =================
    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.transactions = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.transactions = []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.transactions, f, indent=4, ensure_ascii=False)

    # ================= 业务层 =================
    def add_transaction(self, amount, t_type, note=""):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        record = {
            "amount": amount,
            "type": t_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "note": note
        }

        self.transactions.append(record)
        self.save()

    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t["type"] == "income":
                balance += t["amount"]
            else:
                balance -= t["amount"]
        return balance

    def get_total_income(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "income")

    def get_total_expense(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "expense")

    # ================= CLI 层 =================
    def show_menu(self):
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Statistics")
        print("5. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose: ").strip()

            if choice == "1":
                try:
                    amount = float(input("Income amount: "))
                    note = input("Note: ")
                    self.add_transaction(amount, "income", note)
                    print("Income added.")
                except ValueError as e:
                    print(e)

            elif choice == "2":
                try:
                    amount = float(input("Expense amount: "))
                    note = input("Note: ")
                    self.add_transaction(amount, "expense", note)
                    print("Expense added.")
                except ValueError as e:
                    print(e)

            elif choice == "3":
                print(f"Balance: {self.get_balance():.2f}")

            elif choice == "4":
                print(f"Total income: {self.get_total_income():.2f}")
                print(f"Total expense: {self.get_total_expense():.2f}")

            elif choice == "5":
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = Ledger()
    app.run()