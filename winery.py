# winery.py

from tkinter import ttk
from data import read_from_excel

def create_winery_tabview(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tabview #1
    all_tab = "Tutte"
    create_treeview_tab(notebook, all_tab)

    # Tabview #2
    ground_floor_tab = "Terra"
    create_treeview_tab(notebook, ground_floor_tab)

    # Tabview #3
    basement_floor_tab = "Interrato"
    create_treeview_tab(notebook, basement_floor_tab)

    # Tabview #4
    not_empty_tab = "Non vuote"
    create_treeview_tab(notebook, not_empty_tab)

    # Tabview #5
    empty_tab = "Vuote"
    create_treeview_tab(notebook, empty_tab)


def create_treeview_tab(notebook, name):
    # Tab #1
    treeview_tab = ttk.Frame(notebook)
    treeview_tab.columnconfigure(index=0, weight=1)
    treeview_tab.rowconfigure(index=0, weight=1)
    notebook.add(treeview_tab, text=name)

    # Create a Frame for the Treeview
    treeFrame = ttk.Frame(treeview_tab)
    treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

    # Scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    # Treeview
    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2, 3, 4), height=12)
    treeview.pack(expand=True, fill="both")
    treeScroll.config(command=treeview.yview)

    # Treeview columns
    treeview.column("#0", width=0, stretch=False)
    treeview.column(1, anchor="center", width=100, stretch=False)
    treeview.column(2, anchor="center", width=100, stretch=False)
    treeview.column(3, anchor="center", width=200, stretch=False)
    treeview.column(4, anchor="w", stretch=True)  # Ultima colonna che può espandersi

    # Treeview headings
    treeview.heading(1, text="Vasca", anchor="center")
    treeview.heading(2, text="HL", anchor="center")
    treeview.heading(3, text="Tipologia", anchor="center")
    treeview.heading(4, text="Aggiunte", anchor="w")

    treeview_data = create_treeview_data(name)

    # Insert treeview data
    for item in treeview_data:
        treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])

    # Pack the notebook and start the main loop
    notebook.pack(expand=True, fill="both", padx=5, pady=5)


def create_treeview_data(name):
    excel_data = read_from_excel()
    if not excel_data.empty:
        treeview_data = []
        end = "end"
        for row in excel_data.itertuples(index=False):
            pid = "" if row.PID == 0 else str(row.PID)
            if row.VAL != 0:
                if row.ADD != "#0":
                    values = (str(row.VASCA), f"{row.VAL}/{row.CAP}", row.TYPE, str(row.ADD))
                else:
                    values = (str(row.VASCA), f"{row.VAL}/{row.CAP}", row.TYPE, "Nessuna aggiunta")
            else:
                values = (str(row.VASCA), f"{row.VAL}/{row.CAP}", "")

            if name == "Terra" or name == "Interrato":
                if row.LOC == name:
                    treeview_data.append((pid, end, row.VASCA, str(row.VASCA), values))
            elif name == "Non vuote":
                if row.VAL != 0:
                    treeview_data.append((pid, end, row.VASCA, str(row.VASCA), values))
            elif name == "Vuote":
                if row.VAL == 0:
                    treeview_data.append((pid, end, row.VASCA, str(row.VASCA), values))
            else:
                treeview_data.append((pid, end, row.VASCA, str(row.VASCA), values))

        return treeview_data



