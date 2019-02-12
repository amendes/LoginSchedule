from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Login_Page(BoxLayout):
	login_text_input = ObjectProperty()
	psswd_text_input = ObjectProperty()

	def enter_button(self):
		 # Get the student name from the TextInputs
		 user_name = self.login_text_input.text
		 user_psswd = self.psswd_text_input.text

class Login_PageApp(App):
	def build(self):
		return Login_Page()

lpApp = Login_PageApp()
lpApp.run()