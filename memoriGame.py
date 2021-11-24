import random
import casioplot as scr
#21 char 6/8

difficulty = 0
NBDigit = 0
lose = False

def delay(x) :
	for _ in range(x):
		pass

def Game():
    drawChar(54,24,"-3-")
    delay(50000)
    drawChar(54,24,"-2-")
    delay(50000)
    drawChar(54,24,"-1-")
    delay(50000)

    Gride = [
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    ]
    
    NBDigit = 5 + 1*difficulty

    ValG = []

    for n in range(NBDigit):
        flag = True
        x=0
        y=0
        while flag:
            x = random.randint(0,20)
            y = random.randint(0,5)
            if Gride[y][x] == " ":
                if x != 20 or y != 0:
                    flag = False

        Gride[y][x] = str(n)
        ValG.append((x,y,str(n)))

    ValR = []

    while len(ValG) > 0: #shuffle
        j = random.randint(0,len(ValG)-1)
        ValR.append(ValG[j])
        ValG.pop(j)

    for i in range(len(ValR)):
        drawChar(ValR[i][0]*6,ValR[i][1]*8,ValR[i][2])
        delay(50000)

    rep = ValR[random.randint(0,len(ValR)-1)][2]

    for i in range(6):
        for j in range(21):
            if Gride[i][j] == " ":
                print(" ", end="")
            elif Gride[i][j] == rep:
                print("?", end="")
            else:
                print("#", end="")
        print("")

    res = input(" : ")

    if res == rep :
        print("\n\n\n\nWOU WIN !!\n\n")
    else:
        print("\n\n\n\nYOU LOSE ...\n")
        print("YOUR SCORE : " + str(difficulty))
        global lose
        lose = True
        

def drawChar(x,y,t):
    scr.clear_screen()
    scr.draw_string(x, y, t, (0,0,0), "large")
    scr.show_screen()


while lose == False:
    Game()
    difficulty +=1