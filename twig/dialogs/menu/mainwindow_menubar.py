import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import dialogs.menu.menu as menu
import service.globals as global_variables
import signals.signals as signals

class MainWindowMenubar(QtGui.QMenuBar):
	def __init__(self, widget):
		QtGui.QMenuBar.__init__(self, widget)
		self.setNativeMenuBar(False)
		self.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.twig_signal = signals.TwigSignals().twig_signal
		
		twig_menu = menu.Menu(self, global_variables._app_name)
		twig_menu.add_action("Preferences", QtGui.QAction(self, triggered = self.preferences_clicked))
		twig_menu.addSeparator()
		twig_menu.add_action("Sign Out", QtGui.QAction(self, triggered = self.signout_clicked))
		twig_menu.add_action("Quit", QtGui.QAction(self, triggered = self.quit_clicked))
		
		filesystem_menu = menu.Menu(self, "Filesystem")
		filesystem_menu.add_action("Add Filesystem", QtGui.QAction(self, triggered = self.addfilesystem_clicked))
		
		help_menu = menu.Menu(self, "Help")
		help_menu.add_action("About Twig", QtGui.QAction(self, triggered = self.abouttwig_clicked))
		help_menu.add_action("About BooKeeping", QtGui.QAction(self, triggered = self.aboutbookeeping_clicked))
		help_menu.add_action("About P.O.T.S", QtGui.QAction(self, triggered = self.aboutpots_clicked))
		
		self.addAction(twig_menu.menuAction())
		self.addAction(filesystem_menu.menuAction())
		self.addAction(help_menu.menuAction())
	
	def preferences_clicked(self):
		pass
	
	def signout_clicked(self):
		pass
	
	def quit_clicked(self):
		self.twig_signal.close_mainwindow.emit()
	
	def addfilesystem_clicked(self):
		self.twig_signal.add_filesystem.emit()
	
	def abouttwig_clicked(self):
		pass
	
	def aboutbookeeping_clicked(self):
		pass
	
	def aboutpots_clicked(self):
		pass