def marksandcredit(n, p):
    subject = float(n / p)
    gpa = subject
    print("Now we calculate the grade.")
    if gpa >= 80 and gpa <= 100:
        grade = 4.00
    elif gpa >= 75 and gpa < 80:
        grade = 3.75
    elif gpa >= 70 and gpa < 75:
        grade = 3.50
    elif gpa >= 65 and gpa < 70:
        grade = 3.25
    elif gpa >= 60 and gpa < 65:
        grade = 3.00
    elif gpa >= 55 and gpa < 60:
        grade = 2.75
    elif gpa >= 50 and gpa < 55:
        grade = 2.50
    elif gpa >= 40 and gpa < 50:
        grade = 2.00
    else:
        grade = 0.00

    X = grade * p
    return X


print("This is how we make a CGPA calculator.")
print("What is your marks and credit for Subject 1?")


mark_1 = float(input("marks:"))
credit_1 = float(input("Credit:"))

A = marksandcredit(mark_1, credit_1)
print("This is the product of credit and grade for subject 1.")
print(A)

print("What is your marks and credit for Subject 2?")

mark_2 = float(input("marks:"))
credit_2 = float(input("Credit:"))

B = marksandcredit(mark_2, credit_2)
print("This is the product of credit and grade for subject 2.")
print(B)

print("What is your marks and credit for Subject 3?")

mark_3 = float(input("marks:"))
credit_3 = float(input("Credit:"))

C = marksandcredit(mark_3, credit_3)
print("This is the product of credit and grade for subject 3.")
print(C)

print("What is your marks and credit for Subject 4?")

mark_4 = float(input("marks:"))
credit_4 = float(input("Credit:"))

D = marksandcredit(mark_4, credit_4)
print("This is the product of credit and grade for subject 4.")
print(D)

print("What is your marks and credit for Subject 5?")

mark_5 = float(input("marks:"))
credit_5 = float(input("Credit:"))

E = marksandcredit(mark_5, credit_5)
print("This is the product of credit and grade for subject 5.")
print(E)

print("What is your marks and credit for Subject 6?")

mark_6 = float(input("marks:"))
credit_6 = float(input("Credit:"))

F = marksandcredit(mark_6, credit_6)
print("This is the product of credit and grade for subject 6.")
print(F)

total_credits = credit_1 + credit_2 + credit_3 + credit_4 + credit_5 + credit_6
Cgpa = (A + B + C + D + E + F) / (total_credits)
print("Your full cgpa value is %r" % (Cgpa))