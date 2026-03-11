Student = str(input("What is the student's name"))
Subject = str(input("What is the subject"))
Score = int(input("Insert test score"))  + int(input("Insert exam score"))

if Score >100:
	print("Please input a correct value")
elif Score >=70:
	print(Student, "grade is A in", Subject)
elif Score >= 60:
	print(Student, "grade is B in", Subject)
elif Score >=50:
	print(Student, "grade is C in", Subject)
elif Score >=45:
	print(Student, "grade is D in", Subject)
elif Score >=0:
	print(Student, "grade is F in", Subject)
elif Score <0:
	print("Please input a correct value")
