import PySide.QtGui as QtGui
import dialogs.mainview.defaultview as defaultview
import dialogs.menu.mainwindow_menubar as mainwindow_menubar
import guicomponents.filesystem_list
import guicomponents.toolbar
import service.globals as global_variables

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(800, 600)
		self.setMinimumHeight(600)
		self.setMinimumWidth(800)
		self.setWindowTitle(global_variables._app_name)
		
		central_widget = QtGui.QWidget()
		central_layout = QtGui.QGridLayout(central_widget)
		
		mainwindow_menubar.MainWindowMenubar(central_widget)
		toolbar = guicomponents.toolbar.Toolbar(central_widget)
		filesystem_list = guicomponents.filesystem_list.FilesystemList(central_widget)
		view = defaultview.DefaultView(central_widget)
		
		central_layout.addWidget(toolbar, 0, 0, 1, 2)
		central_layout.addWidget(filesystem_list, 1, 0)
		central_layout.addWidget(view, 1, 1)
		
		central_layout.setColumnMinimumWidth(1, 600)
		central_layout.setColumnStretch(1, 2)
		central_layout.setHorizontalSpacing(0)
		central_layout.setRowMinimumHeight(0, 30)
		
		self.setStatusBar(QtGui.QStatusBar(self))
		self.setCentralWidget(central_widget)