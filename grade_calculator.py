# Course weight
labs_weight = 20
quizzes_weight = 15
assignments_weight = 0.04
midterms_weight = 0.125
final_weight = 0.18
prep_weight = 0.06

# starting the course total at 0 and adding on
course_total = 0

# inputs and growth of course total
labs = float(input("Enter the number of labs completed: "))
if labs > 6:
    labs = 6

course_total += (labs/6 * labs_weight) # labs

quizzes = float(input("Enter the number of quizzes completed: "))
if quizzes > 6:
    quizzes = 6

course_total += (quizzes/6 * quizzes_weight) # labs & quizzes

ass_1 = float(input("Enter grade for Assignment 1: "))
ass_2 = float(input("Enter grade for Assignment 2: "))
ass_3 = float(input("Enter grade for Assignment 3: "))
ass_4 = float(input("Enter grade for Assignment 4: "))

course_total += ((ass_1 + ass_2 + ass_3 + ass_4) * assignments_weight) # labs, quizzes & assign.

midterm_1 = float(input("Enter grade for Midterm 1: "))
midterm_2 = float(input("Enter grade for Midterm2: "))

course_total += (midterm_1 * midterms_weight + midterm_2 * midterms_weight) # labs, quizzes, assign. & mid


final_exam = float(input("Enter grade for final exam: "))

course_total += (final_exam * final_weight) # labs, quizzes, assign., mid & final

prep = float(input("Enter grade for Midterms and Final Preparation: "))

course_total += (prep * prep_weight) # all the grades have been input

print("Your grade is:", round(course_total))



