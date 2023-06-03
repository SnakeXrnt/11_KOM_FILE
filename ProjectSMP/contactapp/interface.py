from os import system


class Interface: #view

	def __init__(self, contactapp):
		self.config = contactapp.config

	def main_menu(self):
		# system('clear')
		self.config.render_template(self.config.main_menu_txt)