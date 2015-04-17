import dialogs.login
import PySide.QtGui as QtGui
import sys

class LoginWindow(QtGui.QDialog, dialogs.login.Ui_login_dialog):
	def __init__(self, parent = None):
		super(LoginWindow, self).__init__(parent)
		self.setupUi(self)

application = QtGui.QApplication(sys.argv)
login_window = LoginWindow()
login_window.show()
application.exec_()