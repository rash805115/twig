import resources.general_resources
from PySide import QtCore, QtGui

class Ui_login_dialog(object):
	def setupUi(self, login_dialog):
		resources.general_resources.qInitResources()
		
		login_dialog.setObjectName("login_dialog")
		login_dialog.resize(453, 300)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(login_dialog.sizePolicy().hasHeightForWidth())
		login_dialog.setSizePolicy(sizePolicy)
		login_dialog.setStyleSheet("QDialog\n" "{\n" "	background: qconicalgradient(cx:1, cy:0, angle:43.9392, stop:0 rgba(0, 169, 208, 240), stop:1 rgba(255, 255, 255, 255))\n" "}")
		self.username_text = QtGui.QLineEdit(login_dialog)
		self.username_text.setGeometry(QtCore.QRect(30, 140, 391, 31))
		self.username_text.setStyleSheet("background: rgb(255, 255, 255)")
		self.username_text.setMaxLength(128)
		self.username_text.setFrame(False)
		self.username_text.setObjectName("username_text")
		self.password_text = QtGui.QLineEdit(login_dialog)
		self.password_text.setGeometry(QtCore.QRect(30, 180, 391, 31))
		self.password_text.setStyleSheet("background: rgb(255, 255, 255)")
		self.password_text.setMaxLength(64)
		self.password_text.setEchoMode(QtGui.QLineEdit.Password)
		self.password_text.setObjectName("password_text")
		self.login_button = QtGui.QPushButton(login_dialog)
		self.login_button.setGeometry(QtCore.QRect(170, 220, 131, 41))
		self.login_button.setStyleSheet("background: white;")
		self.login_button.setObjectName("login_button")
		self.login_logo_label = QtGui.QLabel(login_dialog)
		self.login_logo_label.setGeometry(QtCore.QRect(220, 30, 201, 101))
		self.login_logo_label.setText("")
		self.login_logo_label.setPixmap(QtGui.QPixmap(":/images/images/logo_transparent.png"))
		self.login_logo_label.setObjectName("login_logo_label")

		self.retranslateUi(login_dialog)
		QtCore.QMetaObject.connectSlotsByName(login_dialog)
		login_dialog.setTabOrder(self.password_text, self.username_text)
		login_dialog.setTabOrder(self.username_text, self.login_button)

	def retranslateUi(self, login_dialog):
		login_dialog.setWindowTitle(QtGui.QApplication.translate("login_dialog", "Login - Twig", None, QtGui.QApplication.UnicodeUTF8))
		self.username_text.setPlaceholderText(QtGui.QApplication.translate("login_dialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
		self.password_text.setPlaceholderText(QtGui.QApplication.translate("login_dialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
		self.login_button.setText(QtGui.QApplication.translate("login_dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))