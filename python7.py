#25
x = 1
while (x < 300):
    print x
    x = x + 2
#25
myFirstList = [12,6,8,32,69,69, "bug off wanker", 3,4,2,7,8,"lol 69"]
index = 0
while (index <len(myFirstList)):
    print myFirstList[index]
    index = index + 1
#50
import random
rand = random.randint(0,  50)
userInput = -1
print "Guess a number"
while (userInput != rand):
    userInput = int(raw_input())
    if (userInput < rand):
        print "too low"
    if (userInput > rand):
        print "too high"
    if (userInput == rand):
        print "congratulations!"