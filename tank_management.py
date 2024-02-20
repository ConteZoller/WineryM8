# tank_management.py

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import pandas as pd
import tkinter.simpledialog
from data import *

def increment_progress(progress, target_value, current_value, increment_amount=1):
        new_value = min(current_value + increment_amount, target_value)
        progress["value"] = new_value
        if current_value < new_value:
            progress.after(10, increment_progress, progress, target_value, new_value, increment_amount)

def decrement_progress(progress, target_value, current_value, decrement_amount=1):
        new_value = max(current_value - decrement_amount, target_value)
        progress["value"] = new_value
        if current_value > new_value:
            progress.after(10, decrement_progress, progress, target_value, new_value, decrement_amount)

     

def increase_font_size(tank_textbox):
    current_size = tank_textbox.cget("font").split(" ")[-1]
    if int(current_size) < 40:
        new_size = int(current_size) + 1  # Incrementa la dimensione del carattere di 2 punti
        tank_textbox.configure(font=("TkDefaultFont", new_size))

def decrease_font_size(tank_textbox):
    current_size = tank_textbox.cget("font").split(" ")[-1]
    if int(current_size) > 11:
        new_size = int(current_size) - 1  # Incrementa la dimensione del carattere di 2 punti
        tank_textbox.configure(font=("TkDefaultFont", new_size))

def invert_text_widget_colors(text_widget):
    current_bg = text_widget.cget("bg")
    current_fg = text_widget.cget("fg")

    # Inverti i colori
    new_bg = current_fg
    new_fg = current_bg

    # Imposta i nuovi colori
    text_widget.configure(bg=new_bg, fg=new_fg)

def decrement_tank(progress_bars, total_capacity, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget):
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]

    if tank_current_level:
        tank_level_user_input = tkinter.simpledialog.askinteger(f"Consuma il Contenuto della Vasca {tank_id}", f"Inserisci un valore (massimo {tank_current_level}):")

        if tank_level_user_input is not None and 0 <= tank_level_user_input <= tank_current_level:
            decrement_per_progress = (tank_level_user_input / tank_current_level) * 2

            for progress in progress_bars:
                target_value = max(progress["value"] - tank_level_user_input, 0)
                decrement_progress(progress, target_value, progress["value"], decrement_amount=decrement_per_progress)

            update_tank(tank_id, new_current_level=tank_current_level - tank_level_user_input)

            tank_data = extract_tank_data(tank_id)
            tank_current_level = tank_data['VAL'].values[0]
            tank_fill_percentage = calculate_fill_percentage(tank_current_level, total_capacity)
            tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

            tank_label_widget["text"] = "{} / {} HL".format(tank_data['VAL'].values[0], tank_data['CAP'].values[0])
            wine_type_label_widget["text"] = tank_data['TYPE'].values[0]

            tank_frame_label.update_idletasks()
            wine_type_label_widget.update_idletasks()
            tank_label_widget.update_idletasks()


def empty_tank(progress_bars, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget, tank_textbox_widget):
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]

    decrement_per_progress = (tank_current_level / progress_bars[0]["maximum"])

    for progress in progress_bars:
        target_value = 0
        decrement_progress(progress, target_value, progress["value"], decrement_amount=decrement_per_progress)

    update_tank(tank_id, new_current_level=0)

    tank_data = extract_tank_data(tank_id)
    tank_fill_percentage = calculate_fill_percentage(0, tank_data['CAP'].values[0])
    tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

    tank_label_widget["text"] = "0 / {} HL".format(tank_data['CAP'].values[0])
    wine_type_label_widget["text"] = ""
    tank_textbox_widget.delete("1.0", tk.END)

    tank_frame_label.update_idletasks()
    tank_label_widget.update_idletasks()
    tank_textbox_widget.update_idletasks()
    wine_type_label_widget.update_idletasks()

