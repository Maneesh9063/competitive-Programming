class Node():
	def __init__(self,data):
		self.data = data
		self.next_node=None


class Single_linked_List(object):
	"""docstring for Single_linked_List"""
	def __init__(self):
		super(Single_linked_List, self).__init__()
		# self.arg = arg
		self.head=None

	def insert_(self,Node):
		if self.head == None:
			self.head=Node
		else:
			x=self.head
			while  x.next_node != None:
				x=x.next_node
			x.next_node = Node
	def get(self):
		if self.head ==None:
			print("empty")
		x=self.head
		while  x.next_node != None:
			print(str(x.data)+"-->",end='')
			x=x.next_node
		print(str(x.data))	
	def pop_(self):
		if self.head ==None:
			print("empty")
		x=self.head
		else:
			while  x.next_node.next_node != None:
				if self.head ==None:
					print("empty")
					break
				x=x.next_node
			x.next_node=None



a = Node(2)
c= Node(4)
v=Node('hi')
b=Single_linked_List ()
b.insert_(a)
b.insert_(c) 
b.insert_(v)
b.get()
b.pop_()
b.get()
b.pop_()
b.get()
b.pop_()
b.get()




