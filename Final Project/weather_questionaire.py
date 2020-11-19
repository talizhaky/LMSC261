"""
This is a quiz that sets the user's weather preferences

lower score = hotter-leaning
higher score = colder-leaning
"""

score = 0

# question 1: Warm or Cold Climate?
question1 = input("Are you from a warm climate or cold climate? Please answer either 'warm' or 'cold': ")

while question1 != "cold" and question1 != "warm":
    print("Please answer either 'warm' or 'cold.")
    question1 = input("Are you from a warm climate or cold climate? Please answer either 'warm' or 'cold': ")
if question1 == "cold":
    score = score + 1
elif question1 == "warm":
    score = score + 2

print(score)

# question 2: it's 60 degrees outside and sunny. What are they wearing?
question2 = input("It's 60 degrees out and sunny. Are you wearing A) a heavy sweater B) a light jacket or C) a tshirt?"
                  "Please answer either 'A' 'B' or 'C': ")

while question2 != "A" and question2 != "B" and question2 != "C":
    print("Please answer either 'A' 'B' or 'C'.")
    question1 = input("It's 60 degrees out and sunny. Are you wearing A) a heavy sweater B) a light jacket or C) a tshirt? ")
if question2 == "C":
    score = score + 1
elif question2 == "B":
    score = score + 2
elif question2 == "A":
    score = score + 3

print(score)

