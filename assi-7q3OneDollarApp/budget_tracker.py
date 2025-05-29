class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return f"{self.item}: ${self.amount}"

class BudgetTracker:
    def __init__(self, starting_amount=1.0):
        self.total = starting_amount
        self.expenses = []

    def add_expense(self, item, amount):
        if amount > self.total:
            print("Not enough budget!")
        else:
            expense = Expense(item, amount)
            self.expenses.append(expense)
            self.total -= amount
            print(f"Added: {item} - ${amount}")

    def show_summary(self):
        print("\n--- Budget Summary ---")
        for e in self.expenses:
            print(e)
        print(f"Remaining: ${self.total:.2f}")

# --- CLI Interface ---
tracker = BudgetTracker()

while True:
    print("\n1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")
    choice = input("Choose option (1-3): ")

    if choice == "1":
        item = input("Enter item name: ")
        amount = float(input("Enter amount spent: $"))
        tracker.add_expense(item, amount)
    elif choice == "2":
        tracker.show_summary()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
        
