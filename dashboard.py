import tkinter as tk
from sidebar import Sidebar
from content import Content

class Dashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.sidebar = Sidebar(self, on_button_click=self.show_content)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content = Content(self)
        self.content.grid(row=0, column=1, sticky="nsew")

        self.grid_columnconfigure(1, weight=1)

    def show_content(self, content_name):
        self.content.show_content(content_name)
