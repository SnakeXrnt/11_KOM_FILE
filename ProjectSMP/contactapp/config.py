from json import load, dump


class Config: #settings

	def __init__(self):
		#Settings Apps
		self.active = True

		#Settings General Text
		self.main_menu_txt = 'template/main_menu.txt'
		self.end_msg = 'Press ENTER to Main Menu.'

		self.data_json_path = 'data/data.json'


	def render_template(self, filepath):
		with open(filepath, 'r') as file_txt:
			contents = file_txt.read()
		print(contents)


	def load_data(self, filepath):
		with open(filepath, 'r') as file_json:
			contents = load(file_json)
		return contents


	def save_data(self, data, filepath):
		with open(filepath, 'w') as file_json:
			dump(data, file_json)
