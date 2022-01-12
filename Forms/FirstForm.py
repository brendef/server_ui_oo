import npyscreen

class FirstForm(npyscreen.ActionForm):

	OK_BUTTON_TEXT = "Next"

	# ---------------------------------------------------------------- #

	def create(self):
		self.add(npyscreen.TitleText, name="This is the first screen")

	# ---------------------------------------------------------------- #

	def on_ok(self):
		self.parentApp.switchForm('LOGIN')
	
	# ---------------------------------------------------------------- #