def increment_tank(progress_bars, total_capacity, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget):
    wine_type_user_input = None
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    max_addition = total_capacity - tank_current_level
    if max_addition > 0:
        if tank_current_level:
            tank_level_user_input = tkinter.simpledialog.askinteger(f"Riempi la Vasca {tank_id}", f"Inserisci un valore (massimo {max_addition}):")
        else:
            wine_type_user_input = tkinter.simpledialog.askstring(f"Prodotto Vasca {tank_id}", f"Inserisci la tipologia di prodotto:")
            tank_level_user_input = tkinter.simpledialog.askinteger(f"Riempi la Vasca {tank_id}", f"Inserisci un valore (massimo {max_addition}):")

        if tank_level_user_input is not None and 0 <= tank_level_user_input <= max_addition:
            increment_per_progress = (tank_level_user_input / (total_capacity - tank_current_level)) * 2

            for progress in progress_bars:
                target_value = min(progress["value"] + tank_level_user_input, progress["maximum"])
                increment_progress(progress, target_value, progress["value"], increment_amount=increment_per_progress)

            update_tank(tank_id, new_current_level=tank_current_level + tank_level_user_input, wine_type=wine_type_user_input)

            tank_data = extract_tank_data(tank_id)
            tank_current_level = tank_data['VAL'].values[0]
            tank_fill_percentage = calculate_fill_percentage(tank_current_level, total_capacity)
            tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

            tank_label_widget["text"] = "{} / {} HL".format(tank_data['VAL'].values[0], tank_data['CAP'].values[0])
            wine_type_label_widget["text"] = tank_data['TYPE'].values[0]

            tank_frame_label.update_idletasks()
            wine_type_label_widget.update_idletasks()
            tank_label_widget.update_idletasks()

def fill_tank(progress_bars, total_capacity, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget):

    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    max_addition = total_capacity - tank_current_level
    wine_type_user_input = tank_data['TYPE'].values[0]
    if max_addition > 0:
        if not tank_current_level:
            wine_type_user_input = tkinter.simpledialog.askstring(f"Prodotto Vasca {tank_id}", f"Inserisci la tipologia di prodotto:")

        increment_per_progress = (max_addition / (total_capacity - tank_current_level)) * 2

        for progress in progress_bars:
            target_value = min(progress["value"] + max_addition, progress["maximum"])
            increment_progress(progress, target_value, progress["value"], increment_amount=increment_per_progress)

        update_tank(tank_id, new_current_level=tank_current_level + max_addition, wine_type=wine_type_user_input)

        tank_data = extract_tank_data(tank_id)
        tank_current_level = tank_data['VAL'].values[0]
        tank_fill_percentage = calculate_fill_percentage(tank_current_level, total_capacity)
        tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

        tank_label_widget["text"] = "{} / {} HL".format(tank_data['CAP'].values[0], tank_data['CAP'].values[0])
        wine_type_label_widget["text"] = tank_data['TYPE'].values[0]

        tank_frame_label.update_idletasks()
        wine_type_label_widget.update_idletasks()
        tank_label_widget.update_idletasks()


def calculate_fill_percentage(current_level, total_capacity):
    if total_capacity <= 0:
        raise ValueError("The total capacity of the tank must be greater than zero.")
    fill_percentage = (current_level / total_capacity) * 100
    fill_percentage = round(fill_percentage, 2)
    return fill_percentage

def decant_tank(treeview, progress_bars, tank_id, tank_frame_label, tank_label_widget, wine_type_label_widget, tank_textbox_widget):
    from winery import get_selection_values
    selected_values = get_selection_values(treeview)
    decant_tank_id = selected_values[0]

    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    tank_wine_type = tank_data['TYPE'].values[0]
    tank_items = tank_data['ADD'].values[0]
    tank_total_capacity = tank_data['CAP'].values[0]

    target_tank_data = extract_tank_data(decant_tank_id)
    target_tank_capacity = target_tank_data['CAP'].values[0]

    decant_value = min(tank_current_level, target_tank_capacity)

    # Check
    if decant_value:
        decrement_per_progress = (tank_current_level / progress_bars[0]["maximum"])

        for progress in progress_bars:
            target_value = tank_current_level - decant_value
            decrement_progress(progress, target_value, progress["value"], decrement_amount=decrement_per_progress)

        update_tank(tank_id, new_current_level=tank_current_level - decant_value)
        update_tank(decant_tank_id, new_current_level=decant_value, wine_type=tank_wine_type, new_items=tank_items)

        tank_data = extract_tank_data(tank_id)
        tank_current_level = tank_data['VAL'].values[0]
        tank_fill_percentage = calculate_fill_percentage(tank_current_level, tank_total_capacity)
        tank_frame_label["text"] = f"Livello vasca: {tank_fill_percentage}%"

        if tank_current_level:
            tank_label_widget["text"] = "{} / {} HL".format(tank_data['VAL'].values[0], tank_data['CAP'].values[0])
        else:
            tank_label_widget["text"] = "0 / {} HL".format(tank_data['CAP'].values[0])
            wine_type_label_widget["text"] = ""
            tank_textbox_widget.delete("1.0", tk.END)

            tank_textbox_widget.update_idletasks()
            wine_type_label_widget.update_idletasks()

        tank_frame_label.update_idletasks()
        tank_label_widget.update_idletasks()

