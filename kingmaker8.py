#!/usr/bin/python3
import random
i=0
def myroll():
	return random.randit(1,6)
while(i<=100):
	n=int(input("press r to roll the dice"))
	if(n=='r'):
		r=myroll()
		i=i+r
		print("new position is",i)
	if (i==3):
    	i=34
    	print("congrats u get a ladder to 34")
    elif (i==8):
    	i=37
    	print("congrats u get a ladder to 37")
    elif (i==40):
    	i=68
    	print("congrats u get a ladder to 68")
    elif (i==52):
    	i=81
    	print("congrats u get a ladder to 81")
    elif (i==76):
    	i=97
    	print("congrats u get a ladder to 97")
    elif (i==11):
    	i=2
    	print("sorry u got a snake down to 2")
    elif (i==25):
    	i=4
    	print("sorry u got a snake down to 4")
    elif (i==38):
    	i=9
    	print("sorry u got a snake down to 9")
    elif (i==65):
    	i=46
    	print("sorry u got a snake down to 46")
    elif (i==89):
    	i=70
    	print("sorry u got a snake down to 70")
    elif (i==93)
        i=64
        print("sorry u got a snake down to 64")