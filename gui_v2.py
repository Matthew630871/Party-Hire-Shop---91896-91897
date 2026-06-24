import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Program constants
FILE_NAME = "hire_records.txt"
hireable_items= ["Blank_1","Blank_2","Blank_3"]
Hired_cap = 500

# Data lists
customer_names=[]
receipt_numbers=[]
items_hired=[]
amount_hired=[]

# Helper Functions
def Submit():
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
        if new_amount > Hired_cap:
            messagebox.showerror("Error", f"Maximum of {Hired_cap} items allowed.")
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

    #6. Saving to a .txt
    with open(FILE_NAME, "a") as file:
        file.write(f"{full_name}, Receipt: {new_num}, Item: {item}, Qty: {new_amount}, Status: hired\n")

    # Code for updating the customer return combobox
    return_name_combo['values'] = customer_names

    # Printing out for testing
    print(f"Saved entry: {full_name}, Receipt: {new_num}, Item: {item}, Qty: {new_amount}")
    messagebox.showinfo("Success", f"Hire record saved successfully for {full_name}")
    
    # 7. clearing boxes after a seccessful save 
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)
    hired.set('')
    hired_num.delete(0, tk.END)

def returnitem():
    #Getting the selected customer from the return dropdown
    selected_customer = return_name_combo.get()

    if not selected_customer:
        messagebox.showwarning("Selection Error", "Please select a customer")
        return
    
    if not os.path.exists(FILE_NAME):
        messagebox.showerror("File Error", "No hire records file found")
        return
        
    #1. Reading the file
    with open(FILE_NAME, "r") as file:
        file_content = file.read()

    target_hire = f"{selected_customer}"
    active_hire_marker = ", Status: hired"
    
    # Checking if the customer is recorded 
    if target_hire in file_content and active_hire_marker in file_content:
        updated_content = file_content.replace(active_hire_marker, ", Status:returned")

        with open(FILE_NAME, "w") as file:
            file.write(updated_content)

        messagebox.showinfo("Success", f"items marked as 'returned' for {selected_customer}")
        return_name_combo.set('') 
    else:
        messagebox.showinfo("Info",f"No active hired items found for {selected_customer}")


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
hired = ttk.Combobox(root, values=hireable_items, state="readonly", width=25)
hired.grid(row=3, column=1, columnspan=2, pady=8, sticky="w")

# ----- Number Hired label and entry box -----  $
tk.Label(root, text="Amount Hired", font=("Arial", 11), bg=BG_COLOUR).grid(row=4, column=0, padx=(20, 10), pady=8, sticky="w")
hired_num = tk.Entry(root, width=27)
hired_num.grid(row=4, column=1, columnspan=2, pady=8, sticky="w")

# ----- Submit Button -----  
sub_btn = tk.Button(root, text="Submit", font=("Arial", 11, "bold"), bg="#92C47D", fg="black", width=20, command=Submit)
sub_btn.grid(row=5, column=0, columnspan=3, pady=15)

# ----- Return items label -----  
return_title_label = tk.Label(root, text="Return items here", font=("Arial", 12, "bold"), bg="white", fg="black", bd=1, relief="solid", height=2)
return_title_label.grid(row=6,column=0, columnspan=3, padx=20, pady=15, sticky="ew")

# ----- Customer name label and dropdown box ----- 
tk.Label(root, text="Customer name", font=("Arial", 11), bg=BG_COLOUR).grid(row=7, column=0, padx=(20, 10), pady=8, sticky="w") 
return_name_combo = ttk.Combobox(root, values=customer_names, state="readonly", width=25)
return_name_combo.grid(row=7, column=1, columnspan=2, pady=8, sticky="w")

# ----- Return button ----- 
return_btn = tk.Button(root, text="Return", font=("Arial", 11, "bold"), bg="#92C47D", fg="black", width=20, command=returnitem) #Add Return command here
return_btn.grid(row=8, column=0, columnspan=3, pady=15)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.mainloop()