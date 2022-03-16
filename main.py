
student_scores = input("Enter number: ").split()
for num in range(0, len(student_scores)):
  student_scores[num] = int(student_scores[num])
print(student_scores)  


highest_score = 0
average_all = 0
for x in student_scores:
  average_all +=1
  if x > highest_score:
    highest_score = x
    result = highest_score / average_all
print(highest_score) 
print(average_all)
print(result)

sum_of_even = 0
for even_nume in range(0,101):
  if even_nume % 2==0:
    sum_of_even += even_nume
print(sum_of_even)    