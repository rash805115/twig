import resources.resource_manager
import PySide.QtGui as QtGui

class File(QtGui.QLabel):
	_version_show = False
	_stylesheet = """
		QLabel {
			background-color: white;
		}
	"""
	def __init__(self):
		QtGui.QLabel.__init__(self)
		self.resource_manager = resources.resource_manager.ResourceManager()
		
		self.parent_directory = None
		self.setPixmap(self.resource_manager.get_resource("file"))
		self.setStyleSheet(self._stylesheet)
	
	def set_parent(self, parent):
		try:
			parent.children.remove(self)
		except ValueError:
			pass
		
		if parent is None:
			self.parent_directory = None
		else:
			self.parent_directory = parent
			parent.children.append(self)
	
	def open(self):
		#signal to open the file using system exec.
		pass
	
	def show_versions(self):
		self._version_show = True
	
	def hide_versions(self):
		self._version_show = False
	
	def get_info(self):
		pass
	
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