import PySide.QtGui as QtGui

class Menu(QtGui.QMenu):
	def __init__(self, menubar, name):
		QtGui.QMenu.__init__(self, menubar)
		self.setTitle(name)
	
	def add_action(self, name, action):
		action.setText(name)
		self.addAction(action)