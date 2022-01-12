import npyscreen

class AptInstallForm(npyscreen.ActionForm):
	
	# Constructor
	def __init__(self, name=None, parentApp=None, framed=None, help=None, color='FORMDEFAULT', widget_list=None, cycle_widgets=False, database=None,*args, **keywords):
		super().__init__(name=name, parentApp=parentApp, framed=framed, help=help, color=color, widget_list=widget_list, cycle_widgets=cycle_widgets, *args, **keywords)
		
		# Attributes
		self.OK_BUTTON_TEXT = "Next"
		self.CANCEL_BUTTON_TEXT = "Back"

		self.database = database

		self.done = "0"
	
	def create(self):
		self.install = self.add(npyscreen.ButtonPress, name="Start Installation", when_pressed_function = self.installPackages)
		self.nextrely += 1
		self.title = self.add(npyscreen.Textfield, value="", editable=False)
		self.nextrely += 1
		self.loadingBar = self.add(npyscreen.Slider, editable=False)
		self.nextrely += 1

	def installPackages(self):
		self.install.hidden = True
		self.title.value = "Starting Installation"
		self.title.display()
		self.install.display()
		totalAptPackages = self.database.get_total_apt_packages()[0]
		loadPercentage = (1 / totalAptPackages) * 100

		for position, apt_package in enumerate(self.database.get_apt_packages()):
			self.title.value = "Installing {} ({} of {})".format(apt_package[0], position + 1, totalAptPackages)
			# f.apt_install(apt_package[0])
			self.loadingBar.value += int(loadPercentage)
			self.title.display()
			self.loadingBar.display()
		self.done = 1
		self.database.install_all_apt_packages()
		npyscreen.notify_confirm("APT-GET Packages installed")
		self.parentApp.switchForm('PACKAGE_SELECT') 
		
	def on_ok(self):
		if self.done == 1:
			self.parentApp.switchForm('PACKAGE_SELECT') 

	def on_cancel(self):
		if self.done == 1:
			self.parentApp.setNextFormPrevious()
	
