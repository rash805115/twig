import resources.resource_manager
import PySide.QtGui as QtGui

class File(QtGui.QGraphicsPixmapItem):
	def __init__(self, view, position = (0, 0), parent = None):
		super(File, self).__init__(parent)
		self.resource_manager = resources.resource_manager.ResourceManager()
		
		self.setScale(0.3)
		self.setOffset(position[0], position[1])