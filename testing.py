# testing.py
import tkinter as tk
from tkinter import ttk

# DA SOSTITUIRE
tank_id = 55
tank_level = 34

def create_progress_bar(container_frame, row, column):
    # Creazione della progress bar verticale
    progress = ttk.Progressbar(container_frame, orient="vertical", length=20, mode="determinate", value=0, maximum=100)
    progress.grid(row=row, column=column, sticky="nsew", pady=(0, 0), padx=(0, 1))
    return progress


"""def create_testing_tab(notebook, name):
    CHECK_NAME_tab = ttk.Frame(notebook)
    CHECK_NAME_tab.columnconfigure(0, weight=1)  # Imposta la colonna 0 per occupare tutto lo spazio disponibile
    CHECK_NAME_tab.rowconfigure(0, weight=1)
    notebook.add(CHECK_NAME_tab, text=name)

    # Creazione del frame contenitore
    container_frame = ttk.Frame(CHECK_NAME_tab)
    container_frame.grid(row=0, column=0, sticky="nsew")

    # Progressbar
    progress = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress.grid(row=0, column=1, padx=(0, 50), pady=(5, 200))
    progress1 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress1.grid(row=0, column=1, padx=(0, 65), pady=(5, 200))
    progress2 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress2.grid(row=0, column=1, padx=(0, 80), pady=(5, 200))
    progress3 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress3.grid(row=0, column=1, padx=(0, 95), pady=(5, 200))
    progress4 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress4.grid(row=0, column=1, padx=(0, 110), pady=(5, 200))
    progress5 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress5.grid(row=0, column=1, padx=(0, 125), pady=(5, 200))
    progress6 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress6.grid(row=0, column=1, padx=(0, 140), pady=(5, 200))
    progress7 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress7.grid(row=0, column=1, padx=(0, 155), pady=(5, 200))
    progress8 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress8.grid(row=0, column=1, padx=(0, 170), pady=(5, 200))
    progress9 = ttk.Progressbar(CHECK_NAME_tab, value=70, mode="determinate", orient="vertical")
    progress9.grid(row=0, column=1, padx=(0, 185), pady=(5, 200))
    

    return CHECK_NAME_tab"""
def create_testing_tab(notebook, name):
    CHECK_NAME_tab = ttk.Frame(notebook)
    CHECK_NAME_tab.columnconfigure(0, weight=1)
    CHECK_NAME_tab.rowconfigure(0, weight=1)
    notebook.add(CHECK_NAME_tab, text=name)

    # Creazione del frame contenitore
    container_frame = ttk.Frame(CHECK_NAME_tab)
    container_frame.grid(row=0, column=0, sticky="nsew")

    # Create a Frame for the Checkbuttons
    tank_frame = ttk.LabelFrame(CHECK_NAME_tab, labelanchor="n", text=f"Livello vasca: {tank_level}%", padding=(20, 10))
    tank_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nw")

    # Progressbar
    progress_container = ttk.Frame(tank_frame)
    progress_container.grid(row=0, column=0)

    info_container = ttk.Frame(tank_frame)
    info_container.grid(row=1, column=0)

    # Label
    label = ttk.Label(info_container, text="34%", justify="center")
    label.grid(row=1, column=0, pady=10, columnspan=2)

    # Crea una singola istanza di Progressbar e duplicala
    base_progress = ttk.Progressbar(progress_container, value=70, mode="determinate", orient="vertical", length=200)

    for i in range(15):
        progress = base_progress
        if i > 0:
            # Duplica la progress bar
            progress = ttk.Progressbar(progress_container, value=70, mode="determinate", orient="vertical", length=200)
        progress.grid(row=0, column=i)

    # Imposta la configurazione della colonna per ridurre lo spazio
    progress_container.grid_columnconfigure(0, weight=1)

    return CHECK_NAME_tab




def create_testing_tabview(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tabview #1
    all_tab = "Tutte"
    create_testing_tab(notebook, all_tab)

    # Altri tabview possono essere aggiunti qui

    notebook.pack(expand=True, fill="both", padx=5, pady=5)