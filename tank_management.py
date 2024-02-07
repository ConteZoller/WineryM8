# tank_management.py

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import pandas as pd
import tkinter.simpledialog
from data import *


def invert_text_widget_colors(text_widget):
    current_bg = text_widget.cget("bg")
    current_fg = text_widget.cget("fg")

    # Inverti i colori
    new_bg = current_fg
    new_fg = current_bg

    # Imposta i nuovi colori
    text_widget.configure(bg=new_bg, fg=new_fg)

def empty_tank(progress_bars, tank_id, tank_frame_label, label_widget):
    def decrement_progress(progress, target_value, decrement_amount=1):
        current_value = progress["value"]
        new_value = max(current_value - decrement_amount, target_value)
        progress["value"] = new_value
        if new_value > target_value:
            progress.after(1, decrement_progress, progress, target_value, decrement_amount)  # Chiamata ricorsiva dopo 10 millisecondi
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    # Calcola il valore di destinazione (0) per tutte le barre di avanzamento
    target_value = 0

    # Calcola l'incremento proporzionale alla capacità rimanente per tutte le barre di avanzamento
    decrement_per_progress = tank_current_level / sum(progress["maximum"] for progress in progress_bars)

    # Decrementa gradualmente tutte le barre di avanzamento
    for progress in progress_bars:
        decrement_progress(progress, target_value, decrement_amount=decrement_per_progress * 2) 

    # Aggiorna i dati nel DataFrame excel_data con il nuovo livello del serbatoio
    update_tank(tank_id, new_current_level=0)

    # Aggiorna il testo nel ttk.LabelFrame
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    tank_total_capacity = tank_data['CAP'].values[0]
    tank_fill_percentage = calculate_fill_percentage(tank_current_level, tank_total_capacity)
    tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

    # Aggiorna il testo nel ttk.Label
    label_widget["text"] = f"{tank_current_level} / {tank_total_capacity} HL"
    tank_frame_label.update_idletasks()
    label_widget.update_idletasks()


def fill_tank(progress_bars, total_capacity, tank_id, tank_frame_label, label_widget):
    def increment_progress(progress, target_value, current_value, increment_amount=1):
        new_value = min(current_value + increment_amount, target_value)
        progress["value"] = new_value
        if current_value < new_value:
            progress.after(10, increment_progress, progress, target_value, new_value, increment_amount)

    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    max_addition = total_capacity - tank_current_level

    user_input = tkinter.simpledialog.askinteger(f"Riempi la Vasca {tank_id}", f"Inserisci un valore (massimo {max_addition}):")

    if user_input is not None and 0 <= user_input <= max_addition:
        increment_per_progress = (user_input / (total_capacity - tank_current_level)) * 2

        for progress in progress_bars:
            target_value = min(progress["value"] + user_input, progress["maximum"])
            increment_progress(progress, target_value, progress["value"], increment_amount=increment_per_progress)

        update_tank(tank_id, new_current_level=tank_current_level + user_input)

        tank_data = extract_tank_data(tank_id)
        tank_current_level = tank_data['VAL'].values[0]
        tank_fill_percentage = calculate_fill_percentage(tank_current_level, total_capacity)
        tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

        label_widget["text"] = f"{tank_current_level} / {total_capacity} HL"
        tank_frame_label.update_idletasks()
        label_widget.update_idletasks()


def calculate_fill_percentage(current_level, total_capacity):
    if total_capacity <= 0:
        raise ValueError("The total capacity of the tank must be greater than zero.")
    fill_percentage = (current_level / total_capacity) * 100
    fill_percentage = round(fill_percentage, 2)
    return fill_percentage

def create_tank_view(tank_management_tab, tank_id):
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    tank_total_capacity = tank_data['CAP'].values[0]
    tank_fill_percentage = calculate_fill_percentage(tank_current_level, tank_total_capacity)

    # Create a Frame for the Checkbuttons
    tank_frame = ttk.LabelFrame(tank_management_tab, labelanchor="n", text=f"Livello vasca: {tank_fill_percentage}%", padding=(20, 10))
    tank_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nw")

    tank_frame.columnconfigure(0, weight=1)
    tank_frame.rowconfigure(0, weight=1)

    tank_border = ttk.LabelFrame(tank_frame, labelanchor="n")
    tank_border.grid(row=0, column=0, pady=20, sticky="nesw")

    # Progressbar
    progress_container = ttk.Frame(tank_border)
    progress_container.grid(row=0, column=0)

    # Separator
    separator = ttk.Separator(tank_frame)
    separator.grid(row=1, column=0, pady=5, sticky="ew")

    

    # Label
    label = ttk.Label(tank_frame, text=f"{tank_current_level} / {tank_total_capacity} HL", justify="center")
    label.grid(row=2, column=0, pady=10)


    ############################################################
    # Create a Frame for the Checkbuttons

    tank_commands_frame = ttk.Frame(tank_management_tab)
    tank_commands_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="nesw")

    tank_commands_border = ttk.LabelFrame(tank_commands_frame, labelanchor="n", text="commands", padding=(20, 10))
    tank_commands_border.grid(row=0, column=0, pady=20, sticky="nesw")

    empty_button = ttk.Button(tank_commands_border, text="Svuota Tank", command=lambda: empty_tank(progress_bars, tank_id, tank_frame, label))
    empty_button.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
    
    fill_button = ttk.Button(tank_commands_border, text="Riempi Tank", command=lambda: fill_tank(progress_bars, tank_total_capacity, tank_id, tank_frame, label))
    fill_button.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")

    items_commands_border = ttk.LabelFrame(tank_commands_frame, labelanchor="n", text="commands", padding=(20, 10))
    items_commands_border.grid(row=1, column=0, pady=20, sticky="nesw")
    invert_color_button = ttk.Button(items_commands_border, text="cambia", command=lambda: invert_text_widget_colors(entry))
    invert_color_button.grid(row=0, column=0,  padx=10,pady=10, sticky="nesw")
    
    ############################################################
    # Create a Frame for the Checkbuttons
    items_frame = ttk.LabelFrame(tank_management_tab, labelanchor="n", text=f"Aggiunte", padding=(20, 10))
    items_frame.grid(row=0, column=2, padx=(20, 10), pady=(20, 10), sticky="nesw")

    items_frame.columnconfigure(0, weight=1)
    items_frame.rowconfigure(0, weight=1)

    # Entry
    entry = scrolledtext.ScrolledText(items_frame)
    items = tank_data['ADD'].values[0]
    for item in items:
        entry.insert("end", item)
    entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="news")

    progress_bars = []
    for i in range(29):
        progress = ttk.Progressbar(progress_container, value=tank_current_level, mode="determinate", orient="vertical", length=500, maximum=tank_total_capacity)
        progress.grid(row=0, column=i)
        progress_bars.append(progress)



def create_tank_management_tab(notebook, tank_id):
    tank_management_tab = ttk.Frame(notebook)
    tank_management_tab.columnconfigure(0, weight=1)
    tank_management_tab.rowconfigure(0, weight=1)
    tank_management_tab.columnconfigure(1, weight=1)
    tank_management_tab.rowconfigure(1, weight=1)
    notebook.add(tank_management_tab, text=f"Vasca {tank_id}")

    create_tank_view(tank_management_tab, tank_id)


    notebook.pack(expand=True, fill="both", padx=5, pady=5)

def create_tank_management_tabview(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tabview #1
    tank_id = 4
    create_tank_management_tab(notebook, tank_id)
