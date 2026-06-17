import tkinter as tk
from tkinter import ttk

# Data lists
#Cus_name=[]



# Helper Functions



















# ---------------------------- TKinter GUI ---------------------------- 


# ----- Define Tkinter GUI ------ 
root = tk.Tk()
root.title("TO BE DECIDED")
root.geometry("300x250")

# ----- App Name label ------ 
title = ttk.Label(root, text="TO BE DECIDED")
 
# ----- Customer label and entry box -----  
ttk.Label(root, text="Blank").grid(row=1, column=0,)
name_entry = ttk.Entry(root, width=25)
name_entry.grid(row=1, column=1)

# ----- Receipt label and entry box -----  
ttk.Label(root, text="Blank").grid(row=2, column=0,)
receipt_entry = ttk.Entry(root, width=25)
receipt_entry.grid(row=2, column=1)

# ----- Item hired label and dropdown box -----  
ttk.Label(root, text="Blank").grid(row=3, column=0,)
hired = ttk.Combobox(root, values=["Blank 1","Blank 2","Blank 3"], state="read only")
hired.grid(row=3, column=1)
# ----- Number Hired label and entry box -----  
ttk.Label(root, text="Blank").grid(row=4, column=0,)
hired_num = ttk.Entry(root, width=25)
hired_num.grid(row=4, column=1)

# ----- Sumbit Button -----  
sub_btn = ttk.Button(root, text="Submit") #Add submit command here
sub_btn.grid(row=5, column=1)

# ----- Return items label -----  
ttk.Label(root, text="Blank").grid(row=6, columnspan=2)

# ----- Customer name label and dropdown box ----- 
ttk.Label(root, text="BLank").grid(row=7, column=0) 
name = ttk.Combobox(root, values=["Blank","Blank","Blank"])
name.grid(row=7, column=1)

# ----- Return button ----- 
sub_btn = ttk.Button(root, text="Return") #Add Return command here
sub_btn.grid(row=8, column=1)

root.mainloop()