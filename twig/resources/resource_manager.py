import PySide.QtGui as QtGui
import utilities.singleton
import resources.general_resources
import resources.component_resources

class ResourceManager(metaclass = utilities.singleton.Singleton):
	_resource_mapping = {
		"logo": ":/images/images/logo_transparent.png",
		"directory_close": ":/components/images/directory_close_transparent.png",
		"directory_open": ":/components/images/directory_open_transparent.png",
		"file": ":/components/images/general_file_transparent.png"
	}
	
	def __init__(self):
		resources.general_resources.qInitResources()
		resources.component_resources.qInitResources()
	
	def get_resource(self, resource_name, scale = True):
		if(resource_name not in self._resource_mapping):
			return None
		
		pixmap = QtGui.QPixmap(self._resource_mapping[resource_name])
		if scale is True:
			pixmap = pixmap.scaledToWidth(50)
		return pixmap