def show_decant_window(progress_bars, tank_id, tank_frame, tank_label, info_label, tank_textbox):
    from winery import create_treeview_data
    # Crea una nuova finestra Toplevel
    decant_window = tk.Toplevel()
    decant_window.title(f"Travaso - Vasca {tank_id}")

    # Create a Frame for the Treeview
    treeFrame = ttk.Frame(decant_window)
    treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

    # Scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    # Treeview
    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
    treeview.pack(expand=True, fill="both")
    treeScroll.config(command=treeview.yview)

    # Treeview columns
    treeview.column("#0", width=0, stretch=False)
    treeview.column(1, anchor="center", stretch=True)
    treeview.column(2, anchor="center", stretch=True)

    # Treeview headings
    treeview.heading(1, text="Vasca", anchor="center")
    treeview.heading(2, text="HL", anchor="center")

    treeview_data = create_treeview_data("Vuote")

    # Insert treeview data
    for item in treeview_data:
        treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])

    decant_commands_frame = ttk.Frame(decant_window)
    decant_commands_frame.pack(expand=True, fill="both", padx=5, pady=5)

    # Crea il pulsante con il nuovo metodo
    change_decant_button = ttk.Button(decant_commands_frame, text="Travaso", command=lambda: decant_tank(treeview, progress_bars, tank_id, tank_frame, tank_label, info_label, tank_textbox))

    # Posiziona il pulsante al centro senza farlo espandere completamente
    change_decant_button.pack(padx=10, pady=10, side="top", anchor="center")



def create_tank_view(tank_management_tab, tank_id):
    tank_data = extract_tank_data(tank_id)
    tank_current_level = tank_data['VAL'].values[0]
    tank_total_capacity = tank_data['CAP'].values[0]
    tank_wine_type = tank_data['TYPE'].values[0] if tank_data['TYPE'].values[0] != "#0" else ""
    tank_fill_percentage = calculate_fill_percentage(tank_current_level, tank_total_capacity)

    ############################################################
    #                                                          #
    #                           VASCA                          #
    #                                                          #
    ############################################################
    # Create a Frame for the Checkbuttons
    tank_frame = ttk.LabelFrame(tank_management_tab, labelanchor="n", text=f"Livello vasca: {tank_fill_percentage}%", padding=(20, 10))
    tank_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nesw")

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

    progress_bars = []
    for i in range(34):
        progress = ttk.Progressbar(progress_container, value=tank_current_level, mode="determinate", orient="vertical", length=730, maximum=tank_total_capacity)
        progress.grid(row=0, column=i)
        progress_bars.append(progress)

    # Label
    tank_label = ttk.Label(tank_frame, text=f"{tank_current_level} / {tank_total_capacity} HL")
    tank_label.grid(row=2, column=0, pady=10)


    ############################################################
    #                                                          #
    #                          COMANDI                         #
    #                                                          #
    ############################################################
    
    tank_commands_frame = ttk.Frame(tank_management_tab)
    tank_commands_frame.grid(row=0, column=1, padx=(20, 10), pady=(20, 10), sticky="n")

    tank_commands_border = ttk.LabelFrame(tank_commands_frame, labelanchor="n", text="Comandi vasca", padding=(20, 10))
    tank_commands_border.grid(row=0, column=0, sticky="nesw")

    empty_button = ttk.Button(tank_commands_border, text="Svuotamento", command=lambda: empty_tank(progress_bars, tank_id, tank_frame, tank_label, info_label, tank_textbox))
    empty_button.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

    fill_button = ttk.Button(tank_commands_border, text="Riempimento", command=lambda: fill_tank(progress_bars, tank_total_capacity, tank_id, tank_frame, tank_label, info_label))
    fill_button.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")
        
    input_empty_button = ttk.Button(tank_commands_border, text="Togli HL", command=lambda: decrement_tank(progress_bars, tank_total_capacity, tank_id, tank_frame, tank_label, info_label))
    input_empty_button.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")

    input_fill_button = ttk.Button(tank_commands_border, text="Aggiungi HL", command=lambda: increment_tank(progress_bars, tank_total_capacity, tank_id, tank_frame, tank_label, info_label))
    input_fill_button.grid(row=3, column=0, padx=10, pady=10, sticky="nesw")

    decant_button = ttk.Button(tank_commands_border, text="Travaso", command=lambda: show_decant_window(progress_bars, tank_id, tank_frame, tank_label, info_label, tank_textbox))
    decant_button.grid(row=4, column=0, padx=10, pady=10, sticky="nesw")

    blend_button = ttk.Button(tank_commands_border, text="Taglio")
    blend_button.grid(row=5, column=0, padx=10, pady=10, sticky="nesw")


