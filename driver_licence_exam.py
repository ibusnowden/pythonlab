correct_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C",
                   "A", "D", "C", "B", "B", "D", "A"]

student_answers = ["D", "C", "A", "A", "D", "D", "C", "A", "A", "B",
                   "A", "D", "A", "D", "C", "C", "B", "A", "C"]

incorrect_answers = []
total_correct = 0
total_incorrect = 0

for i in range(len(correct_answers)):
    if student_answers[i] != correct_answers[i]
       incorrect_answers.append(i)
       total_incorrect += 1
    else:
      total_correct += 1
print()

if total_correct >= 15:
   print('The student passed')
else:
   print("The student did not pass")

print()
print(f"Total correct answers; {total_correct}")
print(f"Total incorrect answers: {total_incorrect}")

print(f"Incorrect question numbers; ", end='')
for i in range(len(incorrect_answers)):
    print(f"{incorrect_answers[i]+1}", end='' )