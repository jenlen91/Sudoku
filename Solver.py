
from random import randint, seed
import click

Empty = click.style('-', fg='red')

mainboard = []
optboard = []
# for i in xrange(9):
# 	tmp=[]
# 	for j in xrange(9):
# 		tmp.append((j+1))
# 	mainboard.append(tmp)
def make_board(mainboard,r,c):
	for i in xrange(r):
		tmp=[]
		for j in xrange(c):
			tmp.append(Empty)
		mainboard.append(tmp)

def make_optboard(mainboard,r,c):
	for i in xrange(r):
		tmp=[]
		for j in xrange(c):
			tmp.append([1,2,3,4,5,6,7,8,9])
		mainboard.append(tmp)

def print_board(board):
    for rowNum, row in enumerate(board):#row = board[i] for all rows
        print "{}".format(" ".join(str(n) for n in row))

make_board(mainboard,9,9)

'''enter non-Empty values'''
#mainboard[row][column]=

mainboard[0]=[Empty,2,Empty,Empty,Empty,5,Empty,Empty,Empty]
mainboard[1]=[Empty,1,5,Empty,Empty,Empty,Empty,Empty,Empty]
mainboard[2]=[Empty,Empty,Empty,Empty,Empty,8,7,Empty,3]
mainboard[3]=[Empty,5,1,Empty,Empty,Empty,Empty,Empty,Empty]
mainboard[4]=[Empty,Empty,9,7,Empty,Empty,Empty,1,Empty]
mainboard[5]=[Empty,Empty,Empty,3,Empty,Empty,Empty,4,6]
mainboard[6]=[Empty,Empty,Empty,Empty,8,Empty,Empty,Empty,1]
mainboard[7]=[7,Empty,Empty,9,3,Empty,Empty,6,Empty]
mainboard[8]=[Empty,Empty,Empty,Empty,Empty,Empty,4,Empty,8]

print "ORIGINAL"
print_board(mainboard)


make_optboard(optboard,9,9)
#print_board(optboard)
#optboard has a list of all integer options

'''FUNCTIONS FOR SOLVING'''
#updates optboard with respect to main board
def step1(mainboard,optboard):		
	for i in range(9):
		for j in range(9):
			if mainboard[i][j]!=Empty:
				optboard[i][j]=[mainboard[i][j]]
#now iterate over mainboard[i][j] and remove optboard[i][j](z) if z appears in same row/column
def step2(mainboard,optboard):
	for i in range(9):
		for j in range(9):
			if mainboard[i][j]==Empty:
				#using tmp to collect all values that are to be excluded as possible values for mainboard[i][j]
				tmp=[]
				for k in range (9):	
					if mainboard[i][k]!=Empty:
						tmp.append(mainboard[i][k])
					if mainboard[k][j]!=Empty:
					    tmp.append(mainboard[k][j])
					    #need to make sure it only appends it if the value is not yet in the list.
				#print tmp
				for value in tmp:
					try:
						optboard[i][j].remove(value)
					except ValueError:
						continue
#next check for each 3*3 grid and remove VALUE from opt list if it already is in grid
def step3(mainboard,optboard):	
	for i in range(3):
		for j in range(3):
			tmp=[]
			#each subgrid of 3*3
			for k in range(3):
				for l in range(3):
					if mainboard[3*i+k][3*j+l]!=Empty:
						tmp.append(mainboard[3*i+k][3*j+l])	
			for k in range(3):
				for l in range(3):
					if mainboard[3*i+k][3*j+l]==Empty:
						for value in tmp:
							try:
								optboard[3*i+k][3*j+l].remove(value)
							except ValueError:
								continue
#check if a value is is the only option in col/row. If so write to mainboard
def step4(mainboard,optboard):	
	for i in range(9):
		for j in range(9):
			
			for m in range(1,10):
				tmp=[]
				tmp2=[]
				#k  iterating over all lists of options in the COLUMN
				for k in range(0,9):
					#iterates over row&col
					#if m in optboard[i][k]:
					for l in range(len(optboard[i][k])):
						if m == optboard[i][k][l]:	
							tmp.append(m)
							tmp2.append(k)
				if len(tmp)==1:
					optboard[i][tmp2[0]]=[m]


				tmp=[]
				tmp2=[]
				#k  iterating over all lists of options in the ROW
				for k in range(0,9):
					#iterates over row&col
					#if m in optboard[i][k]:
					for l in range(len(optboard[k][j])):
						if m == optboard[k][j][l]:	
							tmp.append(m)
							tmp2.append(k)
				if len(tmp)==1:
					optboard[tmp2[0]][j]=[m]
# check if its only one in 3*3 grid. If so write to mainboard
def step5(mainboard,optboard):	
	for i in range(3):
		for j in range(3):

			for m in range(1,10):
				tmp=[]
				tmp2=[]
				tmp3=[]
				#iterating over all lists of options in subsquare
				for x in range(0,3):
					for y in range(0,3):
						#iterates over row&col
						#if m in optboard[i][x]:
						for l in range(len(optboard[3*i+x][3*j+y])):
							if m == optboard[3*i+x][3*j+y][l]:	
								tmp.append(m)
								tmp2.append(x)
								tmp3.append(y)
				if len(tmp)==1:
					optboard[3*i+tmp2[0]][3*j+tmp3[0]]=[m]
#now adopting mainboard should there be a single option for the field:
def step6(mainboard,optboard):
	for i in range(9):
		for j in range(9):
			if mainboard[i][j]==Empty and len(optboard[i][j])==1:
				mainboard[i][j]=optboard[i][j][0]

z = True
while z == True:

	while True:
	r=randint(0,8)

		mainboard[r][c]

	for step in range 5:
		step1(mainboard,optboard)	
		step2(mainboard,optboard)
		step3(mainboard,optboard)	
		step4(mainboard,optboard)
		step5(mainboard,optboard)	
		step6(mainboard,optboard)

	print_board(optboard)
	print_board(mainboard)

	z = False
	for i in range(9):
		for j in range(9):
			if mainboard[i][j] == Empty:
				z = True

