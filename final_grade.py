score1 = int(input("Enter the score of exam1: "))
score2 = int(input("Enter the score of exam2: "))
score3 = int(input("Enter the score of exam3: "))
average_score = (score1 + score2 + score3) / 3

if average_score >= 90:
    print("Final grade: A")
if average_score >= 80 and average_score <= 89:
    print("Final grade: B")
if average_score >= 70 and average_score <= 79:
    print("Final grade: C")
if average_score >= 60 and average_score <= 69:
    print("Final grade: D")
if average_score < 60:
    print("Final grade: F")
