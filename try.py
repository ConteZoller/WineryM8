import tkinter as tk

def create_progress_bar(parent, height):
    pb = tk.Canvas(parent, width=20, height=height, bg='white', bd=1, relief='solid')
    pb.create_rectangle(0, 0, 20, height)
    pb.pack(side=tk.LEFT)
    return pb

root = tk.Tk()
root.title("Multiple Progress Bars")

# Altezza totale della ProgressBar
total_height = 200

# Creazione di 5 ProgressBar verticali
progress_bar1 = create_progress_bar(root, total_height)
progress_bar2 = create_progress_bar(root, total_height)
progress_bar3 = create_progress_bar(root, total_height)
progress_bar4 = create_progress_bar(root, total_height)
progress_bar5 = create_progress_bar(root, total_height)

# Aggiornamento delle ProgressBar con dei valori fittizi (puoi collegarle a una variabile di stato per avere un controllo dinamico)
progress_bar1.create_rectangle(0, 0, 20, total_height * 0.2, fill='blue')
progress_bar2.create_rectangle(0, 0, 20, total_height * 0.4, fill='green')
progress_bar3.create_rectangle(0, 0, 20, total_height * 0.6, fill='yellow')
progress_bar4.create_rectangle(0, 0, 20, total_height * 0.8, fill='orange')
progress_bar5.create_rectangle(0, 0, 20, total_height, fill='red')

root.mainloop()
