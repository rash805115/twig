import resources.resource_manager
import service.globals as global_variables
import utilities.encryption as encryption
import utilities.download as download
import pybookeeping.core.communication.connection as connection
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import PySide.QtWebKit as QtWebKit
import os
import json

class LoginDialog(QtGui.QDialog):
	_dialog_stylesheet = """
		QDialog {
			background: qconicalgradient(cx:1, cy:0, angle:43.9392, stop:0 rgba(0, 169, 208, 240), stop:1 rgba(255, 255, 255, 255));
		}
	"""
	
	def __init__(self):
		QtGui.QDialog.__init__(self)
		resource_manager = resources.resource_manager.ResourceManager()
		self.secret_filepath = "./../service/secrets"
		self.encryption = encryption.Encryption()
		
		self.setMinimumWidth(550)
		self.setMinimumHeight(180)
		self.setMaximumWidth(550)
		self.setMaximumHeight(180)
		self.setStyleSheet(self._dialog_stylesheet)
		self.setWindowTitle("Login - Twig")
		
		login_logo_label = QtGui.QLabel(self)
		login_logo_label.setGeometry(QtCore.QRect(350, 40, 201, 101))
		login_logo_label.setText("Twig Logo")
		login_logo_label.setPixmap(resource_manager.get_resource("logo"))
		
		if os.path.exists(self.secret_filepath):
			with open(self.secret_filepath, "r") as file:
				contents = file.read()
				self.secrets = json.loads(contents)
			
			pixmap = resource_manager.get_resource("google_signin")
			google_login_button = QtGui.QPushButton(self)
			google_login_button.setIcon(QtGui.QIcon(pixmap))
			google_login_button.setIconSize(pixmap.rect().size())
			google_login_button.setFixedSize(pixmap.rect().size())
			google_login_button.move(20, 30)
			google_login_button.clicked.connect(self.relogin_with_google)
			
			user_image = QtGui.QLabel(parent = self)
			user_image_pixmap = QtGui.QPixmap()
			user_image_pixmap.loadFromData(download.Download.download(self.secrets["user_image"] + "?sz=40"))
			user_image.setPixmap(user_image_pixmap)
			user_image.setToolTip("You are already logged in as " + self.secrets["user_name"])
			user_image.move(google_login_button.rect().topRight().x() + 20, 37)
			
			pixmap = resource_manager.get_resource("facebook_signin")
			facebook_login_button = QtGui.QPushButton(self)
			facebook_login_button.setIcon(QtGui.QIcon(pixmap))
			facebook_login_button.setIconSize(pixmap.rect().size())
			facebook_login_button.setFixedSize(pixmap.rect().size())
			facebook_login_button.move(20, 90)
			facebook_login_button.clicked.connect(self.relogin_with_facebook)
		else:
			pixmap = resource_manager.get_resource("google_signin")
			google_login_button = QtGui.QPushButton(self)
			google_login_button.setIcon(QtGui.QIcon(pixmap))
			google_login_button.setIconSize(pixmap.rect().size())
			google_login_button.setFixedSize(pixmap.rect().size())
			google_login_button.move(20, 30)
			google_login_button.clicked.connect(self.login_with_google)
			
			pixmap = resource_manager.get_resource("facebook_signin")
			facebook_login_button = QtGui.QPushButton(self)
			facebook_login_button.setIcon(QtGui.QIcon(pixmap))
			facebook_login_button.setIconSize(pixmap.rect().size())
			facebook_login_button.setFixedSize(pixmap.rect().size())
			facebook_login_button.move(20, 90)
			facebook_login_button.clicked.connect(self.login_with_facebook)
	
	def relogin_with_google(self):
		userid = self.secrets["userid"]
		user_name = self.secrets["user_name"]
		user_image = self.secrets["user_image"]
		access_token = self.encryption.decrypt(self.secrets["access_token"], global_variables.google_client_secret)
		refresh_token = self.encryption.decrypt(self.secrets["refresh_token"], global_variables.google_client_secret)
		
		global_variables.userid = userid
		global_variables.user_name = user_name
		global_variables.user_image = user_image
		global_variables.google_access_token = access_token
		global_variables.google_refresh_token = refresh_token
		
		self.done(QtGui.QDialog.Accepted)
	
	def relogin_with_facebook(self):
		QtGui.QMessageBox.critical(None, "ERROR", "Facebook Re-Login not yet implemented!")
	
	def login_with_google(self):
		auth_code_url = (
			"https://accounts.google.com/o/oauth2/auth?"
			"scope=email&"
			"redirect_uri=urn:ietf:wg:oauth:2.0:oob:auto&" 
			"response_type=code&"
			"client_id=" + global_variables.google_client_id
		)
		
		web_dialog = QtGui.QDialog()
		web_dialog.setMinimumHeight(600)
		web_dialog.setMinimumWidth(800)
		web = QtWebKit.QWebView(web_dialog)
		web.load(QtCore.QUrl(auth_code_url))
		web_dialog.exec_()
		web.show()
		
		message = web.title()
		try:
			if message.find("code=") == -1:
				raise KeyError
			
			auth_code = message[message.find("code=") + 5 : ]
			auth_connection = connection.Connection()
			auth_connection.host = "www.googleapis.com"
			auth_connection.base = "oauth2/v3/token"
			auth_connection.https = True
			auth_connection.headers = {"Content-Type": "application/x-www-form-urlencoded"}
			auth_connection.timeout = 10
			payload = (
				"code=" + auth_code + "&"
				"client_id=" + global_variables.google_client_id + "&" 
				"client_secret=" + global_variables.google_client_secret + "&"  
				"redirect_uri=" + global_variables.google_redirect_uri + "&"
				"grant_type=" + "authorization_code"
			)
			response = auth_connection.post_request("", payload)
			
			access_token = response["access_token"]
			refresh_token = response["refresh_token"]
			auth_connection.base = "plus/v1/people/me"
			auth_connection.headers = {"Authorization": "Bearer " + access_token}
			response = auth_connection.get_request()
			
			global_variables.user_image = response["image"]["url"]
			global_variables.user_name = response["name"]["givenName"] + " " + response["name"]["familyName"]
			global_variables.google_access_token = access_token
			global_variables.google_refresh_token = refresh_token
			for email in response["emails"]:
				if email["type"] == "account":
					global_variables.userid = email["value"]
			
			with open(self.secret_filepath, "w+") as file:
				contents = {
					"userid": global_variables.userid,
					"user_name": global_variables.user_name,
					"user_image": response["image"]["url"],
					"access_token": self.encryption.encrypt(access_token, global_variables.google_client_secret).decode("UTF-8"),
					"refresh_token": self.encryption.encrypt(refresh_token, global_variables.google_client_secret).decode("UTF-8")
				}
				file.write(json.dumps(contents))
			
			self.done(QtGui.QDialog.Accepted)
		except (KeyError, ValueError):
			self.done(QtGui.QDialog.Rejected)
	
	def login_with_facebook(self):
		QtGui.QMessageBox.critical(None, "ERROR", "Facebook Login not yet implemented!")