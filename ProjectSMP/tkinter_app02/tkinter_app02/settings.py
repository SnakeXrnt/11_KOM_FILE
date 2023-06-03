class Settings:

	def __init__(self):
		self.app_title = "My App"

		#WINDOW_CONFIG
		base = 30
		w_ratio = 9
		h_ratio = 16
		self.width = w_ratio*base
		self.height = h_ratio*base
		self.screen = f"{self.width}x{self.height}+400+300"