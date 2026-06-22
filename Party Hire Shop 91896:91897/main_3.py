import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Data lists
customer_names=[]
receipt_numbers=[]

# Helper Functions

def Submit():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    receipt = receipt_entry.get()

    if not first_name or not last_name:
        messagebox.showwarning("Input Error", "Both First Name and Last Name are required!")
    else:
        # Saving the first and last name as one
        full_name = f"{first_name} {last_name}"
        customer_names.append([full_name])
        print(customer_names) # for testing

    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    receipt_entry.delete(0, tk.END)

    try:
        new_num = int(receipt)
        print (new_num)
    except ValueError:
        messagebox.showerror("Error", "Receipt number must be integer.")
    return False








   







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
ttk.Label(root, text="Item Hired").grid(row=3, column=0,)
hired = ttk.Combobox(root, values=["Blank 1","Blank 2","Blank 3"], state="read only")
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
name = ttk.Combobox(root, values=customer_names)
name.grid(row=7, column=1)

# ----- Return button ----- 
sub_btn = ttk.Button(root, text="Return") #Add Return command here
sub_btn.grid(row=8, column=1)

root.mainloop()