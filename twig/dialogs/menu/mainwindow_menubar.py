import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import service.globals as global_variables

class MainWindowMenubar(QtGui.QMenuBar):
	def __init__(self, entity):
		QtGui.QMenuBar.__init__(self, entity)
		self.setNativeMenuBar(True)
		self.setGeometry(QtCore.QRect(0, 0, 800, 21))
		
		twig_menu = QtGui.QMenu(global_variables._app_name, parent = self)
		twig_menu.addAction(QtGui.QAction("Preferences", twig_menu, triggered = self.preferences_clicked))
		twig_menu.addSeparator()
		twig_menu.addAction(QtGui.QAction("Sign Out", twig_menu, triggered = self.signout_clicked))
		twig_menu.addAction(QtGui.QAction("Quit", twig_menu, triggered = self.quit_clicked))
		
		filesystem_menu = QtGui.QMenu("Filesystem", parent = self)
		filesystem_menu.addAction(QtGui.QAction("Add Filesystem", filesystem_menu, triggered = self.addfilesystem_clicked))
		
		help_menu = QtGui.QMenu("Help", parent = self)
		help_menu.addAction(QtGui.QAction("About Twig", help_menu, triggered = self.abouttwig_clicked))
		help_menu.addAction(QtGui.QAction("About BooKeeping", help_menu, triggered = self.aboutbookeeping_clicked))
		help_menu.addAction(QtGui.QAction("About P.O.T.S", help_menu, triggered = self.aboutpots_clicked))
		
		self.addAction(twig_menu.menuAction())
		self.addAction(filesystem_menu.menuAction())
		self.addAction(help_menu.menuAction())
	
	def preferences_clicked(self):
		pass
	
	def signout_clicked(self):
		pass
	
	def quit_clicked(self):
		global_variables.twig_signal.close_mainwindow.emit()
	
	def addfilesystem_clicked(self):
		global_variables.twig_signal.add_filesystem.emit()
	
	def abouttwig_clicked(self):
		pass
	
	def aboutbookeeping_clicked(self):
		pass
	
	def aboutpots_clicked(self):
		pass