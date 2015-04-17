import resources.resource_manager
import PySide.QtGui as QtGui
import utilities.coordinates as coordinates

class Directory(QtGui.QGraphicsPixmapItem):
	_directory_open = False
	_version_show = False
	_children = []
	pos_right_corner = (0, 0)
	pos_bottom_mid = (0, 0)
	pos_left_mid = (0, 0)
	margin_x = 50
	margin_y = 50
	
	def __init__(self, parent = None):
		super(Directory, self).__init__(parent)
		self.resource_manager = resources.resource_manager.ResourceManager()
		self.parent = parent
		
		if(parent is None):
			self.setOffset(0, 0)
			self.scene = QtGui.QGraphicsScene()
			self.open()
		else:
			self.setOffset(parent.pos_right_corner[0] + self.margin_x, parent.pos_right_corner[1] + self.margin_y)
			self.scene = parent.scene
			self.close()
		
		self.setScale(0.3)
		self.scene.addItem(self)
		self.pos_right_corner = coordinates.Coordinates.bottom_right(self)
		self.pos_bottom_mid = coordinates.Coordinates.bottom_mid(self)
		self.pos_left_mid = coordinates.Coordinates.left_mid(self) 
	
	def get_scene(self):
		return self.scene
	
	def add_directory(self):
		child = Directory(parent = self)
		print(child)
		self._children.append(child)
		self.draw_directory_children()
	
	def remove_directory(self, child_directory):
		self._children.remove(child_directory)
		self.draw_directory_children()
	
	def draw_directory_children(self):
		for child in self._children:
			self.scene.addLine(
				child.parent.pos_bottom_mid[0], child.parent.pos_bottom_mid[1],
				child.pos_left_mid[0], child.pos_left_mid[1]
			)
	
	#hide all children here
	def hide_directory_children(self):
		pass
	
	def open(self):
		self.setPixmap(self.resource_manager.get_resource("directory_open"))
		self._directory_open = True
		self.draw_directory_children()
	
	def close(self):
		self.setPixmap(self.resource_manager.get_resource("directory_close"))
		self._directory_open = False
		self.hide_directory_children()
	
	def show_versions(self):
		pass
	
	def hide_versions(self):
		pass
	
	def get_info(self):
		pass
	
	def mouseDoubleClickEvent(self, event):
		if(self._directory_open is False):
			self.open()
		else:
			self.close()
		
		#is this necessary?
		super(Directory, self).mouseDoubleClickEvent(event)
	
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

class MainWindow(QtGui.QGraphicsView):
	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		
		directory = Directory()
		directory.add_directory()
		directory.add_directory()
		self.setScene(directory.get_scene())
import sys
app = QtGui.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()