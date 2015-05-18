import service.globals as global_variables
import signals.signals as signals
import dialogs.login
import dialogs.main_window
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.user as user
import PySide.QtGui as QtGui
import sys

bookeeping_connection = connection.Connection()
bookeeping_connection.host = global_variables.bookeeping_host
bookeeping_connection.port = global_variables.bookeeping_port
bookeeping_connection.base = global_variables.bookeeping_base
bookeeping_connection.https = global_variables.bookeeping_https
bookeeping_connection.headers = {"Content-Type": "application/json"}
bookeeping_connection.timeout = 30

global_variables.bookeeping_connection = bookeeping_connection
global_variables.twig_signal = signals.TwigSignals()

application = QtGui.QApplication(sys.argv)
login_dialog = dialogs.login.LoginDialog()

if login_dialog.exec_() == QtGui.QDialog.Accepted:
	user_obj = user.User(global_variables.bookeeping_connection)
	getuser_status, _ = user_obj.get_user(global_variables.userid)
	
	if getuser_status is False:
		createuser_status, response = user_obj.create_user(global_variables.userid)
		if createuser_status is False:
			QtGui.QMessageBox.critical(None, "ERROR", response)
			sys.exit(1)
	
	main_window = dialogs.main_window.MainWindow()
	global_variables.main_window = main_window
	
	main_window.show()
	application.exec_()