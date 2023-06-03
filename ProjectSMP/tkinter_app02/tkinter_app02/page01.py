import tkinter as tk

class Page01(tk.Frame):

	def __init__(self, parent, App):
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg="white")
		self.pack(fill="both", expand=True)


		self.create_frame01()
		self.create_frame02()
		self.create_frame03()
		self.create_frame04()
		self.create_frame05()
		self.create_frame06()
		

	def create_frame01(self):
		frame01 = tk.Frame(self, bg="red", height=(self.settings.height//4))
		frame01.pack(side="top", fill="x")

	def create_frame02(self):
		self.frame02 = tk.Frame(self, bg="grey")
		self.frame02.pack(fill="both", expand=True)

	def create_frame03(self):
		frame03 = tk.Frame(self.frame02, bg="green", width=(self.settings.width//3))
		frame03.pack(side="left", fill="y")


	def create_frame04(self):
		self.frame04 = tk.Frame(self.frame02, bg="yellow", width=(self.settings.width//3))
		self.frame04.pack(side="right", fill="y")


	def create_frame05(self):
		frame05 = tk.Frame(self.frame04, bg="blue", height=(self.settings.height//4), width=(self.settings.width//3))
		frame05.pack(side="bottom")

	def create_frame06(self):
		frame06 = tk.Frame(self.frame04, bg="purple", height=(self.settings.height//4), width=(self.settings.width//3))
		frame06.pack(side="top")