import resources.resource_manager
from PySide import QtCore, QtGui

class LoginDialog(object):
	_dialog_stylesheet = """
		QDialog {
			background: qconicalgradient(cx:1, cy:0, angle:43.9392, stop:0 rgba(0, 169, 208, 240), stop:1 rgba(255, 255, 255, 255));
		}
	"""
	_text_stylesheet = """
		background: rgb(255, 255, 255);
	"""
	_button_stylesheet = """
		background: white;
	"""
	
	def setup(self, login_dialog):
		resource_manager = resources.resource_manager.ResourceManager()
		self.setWindowTitle("Login - Twig")
		
		login_dialog.setMinimumWidth(453)
		login_dialog.setMinimumHeight(300)
		login_dialog.setMaximumWidth(453)
		login_dialog.setMaximumHeight(300)
		login_dialog.setStyleSheet(self._dialog_stylesheet)
		
		self.username_text = QtGui.QLineEdit(login_dialog)
		self.username_text.setGeometry(QtCore.QRect(30, 140, 391, 31))
		self.username_text.setStyleSheet(self._text_stylesheet)
		self.username_text.setMaxLength(128)
		self.username_text.setPlaceholderText("Username")
		
		self.password_text = QtGui.QLineEdit(login_dialog)
		self.password_text.setGeometry(QtCore.QRect(30, 180, 391, 31))
		self.password_text.setStyleSheet(self._text_stylesheet)
		self.password_text.setMaxLength(64)
		self.password_text.setEchoMode(QtGui.QLineEdit.Password)
		self.password_text.setPlaceholderText("Password")
		
		self.login_button = QtGui.QPushButton(login_dialog)
		self.login_button.setGeometry(QtCore.QRect(170, 220, 131, 41))
		self.login_button.setStyleSheet(self._button_stylesheet)
		self.login_button.setText("Login")
		self.login_button.setFocus(QtCore.Qt.FocusReason.TabFocusReason)
		
		self.login_logo_label = QtGui.QLabel(login_dialog)
		self.login_logo_label.setGeometry(QtCore.QRect(220, 30, 201, 101))
		self.login_logo_label.setText("Twig Logo")
		self.login_logo_label.setPixmap(resource_manager.get_resource("logo", scale = False))
		
		login_dialog.setTabOrder(self.username_text, self.password_text)
		login_dialog.setTabOrder(self.password_text, self.login_button)
		login_dialog.setTabOrder(self.login_button, self.username_text)
		
		self.login_button.clicked.connect(self.login)
	
	def login(self):
		print(self.username_text.text())
		print(self.password_text.text())