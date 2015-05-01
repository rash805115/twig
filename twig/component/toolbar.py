import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import resources.resource_manager
import signals.signals as signals

class Toolbar(QtGui.QToolBar):
	def __init__(self, widget):
		QtGui.QToolBar.__init__(self, widget)
		self.resource_manager = resources.resource_manager.ResourceManager()
		self.twig_signal = signals.TwigSignals().twig_signal
		
		add_filesystem_icon = QtGui.QIcon()
		add_filesystem_icon.addPixmap(self.resource_manager.get_resource("file"))
		
		add_filesystem = QtGui.QToolButton()
		add_filesystem.setIcon(add_filesystem_icon)
		add_filesystem.setText("Add Filesystem")
		add_filesystem.setToolTip("Add Filesystem")
		add_filesystem.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
		add_filesystem.clicked.connect(self.addfilesystem_clicked)
		
		quit_program = QtGui.QToolButton()
		quit_program.setText("Quit")
		quit_program.setToolTip("Quit")
		quit_program.clicked.connect(self.quitprogram_clicked)
		
		self.view_select = QtGui.QComboBox()
		self.view_select.addItem("Default")
		self.view_select.addItem("Commit")
		self.view_select.currentIndexChanged.connect(self.change_view)
		
		self.addWidget(add_filesystem)
		self.addWidget(quit_program)
		self.addWidget(self.view_select)
	
	def addfilesystem_clicked(self):
		print("add")
	
	def quitprogram_clicked(self):
		print("quit")
	
	def change_view(self, index):
		self.twig_signal.view_changed.emit(index)