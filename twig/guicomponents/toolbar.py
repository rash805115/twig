import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import resources.resource_manager

class Toolbar(QtGui.QToolBar):
	def __init__(self, widget):
		QtGui.QToolBar.__init__(self, widget)
		self.resource_manager = resources.resource_manager.ResourceManager()
		
		add_filesystem_icon = QtGui.QIcon()
		add_filesystem_icon.addPixmap(self.resource_manager.get_resource("file"))
		
		add_filesystem = QtGui.QToolButton()
		add_filesystem.setIcon(add_filesystem_icon)
		add_filesystem.setText("Add Filesystem")
		add_filesystem.setToolTip("Add Filesystem")
		add_filesystem.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
		add_filesystem.clicked.connect(self.addfilesystem_clicked)
		
		_quit = QtGui.QToolButton()
		_quit.setText("Quit")
		_quit.setToolTip("Quit")
		_quit.clicked.connect(self._quit)
		
		self.addWidget(add_filesystem)
		self.addWidget(_quit)
	
	def addfilesystem_clicked(self):
		print("add")
	def _quit(self):
		print("quit")