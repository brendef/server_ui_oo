import npyscreen

class LastForm(npyscreen.ActionForm):

	OK_BUTTON_TEXT = "Exit"
	CANCEL_BUTTON_TEXT = "Back"

	# ---------------------------------------------------------------- #

	def create(self):
		self.add(npyscreen.TitleText, name="This is the next step in the installer")

	# ---------------------------------------------------------------- #
	
	def on_ok(self):
		self.parentApp.switchForm(None)
	
	# ---------------------------------------------------------------- #

	def on_cancel(self):
		self.parentApp.setNextFormPrevious()

	# ---------------------------------------------------------------- #