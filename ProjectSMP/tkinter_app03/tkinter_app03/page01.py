import tkinter as tk

class Page01(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg="white", width=self.settings.width, height=self.settings.height)
		# self.pack(fill="both", expand=True)
		self.grid(row=0, column=0, sticky="nsew")

		self.frame01 = tk.Frame(self, bg="#d255d9",height=self.settings.height//3, width=self.settings.width)
		self.frame01.pack(fill="both")

		self.button_to_p2 = tk.Button(self.frame01, text="To Page 2", command=self.app.change_to_page02)
		self.button_to_p2.grid(row=0, column=0, padx=self.settings.width//2.5, pady=self.settings.height//2.5)