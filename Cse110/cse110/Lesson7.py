grade = int(input("Insert percentage"))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

sign = ""

l= grade % 10

if l >= 7:
    sign = "+"
elif l < 3:
    sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""


if letter == "F":
    sign = ""

print(f"Your letter grade is: {letter}{sign}")

if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")