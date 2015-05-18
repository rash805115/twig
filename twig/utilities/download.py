import PySide.QtCore as QtCore
import urllib.request as request

class Download():
	def download(url):  # @NoSelf
		data = request.urlopen(url).read()
		return QtCore.QByteArray(data)