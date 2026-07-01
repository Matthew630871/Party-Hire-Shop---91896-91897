import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

#Program constants
FILE_NAME = "hire_records.txt"
RETURNED_FILE = "returned_records.txt"
HIREABLE_ITEMS = ["Marquee Tent", "Plastic Chair", "Trestle Table", "Sound System", "Disco Lights"]
HIRE_CAP = 500

# Data lists
customer_names=[]
receipt_numbers=[]
items_hired=[]
amount_hired=[]

# Helper Functions
def submit():
    """Submit button for Username, receipt number, item hired, amount hired"""
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    receipt = receipt_entry.get().strip()
    item = hired.get()
    amount = hired_num.get().strip()

    # 1. Checking if names are missing
    if not first_name or not last_name:
        messagebox.showwarning("Input Error", "Both First Name and Last Name are required!")
        return

    # 2. Checking if the receipt number is missing or not an integer
    if not receipt:
        messagebox.showwarning("Input Error", "Receipt Number is required")
        return

    try:
        new_num = int(receipt)
    except ValueError:
        messagebox.showerror("Error", "Receipt number must be an integer.")
        return
    if new_num <= 0:
        messagebox.showerror("Error", "Receipt Number must be greater than 0.")
        return

    # 3. Checking if a item was selected from dropdown
    if not item: 
        messagebox.showwarning("Input Error","Please select an item to hire!")
        return

    # 4. Checking if the amount of missing or not a valid positive integer
    if not amount: 
        messagebox.showwarning("Input Error", "Amount Hired is required")
        return
    try:
        new_amount = int(amount)
        if new_amount <= 0:
            messagebox.showerror("Error", "Amount hired must be greater than 0.")
            return
        if new_amount > HIRE_CAP:
            messagebox.showerror("Error", f"Maximum of {HIRE_CAP} items allowed.")
            return
    except ValueError:
        messagebox.showerror("Error", "Amount hired must be a whole number.")
        return

    # 5. If it passes all checks, save the data
    full_name = f"{first_name} {last_name}"

    customer_names.append(full_name)
    receipt_numbers.append(new_num)
    items_hired.append(item)
    amount_hired.append(new_amount)

    messagebox.showinfo("Success", f"Hire record saved successfully for {full_name}")

    file_exists = os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0

    # 6. Saving to a .txt
    with open(FILE_NAME, "a") as file:
        if not file_exists:
            current_date = datetime.now().strftime("%Y-%m-%d")
            file.write(f"=== Julie's Hire System Records ({current_date}) ===\n")
            header = f"{'Customer Name':<20} | {'Item Hired':<15} | {'Amount':<8} | {'Receipt':<10}\n" # Learnt on W3schools
            file.write(header)
            file.write("-" * len(header.strip())+ "\n")

            row = f"{full_name:<20} | {item:<15} | {new_amount:<8} | {new_num:<10}\n"
            file.write(row)
        else: 
            row = f"{full_name:<20} | {item:<15} | {new_amount:<8} | {new_num:<10}\n"
            file.write(row)

    # Code for updating the customer return combobox
    return_name_combo['values'] = customer_names

    # 7. clearing boxes after a seccessful save
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    hired.set('')
    hired_num.delete(0, tk.END)



def returnitem():
    selected_customer = return_name_combo.get()

    if not selected_customer:
        messagebox.showerror("Selection Error", "Please select a customer")
        return
   
    if not os.path.exists(FILE_NAME):
        messagebox.showerror("File Error", "No hire records file found")
        return

    if selected_customer in customer_names: 
       
       index = customer_names.index(selected_customer)
       customer_names.pop(index)
       receipt_numbers.pop(index)
       items_hired.pop(index)
       amount_hired.pop(index)
    else:
        messagebox.showinfo("Info", f"No active hire record found for {selected_customer}")
        return
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    
    updated_lines = []
    record_deleted = False
    
    return_file_exists = os.path.exists(RETURNED_FILE) and os.path.getsize(RETURNED_FILE) > 0 

    for line in lines:
        if selected_customer in line and not record_deleted:
            record_deleted = True
            
            with open(RETURNED_FILE, "a") as retrn_file:
                if not return_file_exists:
                    current_date = datetime.now().strftime("%Y-%m-^%d")
                    retrn_file.write(f"=== Julie's Returned Items Archive ({current_date}) ===\n")
                    header = f"{'Customer Name':<20} | {'Item Hired':<15} | {'Amount':<8} | {'Receipt':<10}\n"
                    retrn_file.write(header)
                    retrn_file.write("-" * len(header.strip()) + "\n")
                    return_file_exists = True

                retrn_file.write(line)
            continue

        updated_lines.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)
    
    return_name_combo['values'] = list(customer_names)

    messagebox.showinfo("Success", f"All item successfully returned. Record for {selected_customer} has been deleted.")
    return_name_combo.set('')

