# news.py

#import tkinter as tk
from tkinter import ttk


def create_patch_notes(pane):
    patch_notes_text = """
    # WineryM8 - Versione 1.0.0 (Beta) - Patch Notes

    Benvenuto alla prima versione beta di WineryM8! In questa release introdurremo alcune funzionalità chiave per gestire la tua cantina in modo più efficiente.

    ## Novità Principali:

    ### 1. **Cantina:**
    - Aggiunta la visualizzazione dettagliata delle vasche, inclusi i livelli di HL, la tipologia e le aggiunte.
    - Utilizza il pulsante "Vasche" nel menù per accedere a questa funzionalità.

    ### 2. **Magazzino:**
    - Ora è possibile gestire il magazzino con facilità.
    - Accedi alla sezione "Magazzino" attraverso il pulsante corrispondente nel menù.

    ### 3. **Nuove Note sulla Patch:**
    - Introdotta la sezione "Novità" per tener traccia delle modifiche e delle nuove funzionalità.
    - Consulta le patch notes nella scheda "Novità" per rimanere aggiornato sulle ultime novità.

    ## Miglioramenti e Aggiustamenti:

    - Aggiunta l'opzione per passare tra i temi "Chiaro" e "Scuro" nel menù.
    - Ottimizzazioni delle prestazioni e miglioramenti generali.
    """

    notebook = ttk.Notebook(pane)
    # Tab #1
    tab_patch_notes = ttk.Frame(notebook)
    tab_patch_notes.columnconfigure(index=0, weight=1)
    tab_patch_notes.rowconfigure(index=0, weight=1)
    notebook.add(tab_patch_notes, text="Novità")
    notebook.pack(expand=True, fill="both", padx=5, pady=5)

    # Label
    label = ttk.Label(tab_patch_notes, text=patch_notes_text, justify="left")
    label.grid(row=0, column=0, pady=10, columnspan=2, sticky="nsew")