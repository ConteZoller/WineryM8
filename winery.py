# winery.py

from tkinter import ttk

import pandas as pd

file_path = "vasche.xlsx"
def create_treeview_data_from_xls(file_path):
    try:
        # Leggi i dati dal file XLS utilizzando pandas
        df = pd.read_excel(file_path)
        # Inizializza la lista treeview_data
        treeview_data = []
        id = 100

        # Itera sul DataFrame e aggiungi le righe alla lista
        for index, row in df.iterrows():
            if row['PID'] == 0:
                pid = ""
            else:
                pid = row['PID']

            id = id + 1

            #(1, "end", 4, "Child", ("Subitem 1.3", "Value 1.3")),
            if row['VAL'] != 0:
                # Vasca parent
                treeview_data.append((
                    pid,                                            #Parent ID
                    str(row['END']),                                       #end
                    row['ID'],                                            #ID
                    str(row['VASCA']),                                       #Nome
                    (f"{row['VAL']}/{row['CAP']}", row['TYPE'], row['ADD'])
                ))
            else:
                treeview_data.append((
                    pid,                                            #Parent ID
                    str(row['END']),                                       #end
                    row['ID'],                                            #ID
                    str(row['VASCA']),                                       #Nome
                    (f"{row['VAL']}/{row['CAP']}", "")
                ))

        return treeview_data

    except Exception as e:
        print(f"Errore durante la lettura del file XLS: {e}")
        return None

# Funzione per ordinare la treeview
    def sort_treeview(treeview, col, reverse):
        data = [(treeview.set(child, col), child) for child in treeview.get_children('')]
        data.sort(reverse=reverse)
        for i, item in enumerate(data):
            treeview.move(item[1], '', i)
        treeview.heading(col, command=lambda: sort_treeview(treeview, col, not reverse))

def create_winery_tabview(pane):
    # Notebook
    notebook = ttk.Notebook(pane)

    # Tab #1
    tab_tutti = ttk.Frame(notebook)
    tab_tutti.columnconfigure(index=0, weight=1)
    tab_tutti.rowconfigure(index=0, weight=1)
    notebook.add(tab_tutti, text="Tutti")

    # Create a Frame for the Treeview
    treeFrame = ttk.Frame(tab_tutti)
    treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

    # Scrollbar
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    # Treeview
    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2, 3), height=12)
    treeview.pack(expand=True, fill="both")
    treeScroll.config(command=treeview.yview)

    # Treeview columns
    treeview.column("#0", width=100, stretch=False)
    treeview.column(1, anchor="center", width=100, stretch=False)
    treeview.column(2, anchor="center", width=200, stretch=False)
    treeview.column(3, anchor="w", stretch=True)  # Ultima colonna che può espandersi

    # Treeview headings
    treeview.heading("#0", text="Vasca")
    treeview.heading(1, text="HL", anchor="center")
    treeview.heading(2, text="Tipologia", anchor="center")
    treeview.heading(3, text="Aggiunte", anchor="center")

    treeview_data = create_treeview_data_from_xls(file_path)

    # Insert treeview data
    for item in treeview_data:
        treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])

    # Pack the notebook and start the main loop
    notebook.pack(expand=True, fill="both", padx=5, pady=5)

    # Tab #2
    tab_2 = ttk.Frame(notebook)
    notebook.add(tab_2, text="Tab 2")

    # Tabview #3
    tab_3 = ttk.Frame(notebook)
    notebook.add(tab_3, text="Tab 3")

    notebook.pack(expand=True, fill="both", padx=5, pady=5)

