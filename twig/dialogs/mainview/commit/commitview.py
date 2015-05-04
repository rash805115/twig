import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import dialogs.mainview.commit.directory as directory
import dialogs.mainview.commit.file as file
import service.globals as global_variables
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.xray as xray
import pybookeeping.core.filesystem.structure as structure

class Entity(QtGui.QGraphicsWidget):
	def __init__(self, entity):
		QtGui.QGraphicsWidget.__init__(self)
		self.offset = 50
		
		children_layout = QtGui.QGraphicsLinearLayout(QtCore.Qt.Vertical)
		children_layout.setContentsMargins(self.offset, 0, 0, 0)
		children_layout.setMinimumWidth(200)
		
		if entity.__class__.__name__ is "Directory":
			entity.directory_signal.connect(self.toggle_children)
			entity.dir_version_signal.connect(self.toggle_dir_version)
			entity.dir_info_signal.connect(self.show_dir_info)
			
			for child in entity.children:
				children_layout.addItem(Entity(child))
		else:
			entity.file_signal.connect(self.open_file)
			entity.file_version_signal.connect(self.toggle_file_version)
			entity.file_info_signal.connect(self.show_file_info)
		
		self.children_widget = QtGui.QGraphicsWidget()
		self.children_widget.setLayout(children_layout)
		
		main_layout = QtGui.QGraphicsLinearLayout(QtCore.Qt.Vertical)
		main_layout.setContentsMargins(0, 0, 0, 0)
		
		self.leaf = QtGui.QGraphicsProxyWidget()
		self.leaf.setWidget(entity)
		
		main_layout.addItem(self.leaf)
		main_layout.addItem(self.children_widget)
		self.setLayout(main_layout)
	
	def paint(self, painter, option, widget):
		QtGui.QGraphicsWidget.paint(self, painter, option, widget)
		
		if(self.children_widget.isVisible() and self.children_widget.layout().count() > 0):
			last_child = self.children_widget.layout().itemAt(self.children_widget.layout().count() - 1)
			last_child_y = self.children_widget.geometry().top() + last_child.geometry().top() + self.leaf.geometry().height() / 2
			painter.drawLine(self.offset / 2, self.leaf.geometry().bottom(), self.offset / 2, last_child_y)
			
			for i in range(0, self.children_widget.layout().count()):
				child = self.children_widget.layout().itemAt(i)
				child_y = self.children_widget.geometry().top() + child.geometry().top() + self.leaf.geometry().height() / 2
				painter.drawLine(self.offset / 2, child_y, self.offset, child_y)
	
	def toggle_children(self, open_directory):
		if open_directory:
			self.children_widget.show()
			self.layout().insertItem(1, self.children_widget)
		else:
			self.layout().removeItem(self.children_widget)
			self.children_widget.hide()
		
		self.update()
	
	def toggle_dir_version(self, show_version):
		if show_version:
			print("Opening the version.")
		else:
			print("Closing the version.")
	
	def show_dir_info(self):
		print("Showing dir info")
	
	def open_file(self):
		print("Opening the file")
	
	def toggle_file_version(self, file_version):
		if file_version:
			print("Opening the version.")
		else:
			print("Closing the version.")
	
	def show_file_info(self):
		print("Showing file info")

class CommitView(QtGui.QGraphicsView):
	def __init__(self, entity):
		QtGui.QGraphicsView.__init__(self, entity)
		
		self.scene = QtGui.QGraphicsScene()
		self.setScene(self.scene)
		self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		
		global_variables.twig_signal.filesystem_list_changed.connect(self.draw)
	
	def draw(self, filesystem_info):
		self.scene.clear()
		
		filesystem_rootid = filesystem_info["rootNodeId"]
		properties = {
			"name": "Root Directory",
			"path": "/",
			"nodeId": filesystem_rootid
		}
		self.root_directory = directory.Directory(properties)
		nodes = {properties["path"]: self.root_directory}
		
		new_xray = xray.Xray(connection.Connection())
		remote_xray = new_xray.xray_full_node(filesystem_rootid)
		local_xray = structure.Structure(filesystem_info["localpath"]).xray("")
		change_list = new_xray.diff(local_xray, remote_xray)
		sorted_keys = sorted(list(change_list.keys()), key = lambda x : (x.count("/"), x.split("/")))
		
		for key in sorted_keys:
			is_directory = change_list[key]["directory"]
			change = change_list[key]["change"]
			path = change_list[key]["path"]
			name = change_list[key]["name"]
			
			if is_directory:
				child = directory.Directory(change_list[key])
			else:
				child = file.File(change_list[key])
			
			child.change_pixmap(change)
			child.set_parent(nodes[path])
			nodes[("/" if path == "/" else (path + "/")) + name] = child
		
		self.scene.addItem(Entity(self.root_directory))