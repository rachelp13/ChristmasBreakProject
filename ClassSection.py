<<<<<<< Updated upstream
import numpy as np
import matplotlib.pyplot as plt
import helperFunctions 
from collections import OrderedDict

class ClassSection:
    studentArray = []
    assignmentArray = []
    name = ""

    def __init__(self, name):
        self.name = name

    def visualizeGrades(self):
        gradesArray = [("A+", 0), ("A", 0), ("A-", 0),
                              ("B+", 0), ("B", 0), ("B-", 0),
                              ("C+", 0), ("C", 0), ("C-", 0),
                              ("D+", 0), ("D", 0), ("D-", 0),
                              ("F", 0)]

        gradesArray.reverse()
        grades = OrderedDict(gradesArray)

        for student in self.studentArray:
            currentGrade = student.overallGrade
            grades[helperFunctions.getGradeString(currentGrade)] += 1

        y_pos = np.arange(len(grades.values()))

        plt.bar(y_pos, grades.values(), align='center', alpha=0.5)
        plt.xticks(y_pos, grades.keys())
        plt.ylabel('Students')
        plt.xlabel('Grade')
        plt.title('Class Grades')

        plt.show()

=======
from Student import Student

class ClassSection:
	studentArray = []
	assignmentArray = []
	name = ""
	
	def __init__(self, name):
		self.name = name

	def addStudent(self, name, studentId):
		newStudent = Student(name, studentId)
		self.studentArray.append(newStudent)

	def printStudents(self):
		for x in self.studentArray:
			print(x)

	def removeStudent(self, studentId):
		studentRemoved = 0
		for x in self.studentArray:
			if studentId == x.studentId:
				studentRemoved = x
		self.studentArray.remove(studentRemoved)
				
>>>>>>> Stashed changes


