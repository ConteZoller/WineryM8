import tkinter as tk
import customtkinter
from dashboard import Dashboard

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("WineryM8 - Version 1.0.0 (Beta)")
        self.geometry("800x600")

        self.dashboard = Dashboard(self)
        self.dashboard.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    app = App()
    app.mainloop()
