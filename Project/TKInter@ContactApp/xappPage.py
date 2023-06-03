import tkinter as tk
from PIL import Image, ImageTk

class AppPage(tk.Frame):

	def __init__(self, parent, App): #self.container, self.app

		self.app = App
		self.settings = App.settings

		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_left_frame()
		self.create_right_frame()
		self.config_left_and_right()


	def create_left_frame(self):
		self.left_frame = tk.Frame(self, bg="white", width=self.settings.width//3)
		self.left_frame.grid(row=0, column=0, sticky="nsew")

		self.create_left_header()
		self.create_left_content()


	def create_right_frame(self):
		self.right_frame = tk.Frame(self, bg="white", width=2*self.settings.width//3)
		self.right_frame.grid(row=0, column=1, sticky="nsew")


		self.create_right_header()
		self.create_right_content()
		self.create_right_footer()

	def config_left_and_right(self):
		self.grid_columnconfigure(0, weight=1) #1/3
		self.grid_columnconfigure(1, weight=2) #2/3

		self.grid_rowconfigure(0, weight=1)


	def create_left_header(self):
		frame_w = self.settings.width//3
		frame_h = self.settings.height//5
		self.left_header = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="black")
		self.left_header.pack()

		self.detail_left_header = tk.Frame(self.left_header, width=frame_w, height=frame_h, bg="black")
		self.detail_left_header.grid(row=0, column=0, sticky="nsew")

		image = Image.open(self.settings.logo)
		iW, iH = image.size
		ratio = iW/frame_w
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		self.logo = ImageTk.PhotoImage(image)

		self.label_logo = tk.Label(self.detail_left_header, image=self.logo)
		self.label_logo.pack(fill="x")

		self.searchBox_frame = tk.Frame(self.detail_left_header, width=frame_w, height=frame_h//4, bg="white")
		self.searchBox_frame.pack(fill="x")

		self.entry_search = tk.Entry(self.searchBox_frame, bg="white", fg="black", font=("Arial", 12))
		self.entry_search.grid(row=0, column=0, sticky="nsew")

		self.button_search = tk.Button(self.searchBox_frame, bg="white", fg="black", font=("Arial", 12), text="Find")
		self.button_search.grid(row=0, column=1, sticky="nsew")


		self.searchBox_frame.grid_columnconfigure(0, weight=3)
		self.searchBox_frame.grid_columnconfigure(1, weight=1)

		self.left_header.grid_rowconfigure(0, weight=1)
		self.left_header.grid_columnconfigure(0, weight=1)

	def create_left_content(self):
		frame_w = self.settings.width//3
		frame_h = 4*self.settings.height//5

		self.left_content = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="white")
		self.left_content.pack(fill="x")


		self.contact_listBox = tk.Listbox(self.left_content, bg="white", fg="black", font=("Arial", 12), height=frame_h)
		self.contact_listBox.pack(side="left", fill="both", expand=True)

		self.contacts_scroll = tk.Scrollbar(self.left_content)
		self.contacts_scroll.pack(side="right", fill="y")

		contacts = self.settings.contacts
		for contact in contacts:
			for phone, info in contact.items():
				full_name = f"{info['f_name']} {info['l_name']}"
				self.contact_listBox.insert("end", full_name)

		self.contact_listBox.configure(yscrollcommand=self.contacts_scroll.set)
		self.contacts_scroll.configure(command=self.contact_listBox.yview)


	def create_right_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5

		self.right_header = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_header.pack(expand=True)

		
		self.detail_header = tk.Frame(self.right_header, width=frame_w, height=frame_h, bg="white")
		self.detail_header.grid(row=0, column=0, sticky= "nsew")

		self.virt_img = tk.PhotoImage(width=1, height=1)
		self.fullName_Label = tk.Label(self.detail_header, text="Anas Azhar", font=("Arial", 26), bg="white", image=self.virt_img, compound="c")
		self.fullName_Label.pack()

		self.right_header.grid_rowconfigure(0, weight=1)
		self.right_header.grid_columnconfigure(0, weight=1)

	def create_right_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4

		self.right_content = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_content.pack(expand=True)

		self.detail_content= tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="white")
		self.detail_content.grid(row=0, column=0, sticky= "nsew")

		self.table_info = []
		info = [
			['Telepon :', '081123456789'],
			['Alamat :', 'Pasar 26 Ilir'],
			['Email :', 'anaszz@mail.com']

		]
		rows, columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				label = tk.Label(self.detail_content, text=info[row][column], font=("Arial", 12), bg="white")
				if column == 0:
					sticky = 'e'
				else:
					sticky = 'w'
				label.grid(row=row, column=column, sticky=sticky)
				aRow.append(label)
			self.table_info.append(aRow)


		self.right_content.grid_rowconfigure(0, weight=1)
		self.right_content.grid_columnconfigure(0, weight=1)

	def create_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4

		self.right_footer = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="white")
		self.right_footer.pack(expand=True)

		self.detail_footer= tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="white")
		self.detail_footer.grid(row=0, column=0, sticky= "nsew")

		features = ['Update', 'Delate', 'Add New']
		self.buttons_feature = []
		for feature in features:
			button = tk.Button(self.detail_footer, text=feature, font=("Arial", 12, 'bold'), bg="white", bd=0)
			button.grid(row=0, column=features.index(feature), sticky="nsew", padx=(0, 20))

		self.right_footer.grid_rowconfigure(0, weight=1)
		self.right_footer.grid_columnconfigure(0, weight=1)





