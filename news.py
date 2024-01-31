# news.py

#import tkinter as tk
from tkinter import ttk

def create_patch_notes(pane):
    patch_notes_text = """
    # [Nome dell'App] Patch Notes - Versione X.Y.Z

    ## Novità principali

    1. **Nuova Funzionalità A**
    - Descrizione dettagliata della nuova funzionalità A.
    - Istruzioni su come utilizzare la nuova funzionalità.

    2. **Miglioramenti alla Funzionalità B**
    - Miglioramenti specifici e ottimizzazioni apportate alla funzionalità B.
    - Feedback dagli utenti che ha portato a queste modifiche.

    ## Cambiamenti e Aggiornamenti

    3. **Interfaccia Utente**
    - Modifiche all'interfaccia utente per migliorare la navigazione e l'usabilità.
    - Risoluzione di problemi segnalati dagli utenti relativi all'UI.

    4. **Aggiornamenti delle Librerie di Terze Parti**
    - Aggiornamento a [nome della libreria] versione X.Y.Z per migliorare la stabilità e la sicurezza.
    - Eventuali nuove funzionalità introdotte dalle librerie aggiornate.

    ## Risoluzione di Problemi

    5. **Correzione del Bug C**
    - Descrizione del bug C che è stato risolto.
    - Segnalazioni degli utenti o dei test interni che hanno evidenziato il problema.

    6. **Risoluzione dei Problemi di Prestazioni**
    - Ottimizzazioni delle prestazioni per ridurre i tempi di caricamento o migliorare la reattività dell'app.
    - Dettagli sui test delle prestazioni effettuati e i risultati ottenuti.

    ## Altro

    7. **Note sulla Compatibilità**
    - Informazioni sulla compatibilità con sistemi operativi specifici, hardware o altri requisiti di sistema.
    - Eventuali istruzioni per gli utenti che potrebbero essere influenzati da cambiamenti di compatibilità.

    8. **Note di Sicurezza**
    - Eventuali correzioni di sicurezza apportate in questa versione.
    - Riferimenti a problemi di sicurezza risolti e dettagli su come gli utenti possono proteggersi.

    ## Come Aggiornare

    9. **Istruzioni per l'Aggiornamento**
    - Passaggi dettagliati su come gli utenti possono aggiornare l'app alla versione più recente.
    - Collegamenti diretti ai download o istruzioni integrate nell'app stessa.
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
    label.grid(row=1, column=0, pady=10, columnspan=2)