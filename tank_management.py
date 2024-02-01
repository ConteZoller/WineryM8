# tank_management.py

from tkinter import ttk


"""def create_tank_management_DA_CHECK(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tab #1
    tab_MAGAZZINO = ttk.Frame(notebook)
    tab_MAGAZZINO.columnconfigure(index=0, weight=1)
    tab_MAGAZZINO.rowconfigure(index=0, weight=1)
    notebook.add(tab_MAGAZZINO, text="Visualizzazione")
    notebook.pack(expand=True, fill="both", padx=5, pady=5)"""

def create_tank_management_tab(notebook, name):
    CHECK_NAME_tab = ttk.Frame(notebook)
    CHECK_NAME_tab.columnconfigure(index=0, weight=1)
    CHECK_NAME_tab.rowconfigure(index=0, weight=1)
    notebook.add(CHECK_NAME_tab, text=name)
    notebook.pack(expand=True, fill="both", padx=5, pady=5)
    """# Create a Frame for the Treeview
    CHECK_NAME = ttk.Frame(CHECK_NAME_tab)
    CHECK_NAME.pack(expand=True, fill="both", padx=5, pady=5)"""

def create_tank_management_tabview(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tabview #1
    all_tab = "Tutte"
    create_tank_management_tab(notebook, all_tab)

    # Tabview #2
    ground_floor_tab = "Terra"
    create_tank_management_tab(notebook, ground_floor_tab)

    # Tabview #3
    basement_floor_tab = "Interrato"
    create_tank_management_tab(notebook, basement_floor_tab)

    # Tabview #4
    not_empty_tab = "Non vuote"
    create_tank_management_tab(notebook, not_empty_tab)

    # Tabview #5
    empty_tab = "Vuote"
    create_tank_management_tab(notebook, empty_tab)