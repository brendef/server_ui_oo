import npyscreen

# Local files
import Lists

class AptSelectForm(npyscreen.ActionForm):

	allPackages = []

	# Constructor
	def __init__(self, name=None, database=None, parentApp=None, framed=None, help=None, color='FORMDEFAULT', widget_list=None, cycle_widgets=False, *args, **keywords):
		super().__init__(name=name, parentApp=parentApp, framed=framed, help=help, color=color, widget_list=widget_list, cycle_widgets=cycle_widgets, *args, **keywords)

		# Attributes
		self.OK_BUTTON_TEXT = "Install"
		self.CANCEL_BUTTON_TEXT = "Back"

		self.database = database 

		# Set default apt packages
		sql = "SELECT host FROM server_details"
		host = self.database.SqlGetRow(sql)
		sql = "SELECT package FROM server_details"
		self.package = self.database.SqlGetRow(sql)
		sql = "SELECT user FROM server_details"
		self.user = self.database.SqlGetRow(sql)

		# Insert packages into database
		for apt_package in Lists.AptList:
			sql = "INSERT INTO apt_list (host, package, user, apt_package, installed) VALUES ('{}','{}','{}','{}', 0)".format(host, self.package, self.user, apt_package)
			self.database.executeSql(sql)
				
	# Methods
	#------------------------------------------------------------------------------ #

	def create(self):
		
		self.add(npyscreen.FixedText, value="A default list of packages will be installed")
		self.add(npyscreen.ButtonPress, name="Show Default Packages", when_pressed_function = self.showPackages)

		self.nextrely += 1

		self.add(npyscreen.FixedText, value="Add additional packages")
		self.newPackage = self.add(npyscreen.TitleText, name="add:")
		self.add(npyscreen.ButtonPress, name="Add Package", when_pressed_function = self.addPackage) 

	#------------------------------------------------------------------------------ #

	def addPackage(self):
		# User and system details
		sql = "SELECT host FROM server_details"
		self.host = self.database.SqlGetRow(sql)
		sql = "SELECT package FROM server_details"
		self.package = self.database.SqlGetRow(sql)
		sql = "SELECT user FROM server_details"
		self.user = self.database.SqlGetRow(sql)

		if self.newPackage != '':
	
				sql = "INSERT INTO apt_list (host, package, user, apt_package, installed) VALUES ('{}','{}','{}','{}',{})".format(self.host, self.package, self.user, self.newPackage.value, 0)
				self.database.executeSql(sql)
				self.packages.append(self.newPackage.value)
				self.newPackage.value = ""
		

	def showPackages(self):
		self.parentApp.switchForm('DEFAULT_APT')	

	def on_ok(self):
		self.parentApp.switchForm('APT_INSTALL')