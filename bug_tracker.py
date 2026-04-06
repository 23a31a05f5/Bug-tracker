import json
from datetime import datetime

FILE = "bugs.json"

# Load existing bugs
try:
    with open(FILE, "r") as f:
        bugs = json.load(f)
except:
    bugs = []

def save_bugs():
    with open(FILE, "w") as f:
        json.dump(bugs, f)

def add_bug():
    title = input("Enter bug title: ")
    priority = input("Enter priority (High/Medium/Low): ")
    
    bug = {
        "title": title,
        "status": "Open",
        "priority": priority,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    bugs.append(bug)
    save_bugs()
    print("✅ Bug added!")

def view_bugs():
    if not bugs:
        print("No bugs found")
    else:
        for i, bug in enumerate(bugs):
            print(f"\n{i+1}. {bug['title']}")
            print(f"   Status: {bug['status']}")
            print(f"   Priority: {bug['priority']}")
            print(f"   Created: {bug['time']}")

def update_bug():
    view_bugs()
    num = int(input("Enter bug number to update: "))
    
    if 0 < num <= len(bugs):
        bugs[num-1]["status"] = "Closed"
        save_bugs()
        print("✅ Bug marked as closed")
    else:
        print("Invalid number")

def delete_bug():
    view_bugs()
    num = int(input("Enter bug number to delete: "))
    
    if 0 < num <= len(bugs):
        bugs.pop(num-1)
        save_bugs()
        print("✅ Bug deleted")
    else:
        print("Invalid number")

while True:
    print("\n--- BUG TRACKER ---")
    print("1. Add Bug")
    print("2. View Bugs")
    print("3. Update Bug Status")
    print("4. Delete Bug")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_bug()
    elif choice == "2":
        view_bugs()
    elif choice == "3":
        update_bug()
    elif choice == "4":
        delete_bug()
    elif choice == "5":
        break
    else:
        print("Invalid choice")