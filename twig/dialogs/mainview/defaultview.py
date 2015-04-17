import PySide.QtGui as QtGui

class View(QtGui.QGraphicsView):
	def __init__(self, parent = None):
		super(View, self).__init__(parent)
		