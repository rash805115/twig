class Coordinates():
	def top_left(graphics_item):  # @NoSelf
		return (graphics_item.boundingRect().topLeft().x(), graphics_item.boundingRect().topLeft().y())
	
	def top_right(graphics_item):  # @NoSelf
		return (graphics_item.boundingRect().topRight().x(), graphics_item.boundingRect().topRight().y())
	
	def bottom_left(graphics_item):  # @NoSelf
		return (graphics_item.boundingRect().bottomLeft().x(), graphics_item.boundingRect().bottomLeft().y())
	
	def bottom_right(graphics_item):  # @NoSelf
		return (graphics_item.boundingRect().bottomRight().x(), graphics_item.boundingRect().bottomRight().y())
	
	def top_mid(graphics_item):  # @NoSelf
		top_left = Coordinates.top_left(graphics_item)
		top_right = Coordinates.top_right(graphics_item)
		return ((top_left[0] + top_right[0]) / 2, top_left[1])
	
	def bottom_mid(graphics_item):  # @NoSelf
		bottom_left = Coordinates.bottom_left(graphics_item)
		bottom_right = Coordinates.bottom_right(graphics_item)
		return ((bottom_left[0] + bottom_right[0]) / 2, bottom_left[1])
	
	def left_mid(graphics_item):  # @NoSelf
		top_left = Coordinates.top_left(graphics_item)
		bottom_left = Coordinates.bottom_left(graphics_item)
		return (top_left[0], (top_left[1] + bottom_left[1]) / 2)
	
	def right_mid(graphics_item):  # @NoSelf
		top_right = Coordinates.top_right(graphics_item)
		bottom_right = Coordinates.bottom_right(graphics_item)
		return (top_right[0], (top_right[1] + bottom_right[1]) / 2)