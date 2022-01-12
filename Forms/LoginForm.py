import npyscreen

class LoginForm(npyscreen.ActionForm):
	
	# Constructor
	def __init__(self, name=None, parentApp=None, framed=None, help=None, color='FORMDEFAULT', widget_list=None, cycle_widgets=False, database=None,*args, **keywords):
		super().__init__(name=name, parentApp=parentApp, framed=framed, help=help, color=color, widget_list=widget_list, cycle_widgets=cycle_widgets, *args, **keywords)

		# Attributes
		self.OK_BUTTON_TEXT = "Login"
		self.CANCEL_BUTTON_TEXT = "Back"

		self.database = database
		self.pem = 0

	# Methods
	#------------------------------------------------------------------------------ #

	def create(self):

		self.add(npyscreen.TitleText, name="Login to a remote server", editable=False)
		self.host = self.add(npyscreen.TitleText, name="Host:").value = "brendan.technocore.co.za"
		self.user = self.add(npyscreen.TitleText, name="User:").value = "admin"
		self.confirmPem = self.add(npyscreen.TitleText, name="Key: ", editable=False)
		self.add(npyscreen.ButtonPress, name="Add Key", when_pressed_function = self.addKey) 

	#------------------------------------------------------------------------------ #

	def addKey(self):

		self.pem = npyscreen.selectFile()
		self.confirmPem.value = self.pem
		self.confirmPem.display()

	#------------------------------------------------------------------------------ #

	def on_ok(self):
		sql = "SELECT package FROM server_details"
		package = self.database.SqlGetRow(sql)

		if self.pem != 0:
			npyscreen.notify_wait('Logging into {}'.format(self.host), title= 'Connecting...')
			sql = "UPDATE server_details SET local = 1 WHERE local = 0"
			self.database.executeSql(sql)
			sql = "INSERT INTO server_details (host, package, user, pem_address, local) VALUES ('{}','{}','{}','{}',{})".format(self.host.value, package, self.user.value, self.pem, 0)
			self.database.executeSql(sql)
		else:
			sql = "INSERT INTO server_details (host, package, user, pem_address, local) VALUES ('localhost','{}','{}','',1)".format(package, self.user)
			self.database.executeSql(sql)

		# self.parentApp.switchForm('APT_SELECT')
		self.parentApp.switchForm('APT_SELECT')

	#------------------------------------------------------------------------------ #

	def on_cancel(self):
		
		self.parentApp.setNextFormPrevious()

	#------------------------------------------------------------------------------ #