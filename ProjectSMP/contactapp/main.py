
from config import Config
from interface import Interface
from contact import Contact
from user import User


class ContactApp:

	def __init__(self):
		self.config = Config()
		self.contact = Contact(self.config)
		self.interface = Interface(self)
		self.user = User()

	def check_input(self):
		current_input = self.user.current_input.lower()
		if current_input == 'q':
			return False
		elif current_input == '1':
			self.contact.show_contact()
			return True
		elif current_input == '2':
			self.contact.create_contact()
			return True
		elif current_input == '3':
			self.contact.find_contact()
			return True
		elif current_input == '4':
			self.contact.delete_contact()
			return True
		elif current_input == '5':
			self.contact.update_contact()
			return True
		else:
			return True

	def run(self):
		while self.config.active :
			self.interface.main_menu()
			self.user.input_prompt()
			self.config.active = self.check_input()


if __name__ == "__main__":

	my_app = ContactApp()
	my_app.run()