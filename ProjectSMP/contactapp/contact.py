from os import system


class Contact:

	def __init__(self, config):
		self.config = config
		self.contact_list = self.config.load_data(self.config.data_json_path)

	def update_contact_name(self, name):
		# system('clear')
		print(f'Old Name \t:{name}')
		new_name = input(f'New name \t:')
		confirm = input('Are you sure to update ? (y/n) ')
		if confirm.lower() == 'y':
			self.contact_list[new_name] = self.contact_list[name]
			del self.contact_list[name]
			self.config.save_data(self.contact_list, self.config.data_json_path)
			print('Contact Updated.')
		else:
			print('Canceled.')

	def update_contact_phone(self, name):
		print(f'Old Phone \t:{self.contact_list[name]["phone"]}')
		new_phone = input(f'New Phone \t:')
		confirm = input('Are you sure to update ? (y/n) ')
		if confirm.lower() == 'y':
			self.contact_list[name]['phone'] = new_phone
			self.config.save_data(self.contact_list, self.config.data_json_path)
			print('Contact Updated.')
		else:
			print('Canceled.')

	def update_contact(self):
		# system('clear')
		print('Update Contact')
		search_contact = input('Name\t:')

		res = self.is_contact_exist(search_contact)
		if res:
			print("1. Name\t2.Phone\t3.Mail\n")
			option = input('Which field do you want to update ? (1/2/3)')
			if option == '1':
				self.update_contact_name(search_contact)
			elif option == '2':
				self.update_contact_phone(search_contact)
			elif option == '3':
				pass
			else:
				pass
		input(self.config.end_msg)


	def is_contact_exist(self, name):
		search_contact = name

		if search_contact in self.contact_list:
			msg = f"Contact Found"
			print(msg)
			print(f"Name\t : {search_contact}")
			print(f"Phone\t : {self.contact_list[search_contact]['phone']}")
			print(f"Mail\t : {self.contact_list[search_contact]['mail']}\n")
			return True
		else:
			msg = f"{search_contact} doesn't exists.\n"
			print(msg)


	def delete_contact(self):
		# system('clear')
		print('Delete Contact')
		search_contact = input('Name\t:')

		res = self.is_contact_exist(search_contact)
		if res:
			confirm = input(f'Are you sure to delete {search_contact} ? (y/n)')
			if confirm.lower() == 'y':
				del self.contact_list[search_contact]
				self.config.save_data(self.contact_list, self.config.data_json_path)
				print('Contact has been deleted.')
			else:
				print('Canceled.')
		input(self.config.end_msg)



	def find_contact(self):
		# system('clear')
		print('Find Contact')
		search_contact = input('Name\t:')

		self.is_contact_exist(search_contact)
		input(self.config.end_msg)


	def show_contact(self):
		# system('clear')
		if len(self.contact_list) > 0:
			print('Name\tPhone\tMail\n')
			for name, data in self.contact_list.items():
				print(f'{name}\t{data["phone"]}\t{data["mail"]}')
		else:
			msg = 'There is no contact yet.'
			print(msg)
		input(self.config.end_msg)

	def create_contact(self):
		# system('clear')
		print('Add New Contact\n')
		name = input('Name\t: ')
		phone = input('Phone\t: ')
		mail = input('Mail\t: ')

		contact = {
			'phone' : phone,
			'mail' : mail
		}

		confirm = input('Are you sure to save ? (y/n)')
		if confirm.lower() == 'y':
			self.contact_list[name] = contact
			self.config.save_data(self.contact_list, self.config.data_json_path)
			print('Contact has been saved.')
		else:
			print('Canceled.')
		input(self.config.end_msg)
