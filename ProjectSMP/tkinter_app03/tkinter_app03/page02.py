import tkinter as tk

class Page02(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		background_color = "#f1f73e"
		font_page = ("Arial", 25, "bold")
		font_content = ("Arial", 16, "bold")

		super().__init__(parent)
		self.configure(bg="red", width=self.settings.width, height=self.settings.height)
		# self.pack(fill="both", expand=True)
		self.grid(row=0, column=0, sticky="nsew")

		self.frame01 = tk.Frame(self, bg=background_color,height=self.settings.height//3, width=self.settings.width)
		self.frame01.pack(fill="both", expand=True)

		self.textTitle = tk.Label(self.frame01, text="Application Login Page", font=font_page, bg=background_color)
		self.textTitle.grid(columnspan=2, sticky="nsew")

		self.nameLabel = tk.Label(self.frame01, text="Username :", font=font_content, bg=background_color)
		self.nameLabel.grid(row=1, column=0, sticky="e")

		self.nameVar = tk.StringVar()
		self.nameEntry = tk.Entry(self.frame01, bg=background_color, font=font_content, textvariable=self.nameVar)
		self.nameEntry.grid(row=1, column=1, sticky="w")
		

		self.passwordLabel = tk.Label(self.frame01, text="Password :", font=font_content, bg=background_color)
		self.passwordLabel.grid(row=2, column=0, sticky="e")

		self.passwordVar = tk.StringVar()
		self.passwordEntry = tk.Entry(self.frame01, bg=background_color, font=font_content, show="*", textvariable=self.passwordVar)
		self.passwordEntry.grid(row=2, column=1, sticky="w")


		self.button_to_p1 = tk.Button(self.frame01, text="Login", command=self.app.change_to_page01, bg=background_color, font=font_content)
		self.button_to_p1.grid(columnspan=2, sticky="nsew")

