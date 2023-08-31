from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from PIL import ImageTk, Image
from tkinter import Label
from tkinter import ttk
import tkinter as tk
import json


# Commands
def save_to_json(data):
    with open("entry_data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_from_json():
    try:
        with open("entry_data.json", "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return []

def quit(): # Exits the entire GUI
    answer = askyesno(title="Confirm", message="Are you sure you want to quit?")
    if answer: # Confirm Exit
        main_window.destroy()

def submit(): # Submits all enteries into the treeveiw 
    name = entry_name.get() # gets entry name
    receipt = entry_receipt.get() # gets entry receipt
    item = entry_item.get() # gets entry item
    quantity = entry_quantity.get() # gets entry quantity 
    
    if name and receipt and item and quantity: # if statment error shown 
        num_in_name = False # Detects if numbers are included in the name 
        for char in name:
            if char.isdigit():
                num_in_name = True
                break

        if num_in_name: # Displays error message for num_in_name
            messagebox.showerror(title="Full Name Error", message="There can only be letters in your name")
        else:
            if not quantity.isdigit(): # Checks for leters in entry box displaing Error
                messagebox.showerror(title="Quantity Error", message="Quantity must be a valid number")
            else:
                quantity_num = int(quantity) 
                if quantity_num < 1 or quantity_num > 500: # Checks if item nnumber is between 1-500
                    messagebox.showerror(title="Quantity Error", message="Quantity must be between 1-500")
                    #displays error message for quantity 
                else:
                    if not receipt.isdigit(): # checks if reciept entry box has digits else prints error
                        messagebox.showerror(title="Receipt Error", message="Your Receipt number can only contain numbers")
                    else:
                        tree.insert("", "end", values=(name, receipt, item, quantity))
                        clear_entries() # When entries submitted clear all enttry boxes 

                        data = load_from_json()
                        data.append({"name": name, "receipt": receipt, "item": item, "quantity": quantity})
                        save_to_json(data) 
    else:
        messagebox.showerror(title="Entry Error", message="Please fill out all fields")

def delete():
    selected_item = tree.selection()  # Get selected items in the Treeview
    if selected_item:
        for item_id in selected_item:
            item_index = tree.index(item_id)
            answer = messagebox.askyesno(message="Do you want to delete this Entry?", title="Delete Confirmation")

            if answer:
                data = load_from_json()  # Load data from the JSON file
                del data[item_index]  # Delete the corresponding item from the data list
                save_to_json(data)  # Save the updated data back to the JSON file
                tree.delete(item_id)  # Delete the selected item from the Treeview
    else:
        messagebox.showerror(title="Error", message="Please select a row to delete")
                           
           
#def delete(): # Deletes a selected row in the tree view
    #selected_item = tree.selection() # Selects Row
    #if selected_item:
        #tree.delete(selected_item) # ensures a row is selected and delettes seleted row
    #else:
        #messagebox.showerror(title="Error", message="Please select a row to delete")

def clear_entries(): # Command to clear entries when submitted 
    entry_name.delete(0,END) # clear name
    entry_receipt.delete(0,END) # clear reciept
    entry_item.delete(0,END) # clear item
    entry_quantity.delete(0,END) # clear quantity

def center_message_box(title, message):
    messagebox = tk.Toplevel(main_window)
    messagebox.title(title)

# Main Window setup
main_window = Tk() 
main_window.geometry("870x600")
main_window.title("Julie's Party Hire")

main_window.configure(bg='#6e758a') # programme background colour


# PIP Image insert
image_path = "/Volumes/PHOENIX/julieparty.png"
original_image = Image.open(image_path)
# Desired size mage
desired_size = (100, 100)
resized_image = original_image.resize(desired_size)
# Convert the resized image to PhotoImage
img1 = ImageTk.PhotoImage(resized_image)
label_image = tk.Label(main_window, image=img1, bg='#6e758a')
label_image.grid(row=2, column=1)

# tree view layout

tree = ttk.Treeview(main_window, columns=("Name", "Receipt Number", "Item Name", "Quantity"), show="headings") # Treeveiw column headlines

# Heading and layout for Tree Veiw
tree.heading("Name", text="Full Name")
tree.heading("Receipt Number", text="Receipt Number")
tree.heading("Item Name", text="Item Name")
tree.heading("Quantity", text="Quantity of Items")
tree.grid(row=1, column=0, columnspan=2, padx=(30, 30), pady=(20, 20)) # Grid placement of Treeview

# Labels For Entry Boxes
label_window = Label(main_window, text="Julie's Party Hire", font="helvetica 35 bold", bg='#6e758a',  fg="white") # # Heading Title
label_name = Label(main_window, text="Full Customer Name :", bg='#6e758a') # name label
label_receipt = Label(main_window, text="Receipt Number :", bg='#6e758a') # receipt label
label_item = Label(main_window, text="Item Name :", bg='#6e758a') # item label
label_quantity = Label(main_window, text="Quantity of Items :", bg='#6e758a') # quantity label 
label_window.grid(row=2, column=0, columnspan=2) 

# Label Grid placement
label_name.grid(row=3, column=0, pady=5, padx=20, sticky="e")
label_receipt.grid(row=4, column=0, pady=5, padx=20, sticky="e")
label_item.grid(row=5, column=0, pady=5, padx=20, sticky="e")
label_quantity.grid(row=6, column=0, pady=5, padx=20, sticky="e")

# Entry boxes for Treeview
entry_name = Entry(main_window)
entry_receipt = Entry(main_window)
entry_item = Entry(main_window)
entry_quantity = Entry(main_window)

# Entry box placement
entry_name.grid(row=3, column=1, pady=5, padx=5, sticky="w")
entry_receipt.grid(row=4, column=1, pady=5, padx=5, sticky="w")
entry_item.grid(row=5, column=1, pady=5, padx=5, sticky="w")
entry_quantity.grid(row=6, column=1, pady=5, padx=5, sticky="w")

# Buttons created
btn_submit = Button(main_window, text="Submit", command=submit, width=6, fg="green")
btn_delete = Button(main_window, text="Delete Selected", command=delete, fg="red")
btn_quit = Button(main_window, text="Quit", command=quit, width=6, bg='#6e758a')

# Button Grid
btn_submit.grid(row=7, column=1, padx=5, pady=10, sticky="w")
btn_delete.grid(row=7, column=0, padx=5, pady=10, sticky="e")
btn_quit.grid(row=8, column=1, padx=5, pady=10, sticky="e")


# Calculate screen width and height
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

# Calculates window position to center it
window_width = 870
window_height = 600
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set window geometry to center of screen
main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Load existing data from the JSON file
existing_data = load_from_json()
for item in existing_data:
    tree.insert("", "end", values=(item["name"], item["receipt"], item["item"], item["quantity"]))

# Main Window Loop
main_window.mainloop()