# storage.py

from tkinter import ttk

def create_storage_tabview(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tab #1
    tab_MAGAZZINO = ttk.Frame(notebook)
    tab_MAGAZZINO.columnconfigure(index=0, weight=1)
    tab_MAGAZZINO.rowconfigure(index=0, weight=1)
    notebook.add(tab_MAGAZZINO, text="Bloccato")
    notebook.pack(expand=True, fill="both", padx=5, pady=5)