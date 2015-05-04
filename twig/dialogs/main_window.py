import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import dialogs.mainview.default.defaultview as defaultview
import dialogs.mainview.commit.commitview as commitview
import dialogs.menu.mainwindow_menubar as mainwindow_menubar
import component.filesystem_list
import component.toolbar
import service.globals as global_variables

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(800, 600)
		self.setMinimumHeight(600)
		self.setMinimumWidth(800)
		self.setWindowTitle(global_variables._app_name)
		
		central_widget = QtGui.QWidget()
		self.central_layout = QtGui.QGridLayout(central_widget)
		
		self.defaultview = defaultview.DefaultView(central_widget)
		self.commitview = commitview.CommitView(central_widget)
		
		self.setMenuBar(mainwindow_menubar.MainWindowMenubar(self))
		self.toolbar = component.toolbar.Toolbar(self)
		self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
		self.setStatusBar(QtGui.QStatusBar(self))
		filesystem_list = component.filesystem_list.FilesystemList(central_widget)
		
		self.central_layout.addWidget(filesystem_list, 0, 0)
		self.central_layout.addWidget(self.defaultview, 0, 1)
		
		self.central_layout.setColumnMinimumWidth(1, 600)
		self.central_layout.setColumnStretch(1, 2)
		self.central_layout.setHorizontalSpacing(0)
		
		self.setCentralWidget(central_widget)
		
		global_variables.twig_signal.close_mainwindow.connect(self.close_window)
		global_variables.twig_signal.view_changed.connect(self.change_view)
	
	def change_view(self, index):
		if index == 0:
			self.defaultview.setParent(self)
			self.central_layout.addWidget(self.defaultview, 0, 1)
		elif index == 1:
			self.commitview.setParent(self)
			self.central_layout.addWidget(self.commitview, 0, 1)
	
	def close_window(self):
		self.close()