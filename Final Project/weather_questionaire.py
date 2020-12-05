"""
This is a quiz that sets the user's weather preferences

the higher the score the warmer someone tends to dress
"""

score = 0

question1 = input("Do you tend to run "
                  "A) warm "
                  "B) cold? ")
while question1 != "A" and question1 != "B":
    print("Please answer either 'A' or 'B.")
    question1 = input("Do you tend to run "
                      "A) warm "
                      "B) cold? ")
if question1 == "A":
    score = score + 1
elif question1 == "B":
    score = score + 2

question2 = input("Are you from a "
                  "A) colder climate "
                  "B) warmer climate? ")
while question2 != "A" and question2 != "B":
    print("Please answer either 'A' or 'B.")
    question2 = input("Are you from a "
                      "A) colder climate "
                      "B) warmer climate? ")
if question2 == "A":
    score = score + 1
elif question2 == "B":
    score = score + 2

question3 = input("It's 60 degrees out and sunny. Are you wearing "
                  "A) a t-shirt "
                  "B) a light jacket "
                  "C) a heavy sweater? "
                  )
while question3 != "A" and question3 != "B" and question3 != "C":
    print("Please answer either 'A' 'B' or 'C'.")
    question3 = input("It's 60 degrees out and sunny. Are you wearing "
                      "A) a t-shirt "
                      "B) a light jacket "
                      "C) a heavy sweater? ")
if question3 == "A":
    score = score + 1
elif question3 == "B":
    score = score + 2
elif question3 == "C":
    score = score + 3

question4 = input("At what temperature do you start wearing shorts instead of pants? "
                  "A) 60F "
                  "B) 70F "
                  "C) 80F ")
while question4 != "A" and question4 != "B" and question4 != "C":
    print("Please answer either 'A' 'B' or 'C'.")
    question4 = input("At what temperature do you start wearing shorts instead of pants? "
                      "A) 60F "
                      "B) 70F "
                      "C) 80F ")
if question4 == "A":
    score = score + 1
elif question4 == "B":
    score = score + 2
elif question4 == "C":
    score = score + 3

question5 = input("It’s pouring rain out, what do you do? "
                  "A) Nothing, I don't mind rain "
                  "B) A hood will do just fine "
                  "C) Bring an umbrella "
                  "D) I'm not going outside today ")
while question5 != "A" and question5 != "B" and question5 != "C" and question5 != "D":
    print("Please answer either 'A' 'B' or 'C'.")
    question5 = input("It’s pouring rain out, what do you do? "
                      "A) Nothing, I don't mind rain "
                      "B) A hood will do just fine "
                      "C) Bring an umbrella "
                      "D) I'm not going outside today ")
if question5 == "A":
    score = score + 1
elif question5 == "B":
    score = score + 2
elif question5 == "C":
    score = score + 3
elif question5 == "D":
    score = score + 4

print(score)