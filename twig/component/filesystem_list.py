import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import pybookeeping.core.communication.connection as connection
import pybookeeping.core.operation.filesystem as filesystem
import service.globals as global_variables
import component.filesystem_item as filesystem_item
import dialogs.add_filesystem as add_filesystem
import signals.signals as signals
import json
import functools

class FilesystemList(QtGui.QListWidget):
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
		self.setSortingEnabled(True)
		self.setStyleSheet(self._stylesheet)
		self.setFocusPolicy(QtCore.Qt.NoFocus)
		self.twig_signal = signals.TwigSignals().twig_signal
		
		self.twig_signal.add_filesystem.connect(self.create_new)
		self.itemSelectionChanged.connect(self.item_changed)
		
		self.filesystem = filesystem.Filesystem(connection.Connection())
		self.display_children()
	
	def display_children(self):
		for filesystem_info in self.filesystem.get_all_filesystem(global_variables._current_user):
			item_tooltip = json.dumps(filesystem_info, indent = 8)
			item = filesystem_item.FilesytemItem(filesystem_info, self)
			item.setToolTip(item_tooltip)
	
	def remove_children(self):
		while self.count() > 0:
			self.takeItem(0)
	
	def contextMenuEvent(self, event):
		menu = QtGui.QMenu()
		
		item = self.itemAt(event.x(), event.y())
		if item is None:
			menu.addAction(QtGui.QAction("Create New Filesystem", menu, triggered = self.create_new))
		else:
			menu.addAction(QtGui.QAction("Show Changes", menu, triggered = functools.partial(item.filesystem_change)))
			#menu.addAction(QtGui.QAction("Commit", menu, triggered = functools.partial(item.commit)))
		
		menu.exec_(QtGui.QCursor.pos())
	
	def create_new(self):
		add_dialog = add_filesystem.AddFilesystem()
		if add_dialog.exec_() == QtGui.QDialog.Accepted:
			self.remove_children()
			self.display_children()
	
	def item_changed(self):
		current_filesytem_info = self.currentItem().filesystem_info
		self.twig_signal.filesystem_list_changed.emit(current_filesytem_info)