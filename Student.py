class Student :
    def __init__(self,Grades,Sentence):
        self.Grades = Grades
        self.Sentence = Sentence
    def printObject(self):
        print("Your childs grades are",self.Grades)
        print(self.Sentence)

Daksh = Student("A+","Does best in math and science both")

Daksh.printObject()