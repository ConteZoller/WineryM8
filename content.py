# content.py
import tkinter as tk
import customtkinter

class Vasche(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Lista vasche")
        self.label.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

        # Frame interno per utilizzare pack
        self.inner_frame = tk.Frame(self)
        self.inner_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Create tabview
        self.tabview = customtkinter.CTkTabview(self.inner_frame)#, width=1640, height=800)
        self.tabview.pack(expand=True, fill="both")  # Utilizza pack per l'allineamento

        self.tabview.add("Tutti")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
    
        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("Tutti"), width=1600)
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(10):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
    """def open_input_dialog_event(self):
        # Define the behavior when the button is clicked
        pass"""

class Magazzino(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="Magazzino (Bloccato)")
        label.pack(padx=20, pady=20)
        # Aggiungi altri widget o elementi di interfaccia utente necessari
