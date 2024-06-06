class Marks_calculation:

    def __init__(self, marks) -> None:
        self.marks = marks
        self.grade = ""

    def calculate_total_marks(self):
        self.total_marks = sum(self.marks)

    def calculate_persentage(self):
        self.percentage = self.total_marks/5
    
    def subject_grade(self):
        for mark in self.marks:
            if mark < 50:
                print("Subject1", mark, "D")
            
            elif mark > 50 and mark <= 60:
                print("Subject2", mark, "C")
            
            elif mark > 60 and mark <= 80:
                print("Subject3", mark, "B")
            
            else:
                print("Subject4", mark, "A")

    def calculate_grade(self):
        if self.percentage < 50:
            self.grade = "D"

        elif self.percentage > 50 and self.percentage <= 60:
            self.grade = "C"

        elif self.percentage > 60 and self.percentage <=80:
            self.grade = "B"

        else:
            self.grade = "A"

    def result(self):
        print("Total Marks: ", self.total_marks, "/", "500")
        print("Persentage: ", self.percentage)
        print("Grade", self.grade)

marks = []      
for val in range(1, 6):
    marks.append(int(input("Enter the marks: ")))

marks_obj = Marks_calculation(marks)

marks_obj.calculate_total_marks()
marks_obj.calculate_persentage()
marks_obj.calculate_grade()
marks_obj.subject_grade()
marks_obj.result()