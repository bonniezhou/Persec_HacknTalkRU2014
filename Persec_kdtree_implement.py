import csv
import math

radius = 0.03


class Node:
	def __init__(self, incident, x, y, left, right):
		self.incident = incident
		self.x = x
		self.y = y
		self.left = left
		self.right = right


#within_radius: Node Node -> bool
def within_radius(gps, crime):
	dist = math.sqrt((gps.x - crime.x)^2 + (gps.y - crime.y)^2)
	return dist < radius


#insert: Node Node bool -> void
def insert(root, newnode, flag):
	if root == None:
		root = newnode
	elif flag == True:
		if newnode.x < root.x:
			insert(root.left, newnode, !flag)
		else: 
			insert(root.right, newnode, !flag)
	else:
		if newnode.y < root.y:
			insert(root.left, newnode, !flag)
		else: 
			insert(root.right, newnode, !flag)
			

#build_tree: csv_file -> Node
def build_tree(csv_file):
	tree = None
	flag = True
	with open(crime_file, 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
			new = Node(int(row[0]), int(row[9]), int(row[10]), None, None)
			insert(tree, new, flag)
			flag = !flag
	return tree


def search(tree, gps_node):
	crimes = []
	if tree == None:
		return crimes
	elif within_radius(gps_node, tree):
		crimes.append(incident)
		tree = 
	
			
