import unittest
import random

from ClassSection import ClassSection
from Student import Student
from Assignment import Assignment

class TestClassProject(unittest.TestCase):

    def testClassSection_Creation(self):
        class1 = ClassSection("Class 1.1 @")
        self.assertEqual(class1.name, 'Class 1.1 @')
        class2 = ClassSection("12345")
        self.assertEqual(class2.name, '12345')

<<<<<<< Updated upstream
    def testClassSection_visualizeGrades(self):
        class1 = ClassSection("Class 1.1 @")
        for x in range(1, 40):
            newTestStudent = Student("Paul", x)
            newTestStudent.overallGrade = random.uniform(55.0, 100.0)
            class1.studentArray.append(newTestStudent)
        class1.visualizeGrades()

=======
    def testClassSection_printStudents(self):
    	class1 = ClassSection("Class1")
    	class1.addStudent("George", 123)
    	class1.addStudent("Paul", 124)
    	class1.addStudent("Ringo", 125)
    	class1.addStudent("John", 126)
    	class1.printStudents()

    def testClassSection_addStudent(self):
    	class1 = ClassSection("Class1")
    	class1.addStudent("George", 123)
    	self.assertEqual(class1.studentArray[0].name, "George")
    	self.assertEqual(class1.studentArray[0].studentId, 123)
    	self.assertEqual(len(class1.studentArray), 1)
    	class1.addStudent("Paul", 122)
    	self.assertEqual(class1.studentArray[1].name, "Paul")
    	self.assertEqual(class1.studentArray[1].studentId, 122)
    	self.assertEqual(len(class1.studentArray), 2)



    def testClassSection_removeStudent(self):
    	class2 = ClassSection("Class2")
    	class2.addStudent("George", 123)
    	class2.addStudent("Paul", 124)
    	class2.addStudent("Ringo", 125)
    	class2.addStudent("John", 126)
    	class2.addStudent("Yoko", 122)
    	self.assertEqual(len(class2.studentArray), 5)
    	class2.removeStudent(122)
    	self.assertEqual(len(class2.studentArray), 4)
>>>>>>> Stashed changes

    def testStudent_Creation(self):
        student1 = Student("George", 12345)
        self.assertEqual(student1.name, 'George')
        self.assertEqual(student1.studentId, 12345)
        student2 = Student("Paul", 12323)
        self.assertEqual(student2.name, 'Paul')
        self.assertEqual(student2.studentId, 12323)

    def testAssignment_Creation(self):
        assign1 = Assignment(20.5, "Numbers", 12312, 50.0)
        self.assertEqual(assign1.weight, 20.5)
        self.assertEqual(assign1.name, "Numbers")
        self.assertEqual(assign1.assignmentId, 12312)
        self.assertEqual(assign1.totalPossiblePoints, 50.0)
        assign2 = Assignment(15.0, "Random", 123, 23.2)
        self.assertEqual(assign2.weight, 15.0)
        self.assertEqual(assign2.name, "Random")
        self.assertEqual(assign2.assignmentId, 123)
        self.assertEqual(assign2.totalPossiblePoints, 23.2)



if __name__ == '__main__':
    unittest.main()
