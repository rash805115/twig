import PySide.QtCore as QtCore
import utilities.singleton

class TwigSignals(metaclass = utilities.singleton.Singleton):
	twig_signal = None
	
	def __init__(self):
		self.twig_signal = _TwigSignals()

class _TwigSignals(QtCore.QObject):
	#emit when the main window is supposed to close.
	close_mainwindow = QtCore.Signal()
	
	#emit when the add_filesystem dialog needs to be shown.
	add_filesystem = QtCore.Signal()
	
	#emit when an item in the filesytem list has been changed.
	filesystem_list_changed = QtCore.Signal(dict)
	
	def __init__(self):
		QtCore.QObject.__init__(self)