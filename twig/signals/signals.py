import PySide.QtCore as QtCore

class TwigSignals(QtCore.QObject):
	#emit when the main window is supposed to close.
	close_mainwindow = QtCore.Signal()
	
	#emit when the add_filesystem dialog needs to be shown.
	add_filesystem = QtCore.Signal()
	
	#emit when an item in the filesytem list has been changed.
	filesystem_list_changed = QtCore.Signal(dict)
	
	#emit when the view is changed. Index contains the index of the current selected item.
	view_changed = QtCore.Signal(int)
	
	def __init__(self):
		QtCore.QObject.__init__(self)