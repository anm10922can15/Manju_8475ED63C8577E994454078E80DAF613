class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa,reverse=True)
  return sorted_students

students = [Student("Dhanu", "22CA04",9.9),Student("Kaviya","22CA11",8.9),Student("Manju", "22CA15",9.7),Student("Monisha","22CA17",8.7),
           ]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))