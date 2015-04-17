import resources.resource_manager
import PySide.QtGui as QtGui
import utilities.coordinates as coordinates

class Directory(QtGui.QGraphicsPixmapItem):
	_directory_open = False
	_version_show = False
	pos_right_corner = (0, 0)
	pos_bottom_mid = (0, 0)
	pos_left_mid = (0, 0)
	margin_x = 50
	margin_y = 50
	
	def __init__(self, scene, parent = None):
		super(Directory, self).__init__(parent)
		self.resource_manager = resources.resource_manager.ResourceManager()
		
		
# 		if(parent_directory is None):
# 			self.setOffset(0, 0)
# 			self.open()
# 		else:
# 			if(len(parent_directory.children) == 0):
# 				self.setOffset(parent_directory.pos_right_corner[0] + self.margin_x, parent_directory.pos_right_corner[1] + self.margin_y)
# 			else:
# 				self.setOffset(parent_directory.pos_right_corner[0] + self.margin_x, parent_directory.children[-1].pos_right_corner[1] + self.margin_y)
# 			
# 			parent_directory.children.append(self)
# 			self.close()
		
		self.setScale(0.3)
		self.pos_right_corner = coordinates.Coordinates.bottom_right(self)
		self.pos_bottom_mid = coordinates.Coordinates.bottom_mid(self)
		self.pos_left_mid = coordinates.Coordinates.left_mid(self)
		self.open()
		
		self.scene = scene
		self.scene.addItem(self)
		self.children_group = self.scene.createItemGroup([])
		for item in self.children_group:
			print(item)
	
	def add_child(self, child):
		self.children_group.addToGroup(child)
	
	def remove_child(self, child):
		self.children_group.removeFromGroup(child)
		
	def open(self):
		self.setPixmap(self.resource_manager.get_resource("directory_open"))
		self._directory_open = True
	
	def close(self):
		self.setPixmap(self.resource_manager.get_resource("directory_close"))
		self._directory_open = False
		self.scene.destroyItemGroup(self.children_group)
	
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
		scene = QtGui.QGraphicsScene()
		
		directory = Directory(scene)
		sub_dir1 = Directory(scene)
		sub_dir2 = Directory(scene)
		sub_dir2_1 = Directory(scene)
		
		directory.add_child(sub_dir1)
		directory.add_child(sub_dir2)
		sub_dir2.add_child(sub_dir2_1)
		
		self.setScene(scene)
import sys
app = QtGui.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()