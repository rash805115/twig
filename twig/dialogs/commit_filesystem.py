import service.globals as global_variables
import validation.name_validation as name_validation
import pybookeeping.core.operation.commit as commit
import pybookeeping.core.operation.xray as xray
import pybookeeping.core.operation.directory as directory
import pybookeeping.core.operation.file as file
import pybookeeping.core.filesystem.structure as structure
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

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
		if not name_validation.NameValidation.validate_commit(self.commit_lineedit.text()):
			error_message = "Invalid commit id!\nCan only contain letters, numbers, underscore, hyphen and space."
			QtGui.QMessageBox.critical(self, "ERROR", error_message)
		else:
			self.commit_button.setText("Processing...")
			self.commit_button.setEnabled(False)
			self.commit_button.repaint()
			
			commit_obj = commit.Commit(global_variables.bookeeping_connection, self.commit_lineedit.text())
			xray_obj = xray.Xray(global_variables.bookeeping_connection)
			directory_obj = directory.Directory(global_variables.bookeeping_connection)
			file_obj = file.File(global_variables.bookeeping_connection)
			
			remote_xray = xray_obj.xray_full_node(self.filesystem_info["rootNodeId"])[1]
			local_xray = structure.Structure(self.filesystem_info["localPath"]).xray("")
			change_list = xray_obj.diff(local_xray, remote_xray)
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
					if change != "delete":
						raise KeyError
				
				if is_directory:
					if change == "add":
						directory_obj.create_directory(commit_obj, global_variables.userid,
										self.filesystem_info["filesystemId"],
										self.filesystem_info["version"], path, name, properties)
					elif change == "delete":
						directory_obj.delete_directory(commit_obj, change_list[key]["nodeid"])
					elif change == "modify":
						directory_obj.modify_directory(change_list[key]["nodeid"], properties)
				else:
					if change == "add":
						file_obj.create_file(commit_obj, global_variables.userid,
								self.filesystem_info["filesystemId"], self.filesystem_info["version"],
								path, name, properties)
					elif change == "delete":
						file_obj.delete_file(commit_obj, change_list[key]["nodeid"])
					elif change == "modify":
						file_obj.modify_file(change_list[key]["nodeid"], properties)
			
			status, response = commit_obj.commit()
			if status is True:
				self.done(QtGui.QDialog.Accepted)
			else:
				QtGui.QMessageBox.critical(self, "ERROR", response)