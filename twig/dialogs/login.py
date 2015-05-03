import resources.resource_manager
import service.globals as global_variables
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui

class LoginDialog(QtGui.QDialog):
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
	
	def __init__(self):
		QtGui.QDialog.__init__(self)
		resource_manager = resources.resource_manager.ResourceManager()
		
		self.setMinimumWidth(453)
		self.setMinimumHeight(300)
		self.setMaximumWidth(453)
		self.setMaximumHeight(300)
		self.setStyleSheet(self._dialog_stylesheet)
		self.setWindowTitle("Login - Twig")
		
		self.username_text = QtGui.QLineEdit(self)
		self.username_text.setGeometry(QtCore.QRect(30, 140, 391, 31))
		self.username_text.setStyleSheet(self._text_stylesheet)
		self.username_text.setMaxLength(128)
		self.username_text.setPlaceholderText("Username")
		
		self.password_text = QtGui.QLineEdit(self)
		self.password_text.setGeometry(QtCore.QRect(30, 180, 391, 31))
		self.password_text.setStyleSheet(self._text_stylesheet)
		self.password_text.setMaxLength(64)
		self.password_text.setEchoMode(QtGui.QLineEdit.Password)
		self.password_text.setPlaceholderText("Password")
		
		login_button = QtGui.QPushButton(self)
		login_button.setGeometry(QtCore.QRect(170, 220, 131, 41))
		login_button.setStyleSheet(self._button_stylesheet)
		login_button.setText("Login")
		login_button.setFocus(QtCore.Qt.FocusReason.TabFocusReason)
		
		login_logo_label = QtGui.QLabel(self)
		login_logo_label.setGeometry(QtCore.QRect(220, 30, 201, 101))
		login_logo_label.setText("Twig Logo")
		login_logo_label.setPixmap(resource_manager.get_resource("logo", scale = False))
		
		self.setTabOrder(self.username_text, self.password_text)
		self.setTabOrder(self.password_text, login_button)
		self.setTabOrder(login_button, self.username_text)
		
		login_button.clicked.connect(self.login)
	
	def login(self):
		if self.username_text.text() == "john" and self.password_text.text() == "aaa":
			global_variables._current_user = self.username_text.text() 
			self.done(QtGui.QDialog.Accepted)