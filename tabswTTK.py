#----tabs----

# Defines and places the notebook widget
nb = ttk.Notebook(window)
nb.grid(row=1, column=0, columnspan=2, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='CSV')
 
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Text')