import PySide.QtGui as QtGui
import pybookeeping.core.operation.commit as commit
import pybookeeping.core.operation.filesystem as filesystem
import pybookeeping.core.filesystem as local_filesystem
import service.globals as global_variables

class FilesytemItem(QtGui.QListWidgetItem):
	def __init__(self, filesystem_info, parent):
		QtGui.QListWidgetItem.__init__(self, filesystem_info["filesystemId"], parent)
		self.filesystem_info = filesystem_info
	
	def filesystem_change(self):
		print("here")
		print(self.filesystem_info)