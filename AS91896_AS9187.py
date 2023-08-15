from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter import ttk

# Commands

def quit(): # Exits the entire GUI
    answer = askyesno(title="Confirm", message="Are you sure you want to quit?")
    if answer: # Confirm Exit
        main_window.destroy()

def submit(): # Submits all enteries into the treeveiw 
    name = entry_name.get()
    receipt = entry_receipt.get()
    item = entry_item.get()
    quantity = entry_quantity.get()
    
    if name and receipt and item and quantity: # Checks if all entry boxes are filled in
        tree.insert("", "end", values=(name, receipt, item, quantity))
        clear_entries()
    else:
        messagebox.showerror("Entry Error", "Please fill out all fields")

def delete(): # Deletes a selected row in the tree view
    selected_item = tree.selection() # Selects Row
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showerror("Error", "Please select a row to delete")

def clear_entries(): # Command to clear entries when submitted 
    entry_name.delete(0,END)
    entry_receipt.delete(0,END)
    entry_item.delete(0,END)
    entry_quantity.delete(0,END)


# Main Window 
main_window = Tk()
main_window.geometry("900x680")
main_window.title("Julie's Party Hire")

tree = ttk.Treeview(main_window, columns=("Name", "Receipt Number", "Item Name", "Quantity"), show="headings")
tree.heading("Name", text="Full Name")
tree.heading("Receipt Number", text="Receipt Number")
tree.heading("Item Name", text="Item Name")
tree.heading("Quantity", text="Quantity of Items")
tree.grid(row=1, column=0, columnspan=2, padx=(30, 30), pady=(20, 20))

label_window = Label(main_window, text="Julie's Party Hire", font="helvetica 35 bold")
label_name = Label(main_window, text="Full Customer Name:")
label_receipt = Label(main_window, text="Receipt Number:")
label_item = Label(main_window, text="Item Name:")
label_quantity = Label(main_window, text="Quantity of Items:")
label_window.grid(row=2, column=0, columnspan=2)

label_name.grid(row=3, column=0, pady=5, padx=20, sticky="e")
label_receipt.grid(row=4, column=0, pady=5, padx=20, sticky="e")
label_item.grid(row=5, column=0, pady=5, padx=20, sticky="e")
label_quantity.grid(row=6, column=0, pady=5, padx=20, sticky="e")

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
btn_quit = Button(main_window, text="Quit", width=6, command=quit)

btn_submit.grid(row=7, column=1, padx=5, pady=10, sticky="w")
btn_delete.grid(row=3, column=1, padx=5, pady=10, sticky="e")
btn_quit.grid(row=8, column=1, padx=5, pady=10, sticky="e")

main_window.mainloop()
