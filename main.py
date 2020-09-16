# Author: John Sweetall jts6052@psu.edu

gradepoint1 = 0.0
gradepoint2 = 0.0
gradepoint3 = 0.0

part1 = input("Enter your course 1 letter grade: ");
credit1 = int(input("Enter your course 1 credit: "))
if part1 == "A":
  gradepoint1 = 4.0
elif part1 == "A-":
  gradepoint1 = 3.67
elif part1 == "B+":
  gradepoint1 = 3.33
elif part1 == "B":
  gradepoint1 = 3.0
elif part1 == "B-":
  gradepoint1 = 2.67
elif part1 == "C+":
  gradepoint1 = 2.33
elif part1 == "C":
  gradepoint1 = 2.0
elif part1 == "D":
  gradepoint1 = 1.0
elif part1 == "F":
  gradepoint1 = 0.0
else:
  gradepoint1 = 0.0
print(f"Grade point for course 1 is: {gradepoint1}")

part2 = input("Enter your course 2 letter grade: ");
credit2 = int(input("Enter your course 2 credit: "))
if part2 == "A":
  gradepoint2 = 4.0
elif part2 == "A-":
  gradepoint2 = 3.67
elif part2 == "B+":
  gradepoint2 = 3.33
elif part2 == "B":
  gradepoint2 = 3.0
elif part2 == "B-":
  gradepoint2 = 2.67
elif part2 == "C+":
  gradepoint2 = 2.33
elif part2 == "C":
  gradepoint2 = 2.0
elif part2 == "D":
  gradepoint2 = 1.0
elif part2 == "F":
  gradepoint2 = 0.0
else:
  gradepoint2 = 0.0
print(f"Grade point for course 2 is: {gradepoint2}")

part3 = input("Enter your course 3 letter grade: ");
credit3 = int(input("Enter your course 3 credit: "))
if part3 == "A":
  gradepoint3 = 4.0
elif part3 == "A-":
  gradepoint3 = 3.67
elif part3 == "B+":
  gradepoint3 = 3.33
elif part3 == "B":
  gradepoint3 = 3.0
elif part3 == "B-":
  gradepoint3 = 2.67
elif part3 == "C+":
  gradepoint3 = 2.33
elif part3 == "C":
  gradepoint3 = 2.0
elif part3 == "D":
  gradepoint3 = 1.0
elif part3 == "F":
  gradepoint3 = 0.0
else:
  gradepoint3 = 0.0
print(f"Grade point for course 3 is: {gradepoint3}")

GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)  

print(f"Your GPA is: {GPA}")

