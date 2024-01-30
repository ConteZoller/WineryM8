# app.py
import tkinter as tk
import customtkinter
from sidebar import Sidebar
from content import Vasche, Magazzino

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("WineryM8")
        self.geometry(f"{1100}x{580}")

        # set min size
        self.minsize(800, 480)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = Sidebar(self, on_button_click=self.on_sidebar_button_click)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # create content frame
        self.content_frame = tk.Frame(self)
        self.content_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        # initialize the default content (Vasche)
        self.current_content = Vasche(self.content_frame)
        self.current_content.grid(row=0, column=0, sticky="nsew")

        # bind the window resize event
        self.bind("<Configure>", self.on_resize)

    def on_sidebar_button_click(self, button_number):
        if button_number == 1:
            self.show_content(Vasche)
        elif button_number == 2:
            self.show_content(Magazzino)

    def show_content(self, content_class):
        # Rimuovi tutti i widget dal content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Crea e aggiungi il nuovo widget di contenuto
        self.current_content = content_class(self.content_frame)
        self.current_content.grid(row=0, column=0, sticky="nsew")

        # Aggiorna le dimensioni del Sidebar in base alla nuova larghezza della finestra
        self.sidebar_frame.update_dimensions(self.winfo_width())

    def on_resize(self, event):
        # Aggiorna le dimensioni del Sidebar in base alla nuova larghezza della finestra
        self.sidebar_frame.update_dimensions(event.width)

        # Chiamare il metodo on_configure della classe Content
        if hasattr(self.current_content, "on_configure"):
            self.current_content.on_configure(event)

if __name__ == "__main__":
    app = App()
    app.mainloop()

