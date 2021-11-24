import casioplot as scr
from random import *

table = [[[]for j in range(31)] for i in range(63)]

def init():
    for i in range(63):
        for j in range(31):
            x = random()
            if x > 0.5:
                table[i][j] = 1
            else:
                table[i][j] = 0



init()
def draw():
    scr.clear_screen()
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1:
                scr.set_pixel(i*2,j*2)
                scr.set_pixel(i*2+1,j*2)
                scr.set_pixel(i*2,j*2+1)
                scr.set_pixel(i*2+1,j*2+1)
    
    scr.show_screen()



def delay() :
	for _ in range(1000):
		if _ > 1000:
			return 1

for i in range(1000):
    draw()
    #copi
    table2 = [[[]for j in range(31)] for i in range(63)]
    for i in range(len(table)):
        for j in range(len(table[0])):
            table2[i][j] = table[i][j]
    
    for i in range(1, len(table2)-1):
        for j in range(1, len(table2[0])-1):
            v = table[i-1][j-1] + table[i][j-1] + table[i+1][j-1] + table[i+1][j] + table[i+1][j+1] + table[i][j+1] + table[i-1][j+1] + table[i-1][j]
            if table[i][j] == 0:
                if v == 3:
                    table2[i][j] = 1
            if table[i][j] == 1:
                if v == 3 or v == 2:
                    table2[i][j] = 1
                else:
                    table2[i][j] = 0

    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = table2[i][j]

    
