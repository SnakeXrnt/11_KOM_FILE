import tkinter as tk

window = tk.Tk()
window.geometry("800x600+500+500")

frame01 = tk.Frame(window, background="pink", width=10, height=100)
frame01.grid(row=0, column=0, sticky="nsew")

frame02 = tk.Frame(window, background="cyan", width=10, height=100)
frame02.grid(row=0, column=1, sticky="nsew")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=2)

window.grid_rowconfigure(0, weight=1)


window.mainloop()