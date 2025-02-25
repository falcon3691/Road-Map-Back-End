import json
import datetime
import shlex

file_name = "data.json"

def add(description):
    new_data = {
        "description": description,
        "status": "TD",
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        if data:
            max_id = max(item["id"] for item in data)
            new_data["id"] = max_id + 1
        else:
            data = []
            new_data["id"] = 1
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        new_data["id"] = 1
    data.append(new_data)
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"New task added. ID: {new_data['id']}")

def list_tasks(status="all"):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        filtered_data = data if status == "all" else [item for item in data if item["status"] == status]
        
        if not filtered_data:
            print("Couldnt find tasks for this option!")
            return

        for item in filtered_data:
            print(f"{item['id']} {item['status']} {item['description']}")

    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldnt find or read JSON file!")

def updateTask(id):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        status_cycle = {"TD": "IP", "IP": "D", "D": "TD"}
        updated = False

        for item in data:
            if item["id"] == id:
                old_status = item["status"]
                item["status"] = status_cycle.get(old_status, "TD")
                item["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                updated = True
                break

        if not updated:
            print("Couldnt find a task with this ID!")
            return

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Task with ID {id} status updated successfully!")

    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldnt find or read JSON file!")

def update(id,desc):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            if item["id"] == int(id):
                item["description"] = desc
                item["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                updated = True
                break

        if not updated:
            print("Couldnt find a task with this ID!")
            return

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Task with ID {id} updated successfully!")

    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldnt find or read JSON file!")

def remove(id):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        filtered_data = [item for item in data if item["id"] != id]

        if len(filtered_data) == len(data):
            print("Couldnt find a task with this ID!")
            return

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(filtered_data, file, indent=4)

        print(f"Task with ID {id} deleted successfully!")

    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldnt find or read JSON file!")

# Komutları çalıştırma bölümü
def main():
    commands = {
        "add": add,
        "list": list,
        "update": update,
        "updateTask": updateTask,
        "remove": remove,
        "exit": exit
    }

    while True:
        user_input = input("Enter command: ").strip()
        
        if not user_input:
            continue
        
        parts = shlex.split(user_input)  # Boşlukları ve tırnakları doğru işler

        command = parts[0].lower()
        params = parts[1:] if len(parts) > 1 else []

        if command in commands:
            try:
                if command == "update" and len(params) == 2:
                    params[0] = int(params[0])  # ID'yi tam sayı yap
                commands[command](*params)  # Tüm parametreleri fonksiyona geçir
            except TypeError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Error: ID must be a number!")
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
