import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
from validation.name_validation import NameValidation

class AddAmazonS3Storage(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setWindowTitle("Add Amazon S3 Storage")
		
		amazons3_accesskey_label = QtGui.QLabel("Amazon S3 Access Key")
		self.amazons3_accesskey_lineedit = QtGui.QLineEdit()
		self.amazons3_accesskey_lineedit.setMaxLength(256)
		
		amazons3_secretkey_label = QtGui.QLabel("Amazon S3 Secret Key")
		self.amazons3_secretkey_lineedit = QtGui.QLineEdit()
		self.amazons3_secretkey_lineedit.setMaxLength(256)
		
		amazons3_bucketname_label = QtGui.QLabel("Amazon S3 Bucket Name")
		self.amazons3_bucketname_lineedit = QtGui.QLineEdit()
		self.amazons3_bucketname_lineedit.setMaxLength(256)
		
		friendly_name_label = QtGui.QLabel("Name your storage")
		self.friendly_name_lineedit = QtGui.QLineEdit()
		self.friendly_name_lineedit.setMaxLength(128)
		
		self.add_button = QtGui.QPushButton("Add")
		cancel_button = QtGui.QPushButton("Cancel")
		ok_cancel_button = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
		ok_cancel_button.addButton(self.add_button, QtGui.QDialogButtonBox.ButtonRole.AcceptRole)
		ok_cancel_button.addButton(cancel_button, QtGui.QDialogButtonBox.ButtonRole.RejectRole)
		
		layout = QtGui.QGridLayout()
		layout.addWidget(friendly_name_label, 0, 0)
		layout.addWidget(self.friendly_name_lineedit, 0, 1)
		layout.addWidget(amazons3_accesskey_label, 1, 0)
		layout.addWidget(self.amazons3_accesskey_lineedit, 1, 1)
		layout.addWidget(amazons3_secretkey_label, 2, 0)
		layout.addWidget(self.amazons3_secretkey_lineedit, 2, 1)
		layout.addWidget(amazons3_bucketname_label, 3, 0)
		layout.addWidget(self.amazons3_bucketname_lineedit, 3, 1)
		layout.addWidget(ok_cancel_button, 4, 1)
		self.setLayout(layout)
		
		ok_cancel_button.accepted.connect(self.add)
		ok_cancel_button.rejected.connect(self.close)
	
	def add(self):
		if not NameValidation.validate_name(self.friendly_name_lineedit.text()):
			QtGui.QMessageBox.critical(self, "ERROR", "Invalid name!")
		elif len(self.amazons3_accesskey_lineedit.text()) == 0:
			QtGui.QMessageBox.critical(self, "ERROR", "Empty Access Key!")
		elif len(self.amazons3_secretkey_lineedit.text()) == 0:
			QtGui.QMessageBox.critical(self, "ERROR", "Empty Secret Key!")
		elif len(self.amazons3_bucketname_lineedit.text()) == 0:
			QtGui.QMessageBox.critical(self, "ERROR", "Empty Bucket Name!")
		else:
			self.add_button.setText("Processing...")
			self.add_button.setEnabled(False)
			self.add_button.repaint()
			
			#add the credentials to the POTS.
			
			self.done(QtGui.QDialog.Accepted)