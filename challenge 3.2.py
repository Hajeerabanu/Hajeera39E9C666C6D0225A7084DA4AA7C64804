class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  #sort theist of students in descending order of CGPA
   sorted_students = sorted(student_list,
                            key=lambda  student: student.cgpa,reverse=True)
   return sorted_students


#example usage
students=[
    Student("hari","A123",7.8),
    Student("sam","A124",8.7),
    Student("seeman","A125",7.0),
    Student("siva","A126",8.8),
]

sorted_students=sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("name: {},roll_ number: {},CGPA: {}".format(student.name,
                                              student.roll_number,
                                                                             student.cgpa))
  

