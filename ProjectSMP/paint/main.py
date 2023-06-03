#------------- Links Source ---> https://kivy.org/doc/stable/tutorials/firstwidget.html

# notes :
'''
[1] Tanpa import file lain kivy akan membaca file yang ada di folder yang sama dengan syarat nama file.kv memiliki unsur yang sm dengan class
[2] Contoh : paint.kv dari class PaintApp
[3] kelas main atau PaintApp wajib punya kata App dibelakangnya
[4] Root di paint.kv mengarah ke class Painter(Widget)
[5] return saja = return None
'''

#------------- Import System -------------
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Line

#------------- Set Geometry -------------
WIDTH = 9*40
HEIGHT = 14*40

Config.set('graphics', 'width', f'{WIDTH}')
Config.set('graphics', 'height', f'{HEIGHT}')
Config.write()

#------------- Set Window ----------------
Window.clearcolor = get_color_from_hex('#FFFFFF')

#------------- Painter -------------
class Painter(Widget):

	def __init__(self):
		super().__init__()
		self.line_width = 15

	def set_line_width(self, line_width):
		self.line_width = line_width

	def on_touch_down(self, touch):
		#print(touch.x, touch.y)
		#print(touch)
		#print(get_color_from_hex)
		if Widget.on_touch_down(self, touch):
			return

		with self.canvas:
			Color(*get_color_from_hex("#0080FFFF"))
			#Ellipse(pos=(touch.x, touch.y), size=(30, 30))
			touch.ud['line'] = Line(points=(touch.x, touch.y), width= self.line_width)

	def on_touch_move(self, touch):
		if 'line' in touch.ud:
			touch.ud['line'].points += [touch.x, touch.y]

	def clear_canvas(self):
		saved = self.children[:] #clone in different memory
		self.clear_widgets()
		self.canvas.clear()
		for child in saved:
			self.add_widget(child)

#------------- Paint App -------------
class PaintApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Paint App"

	def build(self):
		return Painter()

#------------- Runner -------------
def main():
	app = PaintApp()
	app.run()

#------------- Trigger -------------
if __name__ == '__main__':
	main()