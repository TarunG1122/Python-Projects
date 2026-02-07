print("Welcome to my computer quiz!")


playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay ! let's play :)")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
    print(f"Score: {score}")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTML stand for? ").lower()
if answer == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTTP stand for? ").lower()
if answer == "hypertext transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your score:", score, "/5")
