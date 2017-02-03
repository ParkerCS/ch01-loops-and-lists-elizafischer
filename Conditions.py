#CONDITIONS (15PTS TOTAL)
from math import sqrt
# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.

# Dictionary
# List
def grader(percent):
    if (percent > 100):
        print(str("Sorry, that percent doesn't work."))
    elif percent >= 97:
        print("Grade: A+")
    elif percent >= 93:
        print("Grade: A")
    elif percent >= 90:
        print("Grade: A-")
    elif percent >= 87:
        print("Grade: B+")
    elif percent >= 83 :
        print("Grade: B")
    elif percent >= 80:
        print("Grade: B-")
    elif percent >= 77:
        print("Grade: C+")
    elif percent >= 73:
        print("Grade: C")
    elif percent >= 70:
        print("Grade: C-")
    elif percent >= 67:
        print("Grade: D+")
    elif percent >= 65:
        print("Grade: D")
    elif percent < 1:
        print("Sorry, that doesn't work.")
    else:
        print("Grade: F")


percent = float(input("Enter a grade percentage and the computer will tell you your letter grade:"))
grader(percent)

print("")
# PROBLEM 2 (Vowels - 5pts) ***
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.
'''
def find_vowel(user):
    vowel_count = 0
    if user.find("a"):
        vowel_count +=1
    elif user.find("e"):
        vowel_count += 1
    elif user.find("i"):
        vowel_count += 1
    elif user.find("o"):
        vowel_count += 1
    elif user.find("u"):
        vowel_count += 1
    print(vowel_count)
    print("There are", vowel_count, "different vowel(s) in this string.")

#user = print(input(str("Enter a string and the computer will tell you how many different vowels there are:")))
find_vowel(input(str("Enter a string and the computer will tell you how many different vowels there are:")))
#print("There are " , vowel_count , "different vowels in this string. They are," , vowel)

Doesn't work
'''

user = (str(input("Enter a string and the computer will tell you how many different vowels there are: ")))
total_vowels = []
for vowel in ["a", "e", "i", "o", "u"]:
    if vowel in user:
        total_vowels.append(vowel)

if len(total_vowels)== 1:
    print("There is 1 vowel in your phrase.")
else:
   print("There are", len(total_vowels), "different vowels in this string.")


print("")
# PROBLEM 3 (Quadratic Equation - 6pts) ****
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.
print("The quadratic formula calculator can solve equations in this form: Ax^2 + Bx + C = 0, where A, B and C are nonzero numbers.")
a = float(input("Enter a value for A:"))
b = float(input("Enter a value for B:"))
c = float(input("Enter a value for C:"))

value = ((b ** 2) - 4*(a)*(c))

if a == 0:
    print("No solutions.")
elif ((b ** 2) - 4*(a)*(c)) < 0:
    print("There are no real solutions.")
else:
    print("Solution 1 = ", ((b * -1) + ((sqrt((b**2) - (4*(a)*(c)) ))/ (2 * a) )))
    print("Solution 2 = ", ((b * -1) - ((sqrt((b**2) - (4*(a)*(c)) ))/ (2 * a) )))
if value == 0:
    print("There is One solution")
    solution1 = (((- b +(b ** 2) - 4*(a)*(c))) / 2*a)
