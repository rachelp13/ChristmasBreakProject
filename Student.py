class Student:
	name = ""
	daysAbsent = []
	overallGrade = 100.0
	studentId = 0
	assignmentGrades = []

	def __init__(self, name, studentId):
		self.name = name
		self.studentId = studentId
