score = input("Enter score: ")
score = int(score)
if score > 80 or score == 80:
	grade = 'A'
elif score >= 70:
	grade = 'B'
elif score >= 55:
	grade = 'C'
elif score > 50 or score == 50:
	grade = 'Pass'
else:
	grade = 'Fail' 
print ("\n\nGrade is: " + grade)
