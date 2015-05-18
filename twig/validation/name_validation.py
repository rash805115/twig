import re

class NameValidation():
	def validate_name(name):  # @NoSelf
		name_pattern = re.compile('^[a-zA-Z0-9_\- ]+$')
		if re.match(name_pattern, name) is not None:
			return True
		else:
			return False
	
	def validate_commit(name):  # @NoSelf
		name_pattern = re.compile('^[a-zA-Z0-9_\- ]+$')
		if re.match(name_pattern, name) is not None:
			return True
		else:
			return False