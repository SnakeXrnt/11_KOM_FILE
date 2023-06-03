class Settings:

	def __init__(self):
		self.app_title = "My App"

		#WINDOW_CONFIG
		base = 100
		w_ratio = 3
		h_ratio = 4
		self.width = w_ratio*base
		self.height = h_ratio*base
		self.screen = f"{self.width}x{self.height}+400+300"


		#USER DATA
		self.username = "admin"
		self.password = "12345"

		#USER INPUT DATA
		self.usernameVar = None
		self.passwordVar = None