import PySide.QtGui as QtGui
import PySide.QtCore as QtCore

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(800, 600)
		self.setMinimumHeight(600)
		self.setMinimumWidth(800)
		
		self.central_widget = QtGui.QWidget()
		self.central_layout = QtGui.QGridLayout(self.central_widget)
		
		toolbar = QtGui.QFrame(self.central_widget)
		filesystem_list = QtGui.QListWidget(self.central_widget)
		filesystem_view = QtGui.QGraphicsView(self.central_widget)
		
		self.central_layout.addWidget(toolbar, 0, 0, 1, 2)
		self.central_layout.addWidget(filesystem_list, 1, 0)
		self.central_layout.addWidget(filesystem_view, 1, 1)
		
		toolbar.setFrameShape(QtGui.QFrame.StyledPanel)
		toolbar.setFrameShadow(QtGui.QFrame.Raised)
		
		self.central_layout.setColumnMinimumWidth(1, 600)
		self.central_layout.setColumnStretch(1, 2)
		self.central_layout.setHorizontalSpacing(0)
		self.central_layout.setRowMinimumHeight(0, 30)
		
		self.setCentralWidget(self.central_widget)
		
		
		
		
		
		self.menubar = QtGui.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menu_twig = QtGui.QMenu(self.menubar)
		self.menu_help = QtGui.QMenu(self.menubar)
		self.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(self)
		self.setStatusBar(self.statusbar)
		self.action_add_filesystem = QtGui.QAction(self)
		self.action_exit = QtGui.QAction(self)
		self.action_preferences = QtGui.QAction(self)
		self.action_sign_out = QtGui.QAction(self)
		self.action_about_twig = QtGui.QAction(self)
		self.action_about_bookeeping = QtGui.QAction(self)
		self.action_twig_help = QtGui.QAction(self)
		self.menu_twig.addAction(self.action_add_filesystem)
		self.menu_twig.addAction(self.action_preferences)
		self.menu_twig.addSeparator()
		self.menu_twig.addAction(self.action_sign_out)
		self.menu_twig.addAction(self.action_exit)
		self.menu_help.addAction(self.action_twig_help)
		self.menu_help.addSeparator()
		self.menu_help.addAction(self.action_about_twig)
		self.menu_help.addAction(self.action_about_bookeeping)
		self.menubar.addAction(self.menu_twig.menuAction())
		self.menubar.addAction(self.menu_help.menuAction())
		
		self.retranslateUi(self)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
		self.menu_twig.setTitle(QtGui.QApplication.translate("MainWindow", "Twig", None, QtGui.QApplication.UnicodeUTF8))
		self.menu_help.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
		self.action_add_filesystem.setText(QtGui.QApplication.translate("MainWindow", "Add Filesystem", None, QtGui.QApplication.UnicodeUTF8))
		self.action_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
		self.action_preferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
		self.action_sign_out.setText(QtGui.QApplication.translate("MainWindow", "Sign Out", None, QtGui.QApplication.UnicodeUTF8))
		self.action_about_twig.setText(QtGui.QApplication.translate("MainWindow", "About Twig", None, QtGui.QApplication.UnicodeUTF8))
		self.action_about_bookeeping.setText(QtGui.QApplication.translate("MainWindow", "About BooKeeping", None, QtGui.QApplication.UnicodeUTF8))
		self.action_twig_help.setText(QtGui.QApplication.translate("MainWindow", "Twig Help", None, QtGui.QApplication.UnicodeUTF8))

import sys
app = QtGui.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()