# ---------------------------- TKinter GUI ----------------------------

# ----- Define Tkinter GUI ------
root = tk.Tk()
root.title("Julies Hire system")
root.geometry("460x560")

# Colouring
BG_COLOUR = "#D0E1F9"
root.configure(bg=BG_COLOUR)

# ----- App Title ------
title_label = tk.Label(root, text="Julies Hire system", font=("Arial", 12, "bold"), bg="white", fg="black", bd=1, relief="solid", height=2)
title_label.grid(row=0, columnspan=3, padx=30, pady=(20, 15), sticky="ew")

# ----- Customer label and entry box -----
tk.Label(root, text="Customer Full Name", font=("Arial", 11), bg=BG_COLOUR).grid(row=1, column=0, padx=(20, 10), pady=8, sticky="w")
first_name_entry = tk.Entry(root, width=12)
first_name_entry.grid(row=1, column=1, pady=8, sticky="w")
last_name_entry = tk.Entry(root, width=12)
last_name_entry.grid(row=1, column=2, padx=(0, 20), sticky="w")

# ----- Receipt label and entry box -----
tk.Label(root, text="Receipt Number", font=("Arial", 11), bg=BG_COLOUR).grid(row=2, column=0, padx=(20, 10), pady=8, sticky="w")
receipt_entry = tk.Entry(root, width=27)
receipt_entry.grid(row=2, column=1, columnspan=2, pady=8, sticky="w")

# ----- Item hired label and dropdown box -----
tk.Label(root, text="Item Hired", font=("Arial", 11), bg=BG_COLOUR).grid(row=3, column=0, padx=(20, 10), pady=8, sticky="w")
hired = ttk.Combobox(root, values=HIREABLE_ITEMS, state="readonly", width=25)
hired.grid(row=3, column=1, columnspan=2, pady=8, sticky="w")

# ----- Number Hired label and entry box -----
tk.Label(root, text="Amount Hired", font=("Arial", 11), bg=BG_COLOUR).grid(row=4, column=0, padx=(20, 10), pady=8, sticky="w")
hired_num = tk.Entry(root, width=27)
hired_num.grid(row=4, column=1, columnspan=2, pady=8, sticky="w")

# ----- Submit Button -----
sub_btn = tk.Button(root, text="Submit", font=("Arial", 11, "bold"), bg="#92C47D", fg="black", width=20, command=submit)
sub_btn.grid(row=5, column=0, columnspan=3, pady=15)

# ----- Return items label -----
return_title_label = tk.Label(root, text="Return items here", font=("Arial", 12, "bold"), bg="white", fg="black", bd=1, relief="solid", height=2)
return_title_label.grid(row=6, column=0, columnspan=3, padx=20, pady=15, sticky="ew")

# ----- Customer name label and dropdown box ----- 
tk.Label(root, text="Customer name", font=("Arial", 11), bg=BG_COLOUR).grid(row=7, column=0, padx=(20, 10), pady=8, sticky="w")
return_name_combo = ttk.Combobox(root, values=customer_names, state="readonly", width=25)
return_name_combo.grid(row=7, column=1, columnspan=2, pady=8, sticky="w")

# ----- Return button -----
return_btn = tk.Button(root, text="Return", font=("Arial", 11, "bold"), bg="#92C47D", fg="black", width=20, command=returnitem)
return_btn.grid(row=8, column=0, columnspan=3, pady=15)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()
