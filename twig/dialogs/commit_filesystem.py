import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import service.globals as global_variables
from validation.name_validation import NameValidation
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.commit as commit
import pybookeeping.core.operation.xray as xray
import pybookeeping.core.operation.directory as directory
import pybookeeping.core.operation.file as file
import pybookeeping.core.filesystem.structure as structure

class CommitFilesystem(QtGui.QDialog):
	def __init__(self, filesystem_info):
		QtGui.QDialog.__init__(self)
		self.filesystem_info = filesystem_info
		self.setWindowTitle("Commit")
		
		commit_label = QtGui.QLabel("Commit Id")
		self.commit_lineedit = QtGui.QLineEdit()
		self.commit_lineedit.setMaxLength(128)
		
		self.commit_button = QtGui.QPushButton("Commit")
		cancel_button = QtGui.QPushButton("Cancel")
		ok_cancel_button = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
		ok_cancel_button.addButton(self.commit_button, QtGui.QDialogButtonBox.ButtonRole.AcceptRole)
		ok_cancel_button.addButton(cancel_button, QtGui.QDialogButtonBox.ButtonRole.RejectRole)
		
		layout = QtGui.QGridLayout()
		layout.addWidget(commit_label, 0, 0)
		layout.addWidget(self.commit_lineedit, 0, 1)
		layout.addWidget(ok_cancel_button, 1, 1)
		self.setLayout(layout)
		
		ok_cancel_button.accepted.connect(self.commit)
		ok_cancel_button.rejected.connect(self.close)
	
	def commit(self):
		if not NameValidation.validate_commit(self.commit_lineedit.text()):
			QtGui.QMessageBox.critical(self, "ERROR", "Invalid commit id!")
		else:
			self.commit_button.setText("Processing...")
			self.commit_button.setEnabled(False)
			self.commit_button.repaint()
			
			new_connection = connection.Connection()
			new_commit = commit.Commit(new_connection, self.commit_lineedit.text())
			new_xray = xray.Xray(new_connection)
			new_directory = directory.Directory(new_connection)
			new_file = file.File(new_connection)
			
			remote_xray = new_xray.xray_full_node(self.filesystem_info["rootNodeId"])
			local_xray = structure.Structure(self.filesystem_info["localPath"]).xray("")
			change_list = new_xray.diff(local_xray, remote_xray)
			sorted_keys = sorted(list(change_list.keys()), key = lambda x : (x.count("/"), x.split("/")))
			
			for key in sorted_keys:
				is_directory = change_list[key]["directory"]
				change = change_list[key]["change"]
				path = change_list[key]["path"]
				name = change_list[key]["name"]
				
				try:
					properties = {
						"namehash": change_list[key]["namehash"],
						"contenthash": change_list[key]["contenthash"],
						"combinedhash": change_list[key]["combinedhash"]
					}
				except KeyError:
					if change == "delete":
						pass
					else:
						raise KeyError
				
				if is_directory:
					if change == "add":
						new_directory.create_directory(new_commit, global_variables._current_user, self.filesystem_info["filesystemId"], self.filesystem_info["version"], path, name, properties)
					elif change == "delete":
						new_directory.delete_directory(new_commit, change_list[key]["nodeid"])
					elif change == "modify":
						new_directory.modify_directory(change_list[key]["nodeid"], properties)
				else:
					if change == "add":
						new_file.create_file(new_commit, global_variables._current_user, self.filesystem_info["filesystemId"], self.filesystem_info["version"], path, name, properties)
					elif change == "delete":
						new_file.delete_file(new_commit, change_list[key]["nodeid"])
					elif change == "modify":
						new_file.modify_file(change_list[key]["nodeid"], properties)
			
			try:
				new_commit.commit()
				self.done(QtGui.QDialog.Accepted)
			except ValueError as error:
				QtGui.QMessageBox.critical(self, "ERROR", error.args[1]["operation_message"])