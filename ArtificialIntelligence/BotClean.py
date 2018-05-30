# https://www.hackerrank.com/challenges/botclean?hr_b=1
#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
	if board[posr][posc] == 'b':
		isUp = False
		isDown = False
		isRight = False
		isLeft = False
		# check neighboring cells
		# check up
		if posr != 0:
			if board[posr-1][posc] == "d":
				isUp = True
		# check down:
		if posr != len(board) - 1:
			if board[posr+1][posc] == "d":
				isDown = True
		# check left
		if posc != 0:
			if board[posr][posc-1] == "d":
				isRight = True
		# check right
		if posc != len(board[0]) - 1:
			if board[posr][posc+1] == "d":
				isRight = True

	if board[posr][posc] == 'd':
    	print("CLEAN")

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

