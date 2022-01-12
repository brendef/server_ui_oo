# Libraries 
import npyscreen
import ConfigDatabase
import Control as functions

# Forms
from Forms.FirstForm import FirstForm
from Forms.LastForm import LastForm
from Forms.LoginForm import LoginForm
from Forms.AptSelectForm import AptSelectForm
from Forms.AptInstallForm import AptInstallForm
from Forms.DefaultAptList import DefaultAptList

# ------------------------------------------------------------------------------ #

"""

 (c) TechnoCore - All Rights Reserved.
 NOTICE:  All information contained herein is, and remains
 the property of TechnoCore Automate.

 The intellectual and technical concepts contained
 herein are proprietary to TechnoCore Marketing and
 dissemination of this information or reproduction of this material
 is strictly forbidden unless prior written permission is obtained
 from TechnoCore Automate.

 Author : brendan@technocore.co.za
 Version : Generic
 Implementation :
 Product :
 Package :
 Substrate :
 Status :


 Test SQL :


"""

#------------------------------------------------------------------------------ #

class App(npyscreen.NPSAppManaged):

	def __init__(self):
		super().__init__()

		self.database = ConfigDatabase.ConfigDatabase()
		self.control = functions.Control(self.database)

	def onStart(self):
		self.addForm('MAIN', FirstForm)
		self.addForm('LOGIN', LoginForm, name= "Login", database=self.database)
		self.addForm('APT_SELECT', AptSelectForm, name= "Apt-Get Packages", database=self.database)
		self.addForm('APT_INSTALL', AptInstallForm, name="Installing Apt-Get Packages", database=self.database)
		self.addForm('DEFAULT_APT', DefaultAptList, name="Default Apt Packages")
		# self.addForm('PACKAGE_SELECT', PipSelect, name="Pip/Pip3 Libraries")
		# self.addForm('PACKAGE_INSTALL', PipInstall, name="Installing Pip/Pip3 Libraries")
		# self.addForm('UFW_TOGGLE', FirewallToggleForm, name="UFW Enable/Disable")
		# self.addForm('UFW_CONFIG', FirewallStatusForm, name="UFW Ports Configuration")
		self.addForm('LAST', LastForm)
		
# Main app
App().run()
	