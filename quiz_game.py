print("WELCOME TO MY QUIZ")

playing = input("DO YOU WANT TO PLAY QUIZ?  " )
if playing.lower() != "yes":
    quit()

print("okay lets play!")
score = 0

answer = input("what does the word ipo stands for?   ")
if answer.lower() == "initial public offering":
    print("correct")
    score += 1
else: 
    print("incorrect")

answer = input("what does the word https stands for?   ")
if answer.lower() == "hypertext transfer protocol secure":
    print("correct")
    score += 1
else: 
    print("incorrect")


answer = input("what is the another name of arabh shah?   ")
if answer.lower() == "kana mama":
    print("correct")
    score += 1
else: 
    print("incorrect")


answer = input("what is the favorite thing of mantu kr singh?   ")
if answer.lower() == "fal ka thela":
    print("correct")
    score += 1
else: 
    print("incorrect")



answer = input("what does the word gpo stands for?   ")
if answer.lower() == "general post office":
    print("correct")
    score += 1
else: 
    print("incorrect")



answer = input("who is ceo of google?   ")
if answer.lower() == "sundar pichai":
    print("correct")
    score += 1
else: 
    print("incorrect")



answer = input("who is the prime minister of india?   ")
if answer.lower() == "narendra modi":
    print("correct")
    score += 1
else: 
    print("incorrect")



answer = input("who is the ceo of microsoft?   ")
if answer.lower() == "satya nadella":
    print("correct")
    score += 1
else: 
    print("incorrect")
print("you have got "  + str(score) + " questions correct " )
print("thank you")
