import resources.resource_manager
import service.globals as global_variables
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import PySide.QtWebKit as QtWebKit

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
		login_logo_label.setPixmap(resource_manager.get_resource("logo"))
		
		self.setTabOrder(self.username_text, self.password_text)
		self.setTabOrder(self.password_text, login_button)
		self.setTabOrder(login_button, self.username_text)
		
		login_button.clicked.connect(self.login)
	
	def login(self):
		login_url = (
			"https://accounts.google.com/o/oauth2/auth?scope=email&redirect_uri=urn:ietf:wg:oauth:2.0:oob:auto&" 
			"response_type=code&client_id=250214960321-kmbt9glf164mbmd68jcrj2q44qt7ec0u.apps.googleusercontent.com"
		)
		
		web_dialog = QtGui.QDialog()
		web_dialog.setMinimumHeight(600)
		web_dialog.setMinimumWidth(800)
		web = QtWebKit.QWebView(web_dialog)
		web.load(QtCore.QUrl(login_url))
		web_dialog.exec_()
		
		web.show()
		message = web.title()
		
		if message.find("code=") != -1:
			auth_code = message[message.find("code=") + 5 : ]
			import requests
			payload = "code=" + auth_code + "&client_id=250214960321-kmbt9glf164mbmd68jcrj2q44qt7ec0u.apps.googleusercontent.com&client_secret=-AYzMFGu77bANtqFi0nrvT0N&redirect_uri=urn:ietf:wg:oauth:2.0:oob:auto&grant_type=authorization_code"
			response = requests.post("https://www.googleapis.com/oauth2/v3/token", headers = {"Content-Type": "application/x-www-form-urlencoded"}, data = payload)
			response_dict = response.json()
			
			response = requests.get("https://www.googleapis.com/plus/v1/people/me", headers = {"Authorization": "Bearer " + response_dict["access_token"]})
			get_dict = response.json()
			print(get_dict)
			self.done(QtGui.QDialog.Accepted)
		
		self.done(QtGui.QDialog.Rejected)
# 		local_server.join()
# 		global_variables._current_user = self.username_text.text()
# 		self.done(QtGui.QDialog.Accepted)
		
		#QtGui.QDesktopServices.openUrl(QtCore.QUrl(login_url))