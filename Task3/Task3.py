import json
import os

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        os.system("cls")
        data = input("Please enter the new expense (amount, description, category): ").split(",", maxsplit=2)
        amount, description, category = (data + ["", "", ""])[:3] 
        try:
            amount = float(amount.strip())
        except ValueError as e:
            amount = 0.0
        description, category = description.strip(), category.strip()

        if not self.expenses:
            id = 1

        expense = {
            "id": len(self.expenses) + 1,
            "amount": amount,
            "description": description,
            "category": category
        }
        self.expenses.append(expense)
        self.save_data()
        os.system("cls")
        print(f"New expense with the ID {len(self.expenses)} is added.")
        print("New List\n" + "-"*50)
        tracker.list_expenses()

    def list_expenses(self):
        if not self.expenses:
            print("No expense added yet.")
            return
        totalAmount = 0
        print("\nID  | Amount | Category      | Description")
        print("-"*50)
        for expense in self.expenses:
            try:
                totalAmount += expense['amount']
            except ValueError as e:
                totalAmount += 0
            print(f"{expense['id']:3} | {expense['amount']:6} | {expense['category']:<13} | {expense['description']}")
        print("-"*50 + f"\nTotal amount spent: {totalAmount}")

    def update_expense(self):
        if not self.expenses:
            os.system("cls")
            print("No expense added yet.")
            return
        
        os.system("cls")
        print("Old List\n" + "-"*50)
        tracker.list_expenses()
        data = input("Please enter the values to update (id, amount, description, category): ").split(",", maxsplit=3)
        id, amount, description, category = (data + ["", "", ""])[:4] 
        try:
            expense_id = int(id.strip())
            try:
                amount = float(amount.strip())
            except ValueError as e:
                amount = 0.0
            description, category = description.strip(), category.strip()
            for expense in self.expenses:
                if expense["id"] == expense_id:
                    expense["amount"] = amount
                    expense["description"] = description
                    expense["category"] = category
                    self.save_data()
                    os.system("cls")
                    print(f"Expense with the ID {expense["id"]} is updated.")
                    print("New List\n" + "-"*50)
                    tracker.list_expenses()
                    return
            os.system("cls")
            print("Couldn't find an expense with the given ID.")
        except ValueError as e:
            os.system("cls")
            print(f"Please enter a number for the ID. Error: {e}")
        
    def delete_expense(self):
        if not self.expenses:
            os.system("cls")
            print("No expense added yet.")
            return
        
        try:
            os.system("cls")
            print("Old List\n" + "-"*50)
            tracker.list_expenses()
            id = int(input("Please enter the ID: "))
            for expense in self.expenses:
                if expense["id"] == id:
                    self.expenses = [expense for expense in self.expenses if expense["id"] != id]
                    self.save_data()
                    os.system("cls")
                    print(f"Expense with the ID {id} is deleted.")
                    for i in range(id, len(self.expenses) + 2):
                        for expense in self.expenses:
                            if expense["id"] == i:
                                expense["id"] = expense["id"] - 1
                            self.save_data()
                    print("New List\n" + "-"*50)
                    tracker.list_expenses()
                    return
            os.system("cls")
            print(f"Couldn't find an expense with the ID {id}.")
        except ValueError as e:
            os.system("cls")
            print(f"Please enter a number for the ID. Error: {e}")
    
    def help(self):
        functions = [
            "Add Expense:\n  Adds a new expense entry with an amount, category, and description.\n  Usage: tracker.add_expense(50, 'Lunch', 'Food')\n  Steps:\n    1. Select 'Add(1)' from the main menu.\n    2. Enter 'amount', 'description', and 'category' separated by commas.\n    3. If you want to skip a value, leave it blank and continue.",
            "List Expenses:\n  Displays all recorded expenses. If no expenses exist, it informs the user.\n  Usage: tracker.list_expenses()\n  Steps:\n    1. Select 'List(2)' from the main menu.\n    2. The list of expenses will be displayed in order.",
            "Update Expense:\n  Modifies an existing expense by its ID. You can update one or multiple fields (amount, category, description).\n  Usage: tracker.update_expense(1, amount=55, description='Fruit shopping', category='Groceries')\n  Steps:\n    1. Select 'Update(3)' from the main menu.\n    2. Enter the ID of the expense you want to update.\n    3. Specify new values (leave blank to keep the old ones).\n    4. Confirm the update.",
            "Delete Expense:\n  Removes an expense entry permanently by its ID.\n  Usage: tracker.delete_expense(1)\n  Steps:\n    1. Select 'Delete(4)' from the main menu.\n    2. Enter the ID of the expense you want to delete.\n    3. Confirm deletion.",
        ]
        os.system("cls")
        print("\n".join(functions))

tracker = ExpenseTracker()
i = ""
while i != "0":
    deger = input("\nAdd(1) / List(2) / Update(3) / Delete(4) / Help(5) / Exit(0)\nPlease chose what to do: ")
    if deger == "1":
        tracker.add_expense()
        
    elif deger == "2":
        os.system("cls")
        print("Current List\n" + "-"*50)
        tracker.list_expenses()
        
    elif deger == "3":
        tracker.update_expense()

    elif deger == "4":
        tracker.delete_expense()

    elif deger == "5":
        tracker.help()

    elif deger == "0":
        i = "0"

    else:
        print(f"Error! Entered an unknown command: '{deger}'")
