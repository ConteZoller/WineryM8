# tank_management.py

import tkinter as tk
from tkinter import ttk

def calculate_fill_percentage(current_level, total_capacity):
    if total_capacity <= 0:
        raise ValueError("The total capacity of the tank must be greater than zero.")
    
    fill_percentage = (current_level / total_capacity) * 100
    return fill_percentage

def extract_tank_data(excel_data, tank_id):
    tank_data = excel_data.loc[excel_data['VASCA'] == tank_id]
    return tank_data
        
def create_tank_view(tank_management_tab, tank_fill_percentage, tank_current_level, tank_total_capacity):
        # Create a Frame for the Checkbuttons
        tank_frame = ttk.LabelFrame(tank_management_tab, labelanchor="n", text=f"Livello vasca: {tank_fill_percentage}%", padding=(20, 10))
        tank_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nw")

        tank_border = ttk.LabelFrame(tank_frame, labelanchor="n")
        tank_border.grid(row=0, column=0, pady=20)

        # Progressbar
        progress_container = ttk.Frame(tank_border)
        progress_container.grid(row=0, column=0)

        # Separator
        separator = ttk.Separator(tank_frame)
        separator.grid(row=1, column=0, pady=5, sticky="ew")

        info_container = ttk.Frame(tank_frame)
        info_container.grid(row=2, column=0)

        # Label
        label = ttk.Label(info_container, text=f"{tank_current_level} / {tank_total_capacity} HL", justify="center")
        label.grid(row=2, column=0, pady=10, columnspan=2)

        for i in range(15):
            progress = ttk.Progressbar(progress_container, value=tank_current_level, mode="determinate", orient="vertical", length=200, maximum=tank_total_capacity)
            progress.grid(row=0, column=i)

        # Imposta la configurazione della colonna per ridurre lo spazio
        progress_container.grid_columnconfigure(0, weight=1)

def create_tank_view2(tank_management_tab, tank_fill_percentage, tank_current_level, tank_total_capacity):
    # Create a Frame for the Checkbuttons
    tank_frame = ttk.LabelFrame(tank_management_tab, labelanchor="n", text=f"Livello vasca: {tank_fill_percentage}%", padding=(20, 10))
    tank_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nw")

    tank_border = ttk.LabelFrame(tank_frame, labelanchor="n")
    tank_border.grid(row=0, column=0, pady=20)

    # Progressbar
    progress_container = ttk.Frame(tank_border)
    progress_container.grid(row=0, column=0)

    # Separator
    separator = ttk.Separator(tank_frame)
    separator.grid(row=1, column=0, pady=5, sticky="ew")

    info_container = ttk.Frame(tank_frame)
    info_container.grid(row=2, column=0)

    # Label
    label = ttk.Label(info_container, text=f"{tank_current_level} / {tank_total_capacity} HL", justify="center")
    label.grid(row=2, column=0, pady=10, columnspan=2)

    for i in range(15):
        progress = ttk.Progressbar(progress_container, value=tank_current_level, mode="determinate", orient="vertical", length=200, maximum=tank_total_capacity)
        progress.grid(row=0, column=i)

    # Imposta la configurazione della colonna per ridurre lo spazio
    progress_container.grid_columnconfigure(0, weight=1)

def create_tank_management_tab(notebook, name, excel_data, tank_id):
    tank_management_tab = ttk.Frame(notebook)
    tank_management_tab.columnconfigure(0, weight=1)
    tank_management_tab.rowconfigure(0, weight=1)
    notebook.add(tank_management_tab, text=name)

    # Creazione del frame contenitore
    container_frame = ttk.Frame(tank_management_tab)
    container_frame.grid(row=0, column=0, sticky="nsew")

    tank_data = extract_tank_data(excel_data, tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    tank_total_capacity = tank_data['CAP'].values[0]
    tank_fill_percentage = calculate_fill_percentage(tank_current_level, tank_total_capacity)

    create_tank_view(tank_management_tab, tank_fill_percentage, tank_current_level, tank_total_capacity)
    #create_tank_view2(tank_management_tab, tank_fill_percentage, tank_current_level, tank_total_capacity)

    notebook.pack(expand=True, fill="both", padx=5, pady=5)


def create_tank_management_tabview(pane, excel_data):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tabview #1
    all_tab = "Tutte"
    create_tank_management_tab(notebook, all_tab, excel_data, 4)
