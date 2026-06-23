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


# ---------------------------- TKinter GUI ---------------------------- 

# ----- Define Tkinter GUI ------ 
root = tk.Tk()
root.title("Julies Hire system")
root.geometry("380x290")

# ----- App Name label ------ 
title = ttk.Label(root, text="Julies Hire system")
 
# ----- App Title ------ 
title_label = ttk.Label(root, text="Julies Hire system", font=("Arial", 20, "bold"))
title_label.grid(row=0, columnspan=3, padx=10, pady=15)

# ----- Customer label and entry box -----  
ttk.Label(root, text="Customer Full Name").grid(row=1, column=0, padx=5, pady=5, sticky="e")

# Frame to hold both name entries in the same grid cell
name_frame = ttk.Frame(root)
name_frame.grid(row=1, column=1, columnspan=2, sticky="w", padx=5)

first_name_entry = ttk.Entry(name_frame, width=10)
first_name_entry.pack(side="left", padx=(0, 5)) 

last_name_entry = ttk.Entry(name_frame, width=10)
last_name_entry.pack(side="left")

# ----- Receipt label and entry box -----  
ttk.Label(root, text="Receipt Number").grid(row=2, column=0,)
receipt_entry = ttk.Entry(root, width=25)
receipt_entry.grid(row=2, column=1)

# ----- Item hired label and dropdown box -----  
ttk.Label(root, text="Item Hired").grid(row=3, column=0)
hired = ttk.Combobox(root, values=hireable_items, state="readonly")
hired.grid(row=3, column=1)

# ----- Number Hired label and entry box -----  
ttk.Label(root, text="Amount Hired").grid(row=4, column=0)
hired_num = ttk.Entry(root, width=25)
hired_num.grid(row=4, column=1)

# ----- Sumbit Button -----  
sub_btn = ttk.Button(root, text="Submit", command=Submit) #Add submit command here
sub_btn.grid(row=5, column=1)

# ----- Return items label -----  
title_label = ttk.Label(root, text="Return items here", font=("Arial", 14, "bold"))
title_label.grid(row=6, columnspan=2, padx=5, pady=5)

# ----- Customer name label and dropdown box ----- 
ttk.Label(root, text="Customer name").grid(row=7, column=0) 
return_name_combo = ttk.Combobox(root, values=customer_names, state="readonly")
return_name_combo.grid(row=7, column=1)

# ----- Return button ----- 
sub_btn = ttk.Button(root, text="Return") #Add Return command here
sub_btn.grid(row=8, column=1,)

root.mainloop()