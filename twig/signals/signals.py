import PySide.QtCore as QtCore
import utilities.singleton

class TwigSignals(metaclass = utilities.singleton.Singleton):
	twig_signal = None
	
	def __init__(self):
		self.twig_signal = _TwigSignals()

class _TwigSignals(QtCore.QObject):
	close_mainwindow = QtCore.Signal()
	add_filesystem = QtCore.Signal()
	
	def __init__(self):
		QtCore.QObject.__init__(self)