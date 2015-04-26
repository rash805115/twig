import dialogs.login
import PySide.QtGui as QtGui
import sys

class LoginWindow(QtGui.QDialog, dialogs.login.LoginDialog):
	def __init__(self, parent = None):
		super(LoginWindow, self).__init__(parent)
		self.setup(self)

application = QtGui.QApplication(sys.argv)
login_window = LoginWindow()
login_window.show()
application.exec_()