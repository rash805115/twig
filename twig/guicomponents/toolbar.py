import PySide.QtGui as QtGui

class Toolbar(QtGui.QFrame):
	def __init__(self, widget):
		QtGui.QFrame.__init__(self, widget)
		self.setFrameShape(QtGui.QFrame.StyledPanel)
		self.setFrameShadow(QtGui.QFrame.Raised)