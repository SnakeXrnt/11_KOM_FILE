import tkinter as tk


from settings import Settings
from page01 import Page01



class MainWindow(tk.Tk):

	def __init__(self, App):
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.app_title)
		self.geometry(self.settings.screen)

		self.create_container()

		self.pages = {}
		self.create_page01()

	def create_container(self):
		self.container = tk.Frame(bg="grey")
		self.container.pack(side="top", fill="both", expand=True)

	def create_page01(self):
		self.pages['page01'] = Page01(self.container, self)


class App:

	def __init__(self):
		self.settings = Settings()

		self.main_window = MainWindow(self)

	def run(self):
		self.main_window.mainloop()

if __name__ == '__main__':
	my_app = App()
	my_app.run()