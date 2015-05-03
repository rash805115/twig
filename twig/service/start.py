import PySide.QtGui as QtGui
import service.globals as global_variables
import dialogs.login
import dialogs.main_window
import sys

application = QtGui.QApplication(sys.argv)
login_dialog = dialogs.login.LoginDialog()

if login_dialog.exec_() == QtGui.QDialog.Accepted:
	main_window = dialogs.main_window.MainWindow()
	global_variables.main_window = main_window
	main_window.show()
	application.exec_()