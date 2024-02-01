# app.py

import tkinter as tk
from tkinter import ttk
from news import create_patch_notes
from winery import create_winery_tabview
from storage import create_storage_tabview
from tank_management import create_tank_management_tabview

#Da sostituire
from testing import create_testing_tabview


def change_theme():
    current_theme = style.theme_use()
    new_theme = "forest-light" if switch_var.get() else "forest-dark"
    
    if current_theme != new_theme:
        style.theme_use(new_theme)
        root.configure(bg=style.lookup(new_theme, 'background'))
        root.update_idletasks()


def change_content(button_number):
    # CHECK VAR CHECK NAMES
    # Rimuovi il contenuto attuale della seconda colonna
    for widget in pane_1.winfo_children():
        widget.destroy()

    if button_number == 1:
        create_winery_tabview(pane_1)

    elif button_number == 2:
        create_storage_tabview(pane_1)
    
    elif button_number == 3:
        create_tank_management_tabview(pane_1)
    
    elif button_number == 4:
        create_testing_tabview(pane_1)

    elif button_number == 0:
        create_patch_notes(pane_1)

root = tk.Tk()
root.title("WineryM8 - Version 1.0.0 (Beta)")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=0)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Panedwindow
paned = ttk.PanedWindow(root)
paned.grid(row=0, column=1, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=3)

# Set the content to patch notes
change_content(0)

#change theme
switch_var = tk.BooleanVar()

# Create a Frame for the Checkbuttons
check_frame = ttk.LabelFrame(root, text="Menù", padding=(20, 10))
check_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# Accentbutton
vasche_button = ttk.Button(check_frame, text="Cantina", style="Accent.TButton", command=lambda: change_content(1))
vasche_button.grid(row=2, column=0, padx=5, pady=20, sticky="nsew")
# Accentbutton
magazzino_button = ttk.Button(check_frame, text="Magazzino", style="Accent.TButton", command=lambda: change_content(2))
magazzino_button.grid(row=3, column=0, padx=5, pady=20, sticky="nsew")
# Accentbutton
blocked_button_1 = ttk.Button(check_frame, text="Gestione Vasca", style="Accent.TButton", command=lambda: change_content(3))
blocked_button_1.grid(row=4, column=0, padx=5, pady=20, sticky="nsew")
# Accentbutton
blocked_button_2 = ttk.Button(check_frame, text="Testing", style="Accent.TButton", command=lambda: change_content(4))
blocked_button_2.grid(row=5, column=0, padx=5, pady=20, sticky="nsew")

# Switch
theme_switch = ttk.Checkbutton(check_frame, text="Chiaro/Scuro", style="Switch", variable=switch_var, command=change_theme)
theme_switch.grid(row=9, column=0, padx=5, pady=20, sticky="nsew")

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()

