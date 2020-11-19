"""
This is a quiz that sets the user's weather preferences

the higher the score the warmer someone tends to dress
"""

score = 0
# question 1: do you tend to run warm or cold?
question1 = input("Do you tend to run warm or cold? ")

while question1 != "cold" and question1 != "warm":
    print("Please answer either 'warm' or 'cold.")
    question1 = input("Are you from a warm climate or cold climate? Please answer either 'warm' or 'cold': ")
if question1 == "warm":
    score = score + 1
elif question1 == "cold":
    score = score + 2


# question 2: Warm or Cold Climate? Warm = dress lighter. Cold = dress heavier
question2 = input("Are you from a warm climate or cold climate? Please answer either 'warm' or 'cold': ")

while question2 != "cold" and question2 != "warm":
    print("Please answer either 'warm' or 'cold.")
    question2 = input("Are you from a warm climate or cold climate? Please answer either 'warm' or 'cold': ")
if question2 == "warm":
    score = score + 1
elif question2 == "cold":
    score = score + 2

# question 3: it's 60 degrees outside and sunny. What are they wearing?
question3 = input("It's 60 degrees out and sunny. Are you wearing A) a heavy sweater B) a light jacket or C) a tshirt?"
                  "Please answer either 'A' 'B' or 'C': ")

while question3 != "A" and question3 != "B" and question3 != "C":
    print("Please answer either 'A' 'B' or 'C'.")
    question1 = input("It's 60 degrees out and sunny. Are you wearing A) a heavy sweater B) a light jacket or C) a tshirt? ")
if question3 == "C":
    score = score + 1
elif question3 == "B":
    score = score + 2
elif question3 == "A":
    score = score + 3

#quiz results
if score == 3:
    print("Shorts in the winter? That has your name all over it.")
elif score == 7:
    print("There are never enough layers for you.")
else:
    print("You're in the middle.")