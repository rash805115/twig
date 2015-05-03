import PySide.QtGui as QtGui
import signals.signals as signals
import service.globals as global_variables
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.commit as commit
import pybookeeping.core.operation.xray as xray
import pybookeeping.core.filesystem.structure as local_structure

class FilesytemItem(QtGui.QListWidgetItem):
	def __init__(self, filesystem_info, parent):
		QtGui.QListWidgetItem.__init__(self, filesystem_info["filesystemId"], parent)
		self.filesystem_info = filesystem_info
		self.twig_signal = signals.TwigSignals().twig_signal
		
		new_connection = connection.Connection()
		self.commit = commit.Commit(new_connection, "Temporary Commit Id")
		self.xray = xray.Xray(new_connection)
	
	def filesystem_change(self):
		remote_xray = self.xray.xray_full_node(self.filesystem_info["nodeId"])
		local_xray = local_structure.Structure(self.filesystem_info["localpath"]).xray("")
		global_variables.main_window.toolbar.view_select.setCurrentIndex(1)
		import json
		print(json.dumps(remote_xray, indent = 8))
		print(json.dumps(local_xray, indent = 8))
	
	def commit(self):
		pass