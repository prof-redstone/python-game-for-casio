import random

global Code
global Gride 
global GameOn
playAgain = True

def GetCode():
    a = 0
    b = 0
    c = 0
    d = 0
    while a==b or a==c or a==d or b==c or b==d or c==d :
        a = random.randint(1,9)
        b = random.randint(1,9)
        c = random.randint(1,9)
        d = random.randint(1,9)
    return (a,b,c,d)

def Score(index, Gride, Code) :
    val = Gride[index]
    B=0
    M=0

    if val == (0,0,0,0):
        return "B M"

    for i in range(4):
        if val[i] == Code[i]:
            B+=1
        else :
            for j in range(4):
                if val[i] == Code[j]:
                    M+=1
    return str(B)+ " "+str(M)

def Game():
    Code = GetCode()
    Gride = [(0,0,0,0)]
    GameOn = True
    Try = 0
    while GameOn:
        print("\n\n\n\n\n\n")
        print("  MasterMind !")
        print(" ")
        for i in range(len(Gride)):
            print()
            print("  -" + str(Gride[i][0]) + str(Gride[i][1]) + str(Gride[i][2]) + str(Gride[i][3]) + "- " + Score(i, Gride, Code), end='')

        print("  try : " + str(Try))
        inp = input("\n : ")
        
        Vinput = True
        if len(inp) >= 4 :
            for i in range(4):
                if inp[i] != "1" and inp[i] != "2" and inp[i] != "3" and inp[i] != "4" and inp[i] != "5" and inp[i] != "6" and inp[i] != "7" and inp[i] != "8" and inp[i] != "9":
                    Vinput = False
        else:
            Vinput = False

        if Vinput :
            Try += 1
            val = (int(inp[0]),int(inp[1]),int(inp[2]),int(inp[3]))
            Gride.append(val)

        if Score(len(Gride) - 1, Gride, Code) == "4 0":
            print("\n\n\n\n\n\n  YOU WIN ! ")
            print("  Code : " + str(inp) + "\n")
            GameOn = False
            retry = input("play again : ")
            if retry == "0" or retry == "" or retry == "no":
                global playAgain 
                playAgain = False
        
        if inp == "code":
            Gride.append(Code)

while playAgain:
    Game()