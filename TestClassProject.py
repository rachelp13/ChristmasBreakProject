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

    def testClassSection_visualizeGrades(self):
        class1 = ClassSection("Class 1.1 @")
        for x in range(1, 40):
            newTestStudent = Student("Paul", x)
            newTestStudent.overallGrade = random.uniform(55.0, 100.0)
            class1.studentArray.append(newTestStudent)
        class1.visualizeGrades()


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
