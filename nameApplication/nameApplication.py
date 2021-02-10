import pandas as pd
import json
from tkinter import *

# converting the JSON data to a pandas df, makes sorting much easier:

f = json.load(open('names.json'))
df = pd.json_normalize(f['names'])

# using Tkinter for the GUI, creating the app here:

root = Tk()
root.title("Name Application")

# creating a text area at the bottom of the window for prints:

tHeight = len(df) + 2
t = Text(root, width=35, borderwidth=5, height=tHeight, wrap=WORD)
t.grid(row=5, column=0, columnspan=3, padx=10, pady=10)


# defining the functions for the program:


def amount_sort(data):
    # sorting the name list by the amount, most popular first
    # I always like to reset the index for ease of reading
    # unless it's necessary to keep the old indexing for some reason
    sorted_df = data.sort_values(by=['amount'], ascending=False).reset_index(drop=True)
    t.delete("1.0", END)
    t.insert("1.0", sorted_df)


def alphabet_sort(data):
    # sorting the name list in alphabetical order
    # again resetting the index for easier reading
    sorted_df = data.sort_values(by=['name']).reset_index(drop=True)
    t.delete("1.0", END)
    t.insert("1.0", sorted_df)


def total_names(data):
    # giving a total of all the names on the list
    total = data['amount'].sum()
    t.delete("1.0", END)
    t.insert("1.0", "The total amount of all names on the list is\n")
    t.insert("2.0", str(total))


def name_amount(name, data):

    if name == "":
        printout = "Please give a name."
    else:
        # Adding simple exception handling in case the searched name is not on the list.
        namedata = data[data['name'] == name]
        if namedata.empty:
            printout = str(name + " is not on the list.")
        else:
            printout = namedata.to_string(index=False)
    t.delete("1.0", END)
    t.insert("1.0", printout)


# defining the buttons:

buttonAmountSort = Button(root, text="List and sort by amount", padx=10, command=lambda: amount_sort(df))
buttonAmountSort.grid(row=0, column=0, columnspan=3)

buttonAlphSort = Button(root, text="List and sort alphabetically", padx=3, command=lambda: alphabet_sort(df))
buttonAlphSort.grid(row=1, column=0, columnspan=3)

buttonTotal = Button(root, text=" Total amount of all names ", command=lambda: total_names(df))
buttonTotal.grid(row=2, column=0, columnspan=3)

labelNameAmount = Label(root, text="To check the amount of a specific name, type the name below.", padx=10)
labelNameAmount.grid(row=3, column=0, columnspan=3)

eNameAmount = Entry(root, width=35, borderwidth=5)
eNameAmount.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

buttonNameAmount = Button(root, text="Check", command=lambda: name_amount(eNameAmount.get(), df))
buttonNameAmount.grid(row=4, column=2)

endLabel = Label(root, text="Emmi Lahtisalo, 2021")
endLabel.grid(row=6, column=0, columnspan=3)

root.mainloop()
