import PySide.QtGui as QtGui
import service.globals as global_variables
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.commit as commit
import pybookeeping.core.operation.xray as xray
import pybookeeping.core.filesystem.structure as local_structure

class FilesytemItem(QtGui.QListWidgetItem):
	def __init__(self, filesystem_info, parent):
		QtGui.QListWidgetItem.__init__(self, filesystem_info["filesystemId"], parent)
		self.filesystem_info = filesystem_info
		
		new_connection = connection.Connection()
		self.commit = commit.Commit(new_connection, "Name your commit")
		self.xray = xray.Xray(new_connection)
	
	def filesystem_change(self):
		remote_xray = self.xray.xray_full_node(self.filesystem_info["nodeId"])
		local_xray = local_structure.Structure(self.filesystem_info["localpath"]).xray("")
		global_variables.main_window.toolbar.view_select.setCurrentIndex(1)
	
	def commit(self):
		pass