# 🚨 Don't change the code below 👇
student_scores = input("Enter number: ").split()
for num in range(0, len(student_scores)):
  student_scores[num] = int(student_scores[num])
print(student_scores)  
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0
for x in student_scores:
  if x > highest_score:
    highest_score = x
print(highest_score)  


