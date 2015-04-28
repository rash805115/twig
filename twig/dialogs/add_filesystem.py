import PySide.QtGui as QtGui
import service.globals as global_variables
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.filesystem as filesystem
import pybookeeping.core.operation.commit as commit
from validation.name_validation import NameValidation

class AddFilesystem(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		
		name_label = QtGui.QLabel("Filesystem Name")
		self.name_lineedit = QtGui.QLineEdit()
		self.name_lineedit.setMaxLength(64)
		
		choose_folder_label = QtGui.QLabel("Choose Folder")
		choose_folder_button = QtGui.QPushButton("Choose")
		
		chosen_path_label = QtGui.QLabel("Chosen Path")
		self.chosen_path_value_label = QtGui.QLabel()
		
		commit_label = QtGui.QLabel("Commit Id")
		self.commit_lineedit = QtGui.QLineEdit()
		self.commit_lineedit.setMaxLength(64)
		
		commit_cancel_button = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
		
		layout = QtGui.QGridLayout()
		layout.addWidget(choose_folder_label, 0, 0)
		layout.addWidget(choose_folder_button, 0, 1)
		layout.addWidget(chosen_path_label, 1, 0)
		layout.addWidget(self.chosen_path_value_label, 1, 1)
		layout.addWidget(name_label, 2, 0)
		layout.addWidget(self.name_lineedit, 2, 1)
		layout.addWidget(commit_label, 3, 0)
		layout.addWidget(self.commit_lineedit, 3, 1)
		layout.addWidget(commit_cancel_button, 4, 1)
		self.setLayout(layout)
		
		choose_folder_button.clicked.connect(self.select_folder)
		commit_cancel_button.accepted.connect(self.commit)
		commit_cancel_button.rejected.connect(self.close)
	
	def select_folder(self):
		select_directory_dialog = QtGui.QFileDialog.getExistingDirectory(self, "Select a directory", ".")
		self.chosen_path_value_label.setText(select_directory_dialog)
	
	def commit(self):
		if not NameValidation.validate_name(self.name_lineedit.text()):
			QtGui.QMessageBox.critical(self, "ERROR", "Incorrect filesystem name!")
		elif len(self.chosen_path_value_label.text().strip()) == 0:
			QtGui.QMessageBox.critical(self, "ERROR", "No directory has been chosen!")
		elif not NameValidation.validate_name(self.commit_lineedit.text()):
			QtGui.QMessageBox.critical(self, "ERROR", "Incorrect commit id!")
		else:
			new_connection = connection.Connection()
			new_commit = commit.Commit(new_connection, self.commit_lineedit.text())
			filesystem_object = filesystem.Filesystem(new_connection)
			filesystem_object.create_filesystem(new_commit, global_variables._current_user, self.name_lineedit.text())
			
			try:
				new_commit.commit()
				self.done(QtGui.QDialog.Accepted)
			except ValueError as error:
				QtGui.QMessageBox.critical(self, "ERROR", error.args[1]["data"]["filesystem_create"]["operation_message"])