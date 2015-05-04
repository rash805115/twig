import resources.resource_manager
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import json

class File(QtGui.QLabel):
	file_signal = QtCore.Signal()
	file_version_signal = QtCore.Signal(bool)
	file_info_signal = QtCore.Signal()
	
	_version_show = False
	_stylesheet = """
		QLabel {
			background-color: white;
		}
	"""
	def __init__(self, properties):
		QtGui.QLabel.__init__(self)
		self.resource_manager = resources.resource_manager.ResourceManager()
		self.setToolTip(json.dumps(properties, indent = 8))
		self.properties = properties
		
		self.parent_directory = None
		self.setPixmap(self.resource_manager.get_resource("file"))
		self.setStyleSheet(self._stylesheet)
	
	def set_parent(self, parent):
		try:
			if self.parent_directory is not None:
				self.parent_directory.children.remove(self)
		except ValueError:
			pass
		
		if parent is None:
			self.parent_directory = None
		else:
			self.parent_directory = parent
			parent.children.append(self)
	
	def change_pixmap(self, change_type):
		if change_type == "modify":
			pixmap_type = "yellow"
		elif change_type == "add":
			pixmap_type = "green"
		elif change_type == "delete":
			pixmap_type = "red"
		elif change_type == "none":
			pixmap_type = "blue"
			
		self.setPixmap(self.resource_manager.get_resource(pixmap_type + "_file"))
	
	def open(self):
		self.file_signal.emit()
	
	def show_versions(self):
		self._version_show = True
		self.file_version_signal.emit(True)
	
	def hide_versions(self):
		self._version_show = False
		self.file_version_signal.emit(False)
	
	def get_info(self):
		self.file_info_signal.emit()
	
	def mouseDoubleClickEvent(self, event):
		self.open()
	
	def contextMenuEvent(self, event):
		menu = QtGui.QMenu()
		menu.addAction(QtGui.QAction("Open", menu, triggered = self.open))
		
		if(self._version_show is False):
			menu.addAction(QtGui.QAction("Show Versions", menu, triggered = self.show_versions))
		else:
			menu.addAction(QtGui.QAction("Hide Versions", menu, triggered = self.hide_versions))
		
		menu.addAction(QtGui.QAction("Get Info", menu, triggered = self.get_info))
		menu.exec_(QtGui.QCursor.pos())
	
	def paintEvent(self, paint_event):
		QtGui.QLabel.paintEvent(self, paint_event)
		painter = QtGui.QPainter(self)
		painter.drawText(self.pixmap().rect().bottomRight().x(), self.pixmap().rect().bottomRight().y(), self.properties["name"])