######################### TEXT COMMANDS #########################
    items_commands_border = ttk.LabelFrame(tank_commands_frame, labelanchor="n", text="Comandi testo", padding=(20, 10))
    items_commands_border.grid(row=1, column=0, pady=40, sticky="nesw")

    invert_color_button = ttk.Checkbutton(items_commands_border, text="Chiaro/Scuro", style="ToggleButton", command=lambda: invert_text_widget_colors(tank_textbox))
    invert_color_button.grid(row=0, column=0,  padx=10,pady=10, sticky="nesw")

    increase_font_size_button = ttk.Button(items_commands_border, text="Ingrandisci", command=lambda: increase_font_size(tank_textbox))
    increase_font_size_button.grid(row=1, column=0,  padx=10,pady=10, sticky="nesw")

    decrease_font_size_button = ttk.Button(items_commands_border, text="Diminuisci", command=lambda: decrease_font_size(tank_textbox))
    decrease_font_size_button.grid(row=2, column=0,  padx=10,pady=10, sticky="nesw")

    save_button = ttk.Button(items_commands_border, text="Salva", style="Accent.TButton", command=lambda: update_tank(tank_id, new_items=tank_textbox.get("1.0", tk.END)))
    save_button.grid(row=3, column=0, padx=10, pady=10, sticky="nesw")


######################### INFO FRAME #########################
    info_border = ttk.LabelFrame(tank_commands_frame, labelanchor="n", text="Tipologia", padding=(20, 10))
    info_border.grid(row=2, column=0, pady=100, sticky="nesw")

    #essenziale
    info_border.grid_columnconfigure(0, weight=1)
    info_border.grid_rowconfigure(0, weight=1)
    # Label
    info_label = ttk.Label(info_border, text=tank_wine_type)
    info_label.grid(row=0, column=0, pady=10)
    
    ############################################################
    #                                                          #
    #                         AGGIUNTE                         #
    #                                                          #
    ############################################################
    
    items_frame = ttk.LabelFrame(tank_management_tab, labelanchor="n", text=f"Aggiunte", padding=(20, 10))
    items_frame.grid(row=0, column=2, padx=(20, 10), pady=(20, 10), sticky="nesw")

    #essenziale
    items_frame.columnconfigure(0, weight=1)
    items_frame.rowconfigure(0, weight=1)

    tank_textbox = scrolledtext.ScrolledText(items_frame)
    items = tank_data['ADD'].values[0]
    reformatted_items = reformat_string_to_print(items)
    tank_textbox.insert("end", reformatted_items)
    tank_textbox.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="news")



def create_tank_management_tab(notebook, tank_id):
    tank_management_tab = ttk.Frame(notebook)
    tank_management_tab.columnconfigure(0, weight=1, uniform="columnuniform")
    tank_management_tab.columnconfigure(1, weight=1, uniform="columnuniform")
    tank_management_tab.columnconfigure(2, weight=2, uniform="columnuniform")
    tank_management_tab.rowconfigure(0, weight=1)
    notebook.add(tank_management_tab, text=f"Vasca {tank_id}")

    create_tank_view(tank_management_tab, tank_id)


def create_tank_management_tabview(pane, tank_id):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tabview #1
    create_tank_management_tab(notebook, tank_id)

    notebook.pack(expand=True, fill="both", padx=5, pady=5)