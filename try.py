import tkinter as tk
from tkinter import ttk

class VerticalProgressBar(tk.Frame):
    def __init__(self, master=None, thickness=None, length=None, value=None, maximum=None):
        tk.Frame.__init__(self, master, width=thickness, height=length)

        self.canvas = tk.Canvas(self, width=thickness, height=length, bg='white')
        self.canvas.pack()

        self.value = tk.DoubleVar()
        self.maximum = tk.DoubleVar()

        self.maximum.set(maximum if maximum else 100)
        self.value.set(value if value else 0)

        self.draw_progress()

    def draw_progress(self):
        max_val = self.maximum.get()
        val = self.value.get()
        percentage = min(val / max_val, 1.0)

        height = self.canvas.winfo_reqheight() * percentage

        self.canvas.create_rectangle(0, self.canvas.winfo_reqheight() - height, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), fill='green')

    def set_value(self, value):
        self.value.set(value)
        self.draw_progress()

# Esempio di utilizzo
root = tk.Tk()

thickness = 50
length = 200

progress_bar = VerticalProgressBar(root, thickness=thickness, length=length, value=50, maximum=100)
progress_bar.pack(pady=20)

progress = ttk.Progressbar(root, value=0, mode="determinate", orient="vertical")
progress.pack(pady=20)

# Imposta il valore della barra del progresso
progress_bar.set_value(75)

root.mainloop()
