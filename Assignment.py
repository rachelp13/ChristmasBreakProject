class Assignment:
	score = 0.0
	totalPossiblePoints = 100.0
	weight = 0.0
	name = ""
	assignmentId = 0

	def __init__(self, weight, name, assignmentId, totalPossiblePoints):
		self.weight = weight
		self.name = name
		self.assignmentId = assignmentId
		self.totalPossiblePoints = totalPossiblePoints
