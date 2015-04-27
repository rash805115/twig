import PySide.QtGui as QtGui
import dialogs.login
import dialogs.main_window
import sys

application = QtGui.QApplication(sys.argv)
login_dialog = dialogs.login.LoginDialog()
main_window = dialogs.main_window.MainWindow()

if login_dialog.exec_() == QtGui.QDialog.Accepted:
	main_window.show()
	application.exec_()