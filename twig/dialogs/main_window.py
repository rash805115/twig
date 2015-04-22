import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
from dialogs.mainview.defaultview import DefaultView

class ItemList(QtGui.QListWidget):
	_stylesheet = """
		QListWidget {
			font-family: "Lucida Grande", Verdana, Helvetica, Arial, sans-serif;
			font-size: 14px;
			background-color: #a6a6a6;
		}
		
		QListWidget::item {
			color: #a6a6a6;
			background-color: white;
			padding-top: 10px;
			padding-bottom: 10px;
			border-bottom: 1px solid black;
		}
		
		QListWidget::item:selected {
			color: white;
			background-color: #5abae1;
		}
		
		QListWidget::item:focus {
			border: 0px;
		}
	"""
	
	def __init__(self, widget):
		QtGui.QListWidget.__init__(self, widget)
		self.setStyleSheet(self._stylesheet)
		self.setFocusPolicy(QtCore.Qt.NoFocus)

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.resize(800, 600)
		self.setMinimumHeight(600)
		self.setMinimumWidth(800)
		
		self.central_widget = QtGui.QWidget()
		self.central_layout = QtGui.QGridLayout(self.central_widget)
		
		toolbar = QtGui.QFrame(self.central_widget)
		toolbar.setFrameShape(QtGui.QFrame.StyledPanel)
		toolbar.setFrameShadow(QtGui.QFrame.Raised)
		filesystem_list = ItemList(self.central_widget)
		filesystem_list.setSortingEnabled(True)
		filesystem_view = DefaultView(self.central_widget)
		
		
		QtGui.QListWidgetItem("The Mountain", filesystem_list)
		QtGui.QListWidgetItem("Rash Splash", filesystem_list)
		QtGui.QListWidgetItem("Honey Bunny", filesystem_list)
		QtGui.QListWidgetItem("File-System 4", filesystem_list)
		QtGui.QListWidgetItem("File-System 5", filesystem_list)
		QtGui.QListWidgetItem("File-System 6", filesystem_list)
		
		self.central_layout.addWidget(toolbar, 0, 0, 1, 2)
		self.central_layout.addWidget(filesystem_list, 1, 0)
		self.central_layout.addWidget(filesystem_view, 1, 1)
		
		self.central_layout.setColumnMinimumWidth(1, 600)
		self.central_layout.setColumnStretch(1, 2)
		self.central_layout.setHorizontalSpacing(0)
		self.central_layout.setRowMinimumHeight(0, 30)
		
		self.setCentralWidget(self.central_widget)
		
		filesystem_list.itemSelectionChanged.connect(self.change_filesystem)
		
		
		
		
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
	
	def change_filesystem(self):
		print("Changing item")

import sys
app = QtGui.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()