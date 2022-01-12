from os import error
from sqlite3.dbapi2 import Error
import npyscreen

# Local files
import Lists

class AptSelectForm(npyscreen.ActionForm):

	# Constructor
	def __init__(self, name=None, database=None, parentApp=None, framed=None, help=None, color='FORMDEFAULT', widget_list=None, cycle_widgets=False,*args, **keywords):
		self.database = database
		# Set default apt packages
		sql = "SELECT host FROM server_details"
		host = self.database.SqlGetRow(sql)
		sql = "SELECT package FROM server_details"
		package = self.database.SqlGetRow(sql)
		sql = "SELECT user FROM server_details"
		user = self.database.SqlGetRow(sql)

		# Insert packages into database
		for apt_package in Lists.AptList:
			sql = "INSERT INTO apt_list (host, package, user, apt_package, installed) VALUES ('{}','{}','{}','{}', 0)".format(host, package, user, apt_package)
			self.database.executeSql(sql)
		super().__init__(name=name, parentApp=parentApp, framed=framed, help=help, color=color, widget_list=widget_list, cycle_widgets=cycle_widgets, *args, **keywords)
		
		# Attributes
		self.OK_BUTTON_TEXT = "Install"
		self.CANCEL_BUTTON_TEXT = "Back"

		# Set default apt packages
		sql = "SELECT host FROM server_details"
		host = self.database.SqlGetRow(sql)
		sql = "SELECT package FROM server_details"
		package = self.database.SqlGetRow(sql)
		sql = "SELECT user FROM server_details"
		user = self.database.SqlGetRow(sql)

		# Insert packages into database
		for apt_package in Lists.AptList:
			sql = "INSERT INTO apt_list (host, package, user, apt_package, installed) VALUES ('{}','{}','{}','{}', 0)".format(host, package, user, apt_package)
			self.database.executeSql(sql)
			
	# Methods
	#------------------------------------------------------------------------------ #

	def create(self):
		self.add(npyscreen.FixedText, value="The following packages will be installed using apt-get")
		
		self.nextrely += 1

		self.newPackage = self.add(npyscreen.TitleText, name="add:")
		self.add(npyscreen.ButtonPress, name="Add Package", when_pressed_function = self.addPackage) 

		self.nextrely += 1

		self.packages = []

		sql = "SELECT apt_package FROM apt_list"
		for package in self.database.SqlGetRows(sql):
			self.packages.append(package[0])

		self.result = self.add(npyscreen.MultiLine, values=self.packages)

	#------------------------------------------------------------------------------ #

	def addPackage(self):
		# User and system details
		sql = "SELECT host FROM server_details"
		host = self.database.SqlGetRow(sql)
		sql = "SELECT package FROM server_details"
		package = self.database.SqlGetRow(sql)
		sql = "SELECT user FROM server_details"
		user = self.database.SqlGetRow(sql)

		if self.newPackage != '':
			try:
				sql = "INSERT INTO apt_list (host, package, user, apt_package, installed) VALUES ('{}','{}','{}','{}',0)".format(host, package, user, self.newPackage)
				self.database.executeSql(sql)
				self.packages.append(self.newPackage.value)
				self.newPackage.value = ""
			except Error:
				wr = open("log.txt", 'w')
				wr.write()

	def on_ok(self):
		self.parentApp.switchForm('APT_INSTALL')