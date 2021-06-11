class Node:
	def __init__(self, ntype, parent=None, children=[]):
		self.ntype = ntype
		self.parent = parent
		self.children = children
		if len(self.children) > 0:
			self.adopt_children()

	def adopt_children(self):
		for child in self.children:
			child.parent = self
