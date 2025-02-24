import json
import datetime


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

def list(status):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        if status == "":
            filtered_data = data
        else:
            filtered_data = [item for item in data if item["status"] == status]
        
        if not filtered_data:
            print("Couldnt find tasks for this option!")
            return
        
        if filtered_data:
            for item in filtered_data:
                print(f"{item['id']} {item['status']} {item['description']}")

    except (FileNotFoundError, json.JSONDecodeError):
        print("Couldnt find or read JSON file!")

def update(id):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        status_cycle = {"TD": "IP", "IP": "D", "D": "TD"}
        updated = False

        for item in data:
            if item["id"] == id:
                old_status = item["status"]
                item["status"] = status_cycle.get(old_status, "TD")
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

i = ""
while i != "0":
    deger=input("ADD(1) / LIST(2) / UPDATE(3) / DELETE(4) / EXIT(0) \nPlease chose what to do: ")
    if deger == "1":
        desc = input("Please enter the task: ")
        add(desc)
    elif deger == "2":
        filter = str.upper(input("Please chose a filter option.\n ToDO(td) / In Progress(ip)/ Done(d)/ All(Enter): "))
        list(filter)
    elif deger == "3":
        id = int(input("Please enter the task ID: "))
        update(id)
    elif deger == "4":
        id = int(input("Please enter the task ID: "))
        remove(id)
    elif deger == "0":
        i = "0"
    else:
        print(f"Wrong input: '{deger}'.Please enter a correct input.")
