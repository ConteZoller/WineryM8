# testing.py
import tkinter as tk
from tkinter import ttk


def update_progress(current_value, max_value, progress, percent_label):
    progress["value"] = current_value
    percent_label.config(text=f"{current_value}%")


def create_progress_bar(container_frame, row, column):
    # Creazione della progress bar verticale
    progress = ttk.Progressbar(container_frame, orient="vertical", length=20, mode="determinate", value=0, maximum=100)
    progress.grid(row=row, column=column, sticky="nsew", pady=(0, 0), padx=(0, 1))
    return progress


def create_testing_tab(notebook, name):
    CHECK_NAME_tab = ttk.Frame(notebook)
    CHECK_NAME_tab.columnconfigure(0, weight=1)  # Imposta la colonna 0 per occupare tutto lo spazio disponibile
    CHECK_NAME_tab.rowconfigure(0, weight=1)
    notebook.add(CHECK_NAME_tab, text=name)

    # Creazione del frame contenitore
    container_frame = ttk.Frame(CHECK_NAME_tab)
    container_frame.grid(row=0, column=0, sticky="nsew")

    # Creazione delle progress bar verticali
    progress = create_progress_bar(container_frame, row=0, column=0)
    progress1 = create_progress_bar(container_frame, row=0, column=1)
    progress2 = create_progress_bar(container_frame, row=0, column=2)

    # Nascondi temporaneamente le colonne vuote
    container_frame.grid_columnconfigure(1, weight=1)
    container_frame.grid_columnconfigure(2, weight=1)

    # Etichetta per mostrare la percentuale
    percent_label = tk.Label(CHECK_NAME_tab, text="0%")
    percent_label.grid(row=0, column=0, padx=10, pady=20)

    # Chiamata alla funzione di aggiornamento della progress bar
    update_progress(0, 100, progress, percent_label)

    return CHECK_NAME_tab


def create_testing_tabview(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tabview #1
    all_tab = "Tutte"
    create_testing_tab(notebook, all_tab)

    # Altri tabview possono essere aggiunti qui

    notebook.pack(expand=True, fill="both", padx=5, pady=5)