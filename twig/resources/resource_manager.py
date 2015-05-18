import PySide.QtGui as QtGui
import utilities.singleton
import resources.general_resources
import resources.component_resources
import resources.toolbar_resources

class ResourceManager(metaclass = utilities.singleton.Singleton):
	_resource_mapping = {
		"logo": ":/general/images/logo_transparent.png",
		"google_signin": ":/general/images/google_signin.png",
		"facebook_signin": ":/general/images/facebook_signin.gif",
		
		"blue_directory_close": ":/components/images/blue_directory_close.png",
		"blue_directory_open": ":/components/images/blue_directory_open.png",
		"green_directory_close": ":/components/images/green_directory_close.png",
		"green_directory_open": ":/components/images/green_directory_open.png",
		"yellow_directory_close": ":/components/images/yellow_directory_close.png",
		"yellow_directory_open": ":/components/images/yellow_directory_open.png",
		"red_directory_close": ":/components/images/red_directory_close.png",
		"red_directory_open": ":/components/images/red_directory_open.png",
		"blue_file": ":/components/images/blue_file.png",
		"green_file": ":/components/images/green_file.png",
		"yellow_file": ":/components/images/yellow_file.png",
		"red_file": ":/components/images/red_file.png",
		
		"exit": ":/toolbar/images/exit.png",
		"filesystem": ":/toolbar/images/filesystem.png",
		"permanent_delete": ":/toolbar/images/permanent_delete.png",
		"temporary_delete": ":/toolbar/images/temporary_delete.png",
		"settings": ":/toolbar/images/settings.png",
		"signout": ":/toolbar/images/signout.png",
		"uploading": ":/toolbar/images/uploading.png"
	}
	
	def __init__(self):
		resources.general_resources.qInitResources()
		resources.component_resources.qInitResources()
		resources.toolbar_resources.qInitResources()
	
	def get_resource(self, resource_name):
		if(resource_name not in self._resource_mapping):
			return None
		
		pixmap = QtGui.QPixmap(self._resource_mapping[resource_name])
		return pixmap