import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
from guicomponents.directory import Directory
from guicomponents.file import File

class Folder(QtGui.QGraphicsWidget):
	def __init__(self, widget):
		QtGui.QGraphicsWidget.__init__(self)
		self.offset = 50
		
		children_layout = QtGui.QGraphicsLinearLayout(QtCore.Qt.Vertical)
		children_layout.setContentsMargins(self.offset, 0, 0, 0)
		
		if widget.__class__.__name__ is "Directory":
			widget.directory_signal.connect(self.toggle_children)
			widget.dir_version_signal.connect(self.toggle_dir_version)
			widget.dir_info_signal.connect(self.show_dir_info)
			
			for child in widget.children:
				children_layout.addItem(Folder(child))
		else:
			widget.file_signal.connect(self.open_file)
			widget.file_version_signal.connect(self.toggle_file_version)
			widget.file_info_signal.connect(self.show_file_info)
		
		self.children_widget = QtGui.QGraphicsWidget()
		self.children_widget.setLayout(children_layout)
		
		main_layout = QtGui.QGraphicsLinearLayout(QtCore.Qt.Vertical)
		main_layout.setContentsMargins(0, 0, 0, 0)
		
		self.leaf = QtGui.QGraphicsProxyWidget()
		self.leaf.setWidget(widget)
		self.leaf.setToolTip(widget.path)
		
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
	
	def toggle_children(self, directory_open):
		if(self.children_widget.isVisible()):
			self.layout().removeItem(self.children_widget)
			self.children_widget.hide()
		else:
			self.children_widget.show()
			self.layout().insertItem(1, self.children_widget)
		
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

class DefaultView(QtGui.QGraphicsView):
	def __init__(self, parent = None):
		super(DefaultView, self).__init__(parent)
		
		self.scene = QtGui.QGraphicsScene()
		self.root_directory = Directory("/dir1")
		self.child_directory1 = Directory("/dir1/dir1.1")
		self.child_directory2 = Directory("/dir1/dir1.1")
		
		file1 = File("/dir1/dir1.1/file1.1")
		file2 = File("/dir1/file1")
		
		self.child_directory1.set_parent(self.root_directory)
		self.child_directory2.set_parent(self.root_directory)
		file1.set_parent(self.child_directory1)
		file2.set_parent(self.root_directory)
		
		#self.scene.addItem(self.root_directory)
		#self.scene.addItem(self.child_directory1)
		#self.scene.addItem(self.child_directory2)
		
		self.scene.addItem(Folder(self.root_directory))
		
		self.setScene(self.scene)	

import sys
app = QtGui.QApplication(sys.argv)
main_window = DefaultView()
main_window.show()
app.exec_()
