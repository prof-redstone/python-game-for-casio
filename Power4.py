gride = [
    ["","","","","","",""],
    ["","","","","","",""],
    ["","","","","","",""],
    ["","","","","","",""],
    ["","","","","","",""],
    ["","","","","","",""]
]
J1Char = 'O'
J2Char = 'X'
playerRound = "1" 
end = False
win = False

def GetInput():
    inp = input("")
    try:
        inp = int(inp)
    except ValueError:
        DrawGride(False)
        inp = GetInput()

    if inp < 1 or inp > 7:
        DrawGride(False)
        inp = GetInput()

    return inp

def DrawGride(win):
    print("")
    for i in range(6):
        for j in range(7):
            if gride[i][j] != "":
                print(gride[i][j], end=" ")
            else:
                print("-",end=" ")
        if i == 1:
            print(" P1 : " + J1Char,end="")
        if i == 2:
            print(" P2 : " + J2Char,end="")
        if win == False:
            if i == 5:
                print(" P" + playerRound + " :",end="")
        else:
            if i == 4:
                print(" P" + playerRound + " WIN",end="")
            if i == 5:
                print(" GAME",end="")
        print("")
    if win == False:
        print("1 2 3 4 5 6 7 ",end=" ")

while end == False:
    
    DrawGride(False)

    flag = True
    while flag:
        inp = GetInput()
        if gride[0][inp-1] == "":
            flag = False
        else:
            DrawGride(False)

    #fill the value in the gride
    for i in range(6):
        if gride[5-i][inp-1] == "":
            if playerRound == "1":
                gride[5-i][inp-1] = J1Char
            else:
                gride[5-i][inp-1] = J2Char
            break

    #printing
    DrawGride(False)

    #calculating the win
    
    for i in range(0,4): #horisontal line
        for j in range(0,6):
            if gride[j][i] == gride[j][i+1] == gride[j][i+2] == gride[j][i+3] != "":
                win = True
    
    for i in range(0,7): #vertical line
        for j in range(0,3):
            if gride[j][i] == gride[j+1][i] == gride[j+2][i] == gride[j+3][i] != "":
                win = True
    
    for i in range(0,4): #diagonal to top right line
        for j in range(0,3):
            if gride[j][i] == gride[j+1][i+1] == gride[j+2][i+2] == gride[j+3][i+3] != "":
                win = True
    
    for i in range(0,4): #diagonal to top right line
        for j in range(0,3):
            if gride[j][i+3] == gride[j+1][i+2] == gride[j+2][i+1] == gride[j+3][i] != "":
                win = True

    if win:
        DrawGride(win)
        #print("PLAYER " + playerRound + " WIN GAME")
        end = True

    #equality
    count = 0
    for i in range(0,7): #horisontal line
        for j in range(0,6):
            if gride[j][i] == "":
                count += 1

    if count == 0:
        print("\n EQUALITY !!\n")
        end = True
                
    #change player round
    if playerRound == "1" :
        playerRound = "2"
    else :
        playerRound = "1"