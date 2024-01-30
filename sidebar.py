#sidebar.py

import customtkinter

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, main_app, on_button_click):
        super().__init__(main_app, width=140, corner_radius=0)
        self.main_app = main_app
        self.on_button_click = on_button_click

        #self.grid_rowconfigure(6, weight=1)
        self.logo_label = customtkinter.CTkLabel(self, text="Version 1.0.0 (Beta)", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Aggiungo il numero del pulsante come argomento per identificarlo
        #Pulsante Vasche
        self.sidebar_button_vasche = customtkinter.CTkButton(self, text="Vasche", command=lambda: self.sidebar_button_event(1))
        self.sidebar_button_vasche.grid(row=1, column=0, padx=20, pady=10)

        #Pulsante Magazzino
        self.sidebar_button_magazzino = customtkinter.CTkButton(self, text="Magazzino", command=lambda: self.sidebar_button_event(2))
        self.sidebar_button_magazzino.grid(row=2, column=0, padx=20, pady=10)

        #Pulsante Feature bloccata
        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Bloccato", state="disabled")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        #Pulsante Feature bloccata
        self.sidebar_button_4 = customtkinter.CTkButton(self, text="Bloccato", state="disabled")
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        #Pulsante Feature bloccata
        self.sidebar_button_5 = customtkinter.CTkButton(self, text="Bloccato", state="disabled")
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)

    def sidebar_button_event(self, button_number: int):
        # Richiamo il callback passando il numero del pulsante
        if self.on_button_click:
            self.on_button_click(button_number)

    def update_dimensions(self, new_width):
        # Implementa il codice per aggiornare le dimensioni del Sidebar
        pass
