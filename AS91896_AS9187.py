from tkinter import * 
from tkinter import Label
from tkinter import Listbox
from tkinter import messagebox
from tkinter.messagebox import askyesno


# window created 
main_window = Tk()
main_window.geometry("700x680")
main_window.title("Julie's Party Hire")

#created list box for inputs that have been shown
listbox = Listbox(main_window, height=15, width=70)
listbox.grid(row=1, column=0, columnspan=2, padx=(30,30), pady=(20,20)) # listbox dimensions
listbox.insert(END, "           Full Name       |\tReciept Number       |\tItem Name       |\tQuantity")


# commands

#quit - close application
def quit():
    yesno = askyesno(title="confirm", message="Are you sure you want to quit")
    if answer:
        main_window.destroy()

def submit(): # submits all entry boxes to listbox
    name = entry_name.get()
    receipt = entry_receipt.get()
    item = entry_item.get()
    quantity = entry_quantity.get()
    details = f"{name:<5}\t{receipt:<15}\t{item:<25}\t{quantity}" # sorts the entry into coloums
    
    if name and receipt and item and quantity: # checks if all boxes are entered
        details = f"     {name}      {receipt}      {item}      {quantity}"
        listbox.insert(END, details)
    
    if name == "": # Checks if the entry is empty or has a white space
        messagebox.showerror("Full Name Error", "Please enter your full name")

   
                
    

def delete():
    selected_index = listbox.curselection()
    if selected_index:
        index=int(selected_index[0])
        listbox.delete(index)
    else:
        messagebox.showerror("Error", f"Please Select a Row to Delete")  

def clear_entries():
    entry_name.delete(0,END)
    entry_receipt.delete(0,END)
    entry_item.delete(0,END)
    entry_quantity.delete(0,END)

# labels
label_window = Label(main_window, text="Julie's Party Hire", font="helvetica 35 bold")
label_name = Label(main_window, text="Full Customer Name:")
label_receipt = Label(main_window, text="Receipt Number:")
label_item = Label(main_window, text="Item Name:")
label_quantity = Label(main_window, text="Quantity of Items:")
label_window.grid(row=2, column=0, columnspan=2)


# Grid 
label_name.grid(row=3, column=0, pady=5, padx=20, sticky="e")
label_receipt.grid(row=4, column=0, pady=5, padx=20, sticky="e")
label_item.grid(row=5, column=0, pady=5, padx=20, sticky="e")
label_quantity.grid(row=6, column=0, pady=5, padx=20, sticky="e")

# User Entry
entry_name = Entry(main_window)
entry_receipt = Entry(main_window)
entry_item = Entry(main_window)
entry_quantity = Entry(main_window)

entry_name.grid(row=3, column=1, pady=5, padx=5, sticky="w")
entry_receipt.grid(row=4, column=1, pady=5, padx=5, sticky="w")
entry_item.grid(row=5, column=1, pady=5, padx=5, sticky="w")
entry_quantity.grid(row=6, column=1, pady=5, padx=5, sticky="w")

btn_submit = Button(main_window, text="Submit", command=submit)
btn_delete = Button(main_window, text="Delete Selected", command=delete)    
btn_clear = Button(main_window, text="Clear Entries", command=clear_entries)
btn_quit=Button(main_window, text="Quit", width=6, command=quit)

btn_submit.grid(row=7, column=1, padx=5, pady=10, sticky="w")
btn_delete.grid(row=3, column=1, padx=5, pady=10, sticky="e")
btn_clear.grid(row=5, column=1, padx=5, pady=10, sticky="e")
btn_quit.grid(row=8, column=1, padx=5, pady=10, sticky="e")



main_window.mainloop()