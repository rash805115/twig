import resources.resource_manager
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import json

class Directory(QtGui.QLabel):
	directory_signal = QtCore.Signal(bool)
	dir_version_signal = QtCore.Signal(bool)
	dir_info_signal = QtCore.Signal()
	
	_directory_open = False
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
		self.children = []
		
		self.setStyleSheet(self._stylesheet)
		self.close()
	
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
	
	def open(self):
		self.setPixmap(self.resource_manager.get_resource("directory_open"))
		self._directory_open = True
		self.directory_signal.emit(True)
	
	def close(self):
		self.setPixmap(self.resource_manager.get_resource("directory_close"))
		self._directory_open = False
		self.directory_signal.emit(False)
	
	def show_versions(self):
		self._version_show = True
		self.dir_version_signal.emit(True)
	
	def hide_versions(self):
		self._version_show = False
		self.dir_version_signal.emit(False)
	
	def get_info(self):
		self.dir_info_signal.emit()
	
	def mouseDoubleClickEvent(self, event):
		if(self._directory_open is False):
			self.open()
		else:
			self.close()
	
	def contextMenuEvent(self, event):
		menu = QtGui.QMenu()
		
		if(self._directory_open is False):
			menu.addAction(QtGui.QAction("Open", menu, triggered = self.open))
		else:
			menu.addAction(QtGui.QAction("Close", menu, triggered = self.close))
		
		if(self._version_show is False):
			menu.addAction(QtGui.QAction("Show Versions", menu, triggered = self.show_versions))
		else:
			menu.addAction(QtGui.QAction("Hide Versions", menu, triggered = self.hide_versions))
		
		menu.addAction(QtGui.QAction("Get Info", menu, triggered = self.get_info))
		menu.exec_(QtGui.QCursor.pos())
	
	def paintEvent(self, paint_event):
		QtGui.QLabel.paintEvent(self, paint_event)
		painter = QtGui.QPainter(self)
		painter.drawText(self.pixmap().rect().bottomRight().x() + 5, self.pixmap().rect().bottomRight().y() - 10, self.properties["directoryName"])