import csv
import os
from datetime import datetime
filename = "my_expenses.csv"
fields = ["id", "date", "category", "amount", "note"]
def check_file():
    if not os.path.exists(filename):
        f = open(filename, "w", newline="")
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        f.close()
def get_data():
    check_file()
    data = []
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
def save_to_csv(rows):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
def add_expense():
    data = get_data()
    max_id = 0
    for row in data:
        if int(row["id"]) > max_id:
            max_id = int(row["id"])
    next_id = max_id + 1
    print("Add new")
    d = input("Enter Date:")
    if d == "":
        d = str(datetime.now().date())    
    cat = input("Category: ")
    if cat == "":
        cat = "General"        
    amt = input("Amount: ")
    try:
        amt = float(amt)
    except:
        amt = 0.0
        print("Invalid amount, setting to 0")
    note = input("Note: ")
    new_record = {
        "id": next_id,
        "date": d,
        "category": cat,
        "amount": amt,
        "note": note
    }
    data.append(new_record)
    save_to_csv(data)
    print("Saved")
def view_expenses():
    data = get_data()
    if len(data) == 0:
        print("No records found.")
        return
    print("ID , Date       , Category   , Amount  Note")
    print("-" * 50)
    
    total = 0
    for row in data:
        # manual spacing looks more human than complex formatting
        print(f"{row['id']} , {row['date']} , {row['category']} , {row['amount']} , {row['note']}")
        total = total + float(row['amount'])
        
    print("-" * 50)
    print("Total Expense:", total)
    print()
def delete_item():
    view_expenses()
    target_id = input("Enter ID to delete: ")    
    data = get_data()
    new_data = []
    found = False    
    for row in data:
        if row["id"] != target_id:
            new_data.append(row)
        else:
            found = True            
    if found:
        save_to_csv(new_data)
        print("Deleted")
    else:
        print("ID not found")
def filter_cat():
    cat = input("Enter category name to search: ")
    data = get_data()
    found_any = False    
    print(f"{cat}")
    sum_cat = 0
    for row in data:
        if row["category"].lower() == cat.lower():
            print(f"{row['date']} : {row['amount']} ({row['note']})")
            sum_cat += float(row['amount'])
            found_any = True            
    if not found_any:
        print("Nothing found")
    else:
        print("Total for this category:", sum_cat)
def monthly_sum():
    m = input("Enter Month (): ")
    data = get_data()
    total = 0
    for row in data:
        if m in row["date"]:
            total += float(row["amount"])
    
    print("Total for", m, "is", total)
while True:
    print("1.Add")
    print("2.View All")
    print("3.Delete")
    print("4.Filter")
    print("5.Monthly Total")
    print("6.Exit")
    
    opt = input("Choice: ")
    
    if opt == "1":
        add_expense()
    elif opt == "2":
        view_expenses()
    elif opt == "3":
        delete_item()
    elif opt == "4":
        filter_cat()
    elif opt == "5":
        monthly_sum()
    elif opt == "6":
        print("Bye")
        break
    else:
        print("Wrong input")