import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import signals.signals as signals
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.xray as xray
import dialogs.mainview.commit.directory as directory
import dialogs.mainview.commit.file as file

class Entity(QtGui.QGraphicsWidget):
	def __init__(self, widget):
		QtGui.QGraphicsWidget.__init__(self)
		self.offset = 50
		self.entity = widget
		
		self.connect_children(self.entity)
		
		self.children_layout = QtGui.QGraphicsLinearLayout(QtCore.Qt.Vertical)
		self.children_layout.setContentsMargins(self.offset, 0, 0, 0)
		
		if self.entity.__class__.__name__ is "Directory":
			self.entity.directory_signal.connect(self.toggle_children)
			self.entity.dir_version_signal.connect(self.toggle_dir_version)
			self.entity.dir_info_signal.connect(self.show_dir_info)
		else:
			self.entity.file_signal.connect(self.open_file)
			self.entity.file_version_signal.connect(self.toggle_file_version)
			self.entity.file_info_signal.connect(self.show_file_info)
		
		self.children_widget = QtGui.QGraphicsWidget()
		self.children_widget.setLayout(self.children_layout)
		
		main_layout = QtGui.QGraphicsLinearLayout(QtCore.Qt.Vertical)
		main_layout.setContentsMargins(0, 0, 0, 0)
		
		self.leaf = QtGui.QGraphicsProxyWidget()
		self.leaf.setWidget(self.entity)
		
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
			for child in self.entity.children:
				self.children_layout.addItem(Entity(child))
			
			self.children_widget.show()
			self.layout().insertItem(1, self.children_widget)
		else:
			for child in self.entity.children:
				child.set_parent(None)
				
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
	
	def connect_children(self, parent):
		parent_nodeid = parent.properties["nodeId"]
		new_xray = xray.Xray(connection.Connection())
		children = new_xray.xray_node(parent_nodeid)
		
		for child in children:
			is_directory = False
			try:
				child["directoryName"]
				is_directory = True
			except KeyError:
				is_directory = False
			
			if is_directory is True:
				directory.Directory(child).set_parent(parent)
			else:
				file.File(child).set_parent(parent)

class CommitView(QtGui.QGraphicsView):
	def __init__(self, widget):
		QtGui.QGraphicsView.__init__(self, widget)
		self.twig_signal = signals.TwigSignals().twig_signal
		
		self.scene = QtGui.QGraphicsScene()
		self.setScene(self.scene)
		self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		
		self.twig_signal.filesystem_list_changed.connect(self.draw_root)
	
	def draw_root(self, filesystem_info):
		self.scene.clear()
		
		filesystem_rootid = filesystem_info["rootNodeId"]
		properties = {
			"directoryName": "Root Directory",
			"directoryPath": "/",
			"nodeId": filesystem_rootid
		}
		
		self.root_directory = directory.Directory(properties)
		self.scene.addItem(Entity(self.root_directory))