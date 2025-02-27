import json
import os
import datetime

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
            if float(amount) > 0.0:
                amount = float(amount.strip())
            else:
                amount = 0.0
        except ValueError as e:
            amount = 0.0
        description, category = description.strip(), category.strip()

        if not self.expenses:
            id = 1

        expense = {
            "id": len(self.expenses) + 1,
            "amount": amount,
            "description": description,
            "category": category,
            "createdAt": datetime.datetime.now().strftime("%d/%m/%Y")
        }
        self.expenses.append(expense)
        self.save_data()
        os.system("cls")
        print(f"New expense with the ID {len(self.expenses)} is added.")
        print("New List\n" + "-"*50)
        tracker.list_expenses("")

    def list_expenses(self, data):
        if not self.expenses:
            print("No expense added yet.")
            return
        totalAmount = 0
        if data == "":
            Data = ""
        else:
            Data = input("By Month(1) / By Category(2) / All(Enter)\nPlease chose a filter option: ")
            
        if Data == "1":
            filter = input("Which month do you want to filter by: ")
            if filter != "":
                print("\nID  |  Date      | Amount | Category      | Description")
                print("-"*75)
                for expense in self.expenses:
                    date_str = expense["createdAt"]  # JSON'dan gelen tarih verisi
                    date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")  # Tarihi parçala
                    month = date_obj.month
                    if month == int(filter):
                        try:
                            totalAmount += expense['amount']
                        except ValueError as e:
                            totalAmount += 0
                        print(f"{expense['id']:3} | {expense['createdAt']} | {expense['amount']:6} | {expense['category']:<13} | {expense['description']}")
                        print("-"*75 + f"\nTotal amount spent: {totalAmount}")
            else:
                print("Error! No month value to filter by.")
                tracker.list_expenses("")
            
        elif Data == "2":
            filter = input("Which category do you want to filter by: ")
            if filter != "":
                print("\nID  |  Date      | Amount | Category      | Description")
                print("-"*75)
                for expense in self.expenses:
                    if expense["category"] == filter:
                        try:
                            totalAmount += expense['amount']
                        except ValueError as e:
                            totalAmount += 0
                        print(f"{expense['id']:3} | {expense['createdAt']} | {expense['amount']:6} | {expense['category']:<13} | {expense['description']}")
                        print("-"*75 + f"\nTotal amount spent: {totalAmount}")
            else:
                print("Error! No category value to filter by.")
                tracker.list_expenses("")
        elif Data == "":
            print("\nID  |  Date      | Amount | Category      | Description")
            print("-"*75)
            for expense in self.expenses:
                try:
                    totalAmount += expense['amount']
                except:
                    totalAmount += 0
                print(f"{expense['id']:3} | {expense['createdAt']} | {expense['amount']:6} | {expense['category']:<13} | {expense['description']}")
            print("-"*75 + f"\nTotal amount spent: {totalAmount}")

    def update_expense(self):
        if not self.expenses:
            os.system("cls")
            print("No expense added yet.")
            return
        
        os.system("cls")
        print("Old List\n" + "-"*75)
        tracker.list_expenses("")
        data = input("Please enter the values to update (id, amount, description, category): ").split(",", maxsplit=3)
        id, amount, description, category = (data + ["", "", ""])[:4] 
        try:
            expense_id = int(id.strip())
            for expense in self.expenses:
                if expense["id"] == expense_id:
                    if description != "":
                        description = description.strip()
                    else:
                        description = expense["description"]
                    if category != "":
                        category = category.strip()
                    else:
                        category = expense["category"]
                    try:
                        if amount != "":
                            if float(amount) > 0.0:
                                amount = float(amount.strip())
                            else:
                                amount = 0.0
                        else:
                            amount = expense["amount"]
                    except ValueError as e:
                            amount = 0.0

                    expense["amount"] = amount
                    expense["description"] = description
                    expense["category"] = category
                    self.save_data()
                    #os.system("cls")
                    print(f"Expense with the ID {expense["id"]} is updated.")
                    print("New List\n" + "-"*75)
                    tracker.list_expenses("")
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
            print("Old List\n" + "-"*75)
            tracker.list_expenses("")
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
                    print("New List\n" + "-"*75)
                    tracker.list_expenses("")
                    return
            os.system("cls")
            print(f"Couldn't find an expense with the ID {id}.")
        except ValueError as e:
            os.system("cls")
            print(f"Please enter a number for the ID. Error: {e}")
    
    def help(self):
        functions = [
            "Add Expense:\n  Adds a new expense entry with an amount, category, and description.\n  Usage: tracker.add_expense(50, 'Lunch', 'Food')\n  Steps:\n    1. Select 'Add(1)' from the main menu.\n    2. Enter 'amount', 'description', and 'category' separated by commas.\n    3. If you want to skip a value, leave it blank and continue.",
            "-"*100,
            "List Expenses:\n  Displays all recorded expenses. If no expenses exist, it informs the user.\n  Usage: tracker.list_expenses()\n  Steps:\n    1. Select 'List(2)' from the main menu.\n    2. The list of expenses will be displayed in order.",
            "-"*100,
            "Update Expense:\n  Modifies an existing expense by its ID. You can update one or multiple fields (amount, category, description).\n  Usage: tracker.update_expense(1, amount=55, description='Fruit shopping', category='Groceries')\n  Steps:\n    1. Select 'Update(3)' from the main menu.\n    2. Enter the ID of the expense you want to update.\n    3. Specify new values (leave blank to keep the old ones).\n    4. Confirm the update.",
            "-"*100,
            "Delete Expense:\n  Removes an expense entry permanently by its ID.\n  Usage: tracker.delete_expense(1)\n  Steps:\n    1. Select 'Delete(4)' from the main menu.\n    2. Enter the ID of the expense you want to delete.\n    3. Confirm deletion.",
        ]
        os.system("cls")
        print("\n".join(functions))

tracker = ExpenseTracker()
i = ""
while i != "0":
    data = input("\nAdd(1) / List(2) / Update(3) / Delete(4) / Help(5) / Exit(0)\nPlease chose what to do: ")
    if data == "1":
        tracker.add_expense()
        
    elif data == "2":
        os.system("cls")
        print("Current List\n" + "-"*75)
        tracker.list_expenses(None)
        
    elif data == "3":
        tracker.update_expense()

    elif data == "4":
        tracker.delete_expense()

    elif data == "5":
        tracker.help()

    elif data == "0":
        i = "0"

    else:
        print(f"Error! Entered an unknown command: '{data}'")
