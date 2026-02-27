import json
from datetime import datetime


# =========================
# 数据模型层
# =========================
class Transaction:
    def __init__(self, amount, t_type, note="", category="other", timestamp=None):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if t_type not in ("income", "expense"):
            raise ValueError("Invalid transaction type.")

        self.amount = amount
        self.type = t_type
        self.note = note
        self.category = category
        self.timestamp = timestamp or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "amount": self.amount,
            "type": self.type,
            "note": self.note,
            "category": self.category,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            amount=data["amount"],
            t_type=data["type"],
            note=data.get("note", ""),
            category=data.get("category", "other"),
            timestamp=data.get("timestamp")
        )


# =========================
# 业务系统层
# =========================
class Ledger:
    def __init__(self, filename="ledger.json"):
        self.filename = filename
        self.transactions = []
        self.load()

    # ---------- 数据层 ----------
    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                self.transactions = [
                    Transaction.from_dict(item) for item in raw_data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.transactions = []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [t.to_dict() for t in self.transactions],
                f,
                indent=4,
                ensure_ascii=False
            )

    # ---------- 业务逻辑 ----------
    def add_transaction(self, amount, t_type, note="", category="other"):
        transaction = Transaction(amount, t_type, note, category)
        self.transactions.append(transaction)
        self.save()

    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t.type == "income":
                balance += t.amount
            else:
                balance -= t.amount
        return balance

    def get_total_income(self):
        return sum(t.amount for t in self.transactions if t.type == "income")

    def get_total_expense(self):
        return sum(t.amount for t in self.transactions if t.type == "expense")

    def list_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        for i, t in enumerate(self.transactions):
            print(
                f"{i}: {t.timestamp} | "
                f"{t.type} | "
                f"{t.amount:.2f} | "
                f"{t.category} | "
                f"{t.note}"
            )

    def delete_transaction(self, index):
        if 0 <= index < len(self.transactions):
            del self.transactions[index]
            self.save()
            print("Transaction deleted.")
        else:
            print("Invalid index.")

    def monthly_summary(self, month_prefix):
        total = 0
        for t in self.transactions:
            if t.timestamp.startswith(month_prefix):
                if t.type == "income":
                    total += t.amount
                else:
                    total -= t.amount
        return total

    # ---------- CLI ----------
    def show_menu(self):
        print("\n========== Ledger System ==========")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Statistics")
        print("5. List Transactions")
        print("6. Delete Transaction")
        print("7. Monthly Summary")
        print("8. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose: ").strip()

            if choice == "1":
                try:
                    amount = float(input("Income amount: "))
                    note = input("Note: ")
                    category = input("Category: ")
                    self.add_transaction(amount, "income", note, category)
                    print("Income added.")
                except ValueError as e:
                    print(e)

            elif choice == "2":
                try:
                    amount = float(input("Expense amount: "))
                    note = input("Note: ")
                    category = input("Category: ")
                    self.add_transaction(amount, "expense", note, category)
                    print("Expense added.")
                except ValueError as e:
                    print(e)

            elif choice == "3":
                print(f"Current Balance: {self.get_balance():.2f}")

            elif choice == "4":
                print(f"Total Income: {self.get_total_income():.2f}")
                print(f"Total Expense: {self.get_total_expense():.2f}")

            elif choice == "5":
                self.list_transactions()

            elif choice == "6":
                try:
                    index = int(input("Enter index to delete: "))
                    self.delete_transaction(index)
                except ValueError:
                    print("Invalid input.")

            elif choice == "7":
                month = input("Enter month (YYYY-MM): ")
                result = self.monthly_summary(month)
                print(f"Net result for {month}: {result:.2f}")

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")


# =========================
# 程序入口
# =========================
if __name__ == "__main__":
    app = Ledger()
    app.run()