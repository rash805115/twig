import PySide.QtGui as QtGui
import resources.resource_manager
import service.globals as global_variables

class Toolbar(QtGui.QToolBar):
	def __init__(self, entity):
		QtGui.QToolBar.__init__(self, entity)
		self.resource_manager = resources.resource_manager.ResourceManager()
		
		add_filesystem_icon = QtGui.QIcon()
		add_filesystem_icon.addPixmap(self.resource_manager.get_resource("filesystem"))
		add_filesystem = QtGui.QToolButton()
		add_filesystem.setIcon(add_filesystem_icon)
		add_filesystem.setText("Add Filesystem")
		add_filesystem.setToolTip("Add Filesystem")
		add_filesystem.clicked.connect(self.addfilesystem_clicked)
		
		quit_program_icon = QtGui.QIcon()
		quit_program_icon.addPixmap(self.resource_manager.get_resource("exit"))
		quit_program = QtGui.QToolButton()
		quit_program.setIcon(quit_program_icon)
		quit_program.setText("Quit")
		quit_program.setToolTip("Quit")
		quit_program.clicked.connect(self.quitprogram_clicked)
		
		self.view_select = QtGui.QComboBox()
		self.view_select.addItem("Default View")
		self.view_select.addItem("Commit View")
		self.view_select.setToolTip("Select View")
		self.view_select.currentIndexChanged.connect(self.change_view)
		
		self.addWidget(add_filesystem)
		self.addWidget(quit_program)
		self.addWidget(self.view_select)
	
	def addfilesystem_clicked(self):
		global_variables.twig_signal.add_filesystem.emit()
	
	def quitprogram_clicked(self):
		global_variables.twig_signal.close_mainwindow.emit()
	
	def change_view(self, index):
		global_variables.twig_signal.view_changed.emit(index)