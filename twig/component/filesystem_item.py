import PySide.QtGui as QtGui
import service.globals as global_variables
import dialogs.commit_filesystem as commit_filesystem

class FilesytemItem(QtGui.QListWidgetItem):
	def __init__(self, filesystem_info, parent):
		QtGui.QListWidgetItem.__init__(self, filesystem_info["filesystemId"], parent)
		self.filesystem_info = filesystem_info
	
	def filesystem_changes(self):
		global_variables.main_window.toolbar.view_select.setCurrentIndex(1)
	
	def commit_changes(self):
		commit_dialog = commit_filesystem.CommitFilesystem(self.filesystem_info)
		if commit_dialog.exec_() == QtGui.QDialog.Accepted:
			a = {}
			#send the refresh signal