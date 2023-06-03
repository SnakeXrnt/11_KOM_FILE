import tkinter as tk


from settings import Settings
from page01 import Page01
from page02 import Page02



class MainWindow(tk.Tk):

	def __init__(self, App):
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.app_title)
		self.geometry(self.settings.screen)

		self.create_container()

		self.pages = {}
		self.create_page01()
		self.create_page02()

	def create_container(self):
		self.container = tk.Frame(bg="grey")
		self.container.pack(side="top", fill="both", expand=True)

	def create_page01(self):
		self.pages['page01'] = Page01(self.container, self)

	def create_page02(self):
		self.pages['page02'] = Page02(self.container, self)

	def change_to_page01(self):
		self.settings.usernameVar = self.pages['page02'].nameVar.get()
		self.settings.passwordVar = self.pages['page02'].passwordVar.get()

		print(self.settings.usernameVar, self.settings.username)
		print(self.settings.passwordVar, self.settings.password)


		match = self.settings.usernameVar == self.settings.username and self.settings.passwordVar == self.settings.password
		if match:
			page = self.pages['page01']
			page.tkraise()

	def change_to_page02(self):
		page = self.pages['page02']
		page.tkraise()


class App:

	def __init__(self):
		self.settings = Settings()

		self.main_window = MainWindow(self)

	def run(self):
		self.main_window.mainloop()

if __name__ == '__main__':
	my_app = App()
	my_app.run()