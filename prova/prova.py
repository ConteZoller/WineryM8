import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("WineryM8 - Version 1.0.0 (Beta)")

        # Set the minimum window size
        self.wm_minsize(800, 600)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.pack(expand=True, fill=tk.BOTH)

        self.create_cantina_1()
        self.create_cantina_2()

        # Bind window resize event
        self.bind("<Configure>", self.on_window_resize)

    def create_cantina_1(self):
        tab_one = self.tabview.add("Cantina 1")
        tab_one.grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(tab_one, dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(tab_one, values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(tab_one, text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))

    def create_cantina_2(self):
        tab_two = self.tabview.add("Cantina 2")
        tab_two.grid_columnconfigure(0, weight=1)

        self.label_tab_2 = customtkinter.CTkLabel(tab_two, text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

    def on_window_resize(self, event):
        # Adjust widget sizes or layouts based on window size
        pass

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


if __name__ == "__main__":
    app = App()
    app.geometry("800x600")  # Imposta la dimensione iniziale della finestra
    app.mainloop()
