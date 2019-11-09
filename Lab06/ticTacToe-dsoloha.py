# Tic-Tac-Toe
# Dan Soloha
# 10/8/2019

import random

def drawBoard(board):
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('-----------')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('-----------')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def choose_letter():
	letter = ''
	while letter not in ('x', 'o'):
		print('Do you want to be X or O?')
		letter = input().lower()

	if letter == 'x':
		return ['x', 'o']
	else:
		return ['o', 'x']

def goes_first(letter):
	if letter == 'x':
		return 'player'
	else:
		return 'computer'

def play_again():
	print('Do you want to play again? (y/n)')
	return input().lower().startswith('y')

def get_move(board, letter, move):
	board[move] = letter

def is_winner(board, letter):
	return ((board[7] == letter and board[8] == letter and board[9] == letter) or	# across the top
			(board[4] == letter and board[5] == letter and board[6] == letter) or	# across the middle
			(board[1] == letter and board[2] == letter and board[3] == letter) or	# across the bottom
			(board[7] == letter and board[4] == letter and board[1] == letter) or	# down the left side
			(board[8] == letter and board[5] == letter and board[2] == letter) or	# down the middle
			(board[9] == letter and board[6] == letter and board[3] == letter) or	# down the right side
			(board[7] == letter and board[5] == letter and board[3] == letter) or	# diagonal
			(board[9] == letter and board[5] == letter and board[1] == letter))		# diagonal

def board_copy(board):
	dupeBoard = []

	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def is_space_free(board, move):
	return board[move] == ' '

def player_move(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
		print('What is your next move? (1-9)')
		move = input()
	return int(move)

def random_move_from_list(board, moves_list):
	possible_moves = []
	for i in moves_list:
		if is_space_free(board, i):
			possible_moves.append(i)

	if len(possible_moves) != 0:
		return random.choice(possible_moves)
	else:
		return None

def computer_move(board, computer_letter):
	if computer_letter == 'x':
		playerLetter = 'o'
	else:
		playerLetter = 'x'

	# check if computer can win in the next move
	for i in range(1, 10):
		copy = board_copy(board)
		if is_space_free(copy, i):
			get_move(copy, computer_letter, i)
			if is_winner(copy, computer_letter):
				return i

	# check if the player could win on their next move and block them
	for i in range(1, 10):
		copy = board_copy(board)
		if is_space_free(copy, i):
			get_move(copy, playerLetter, i)
			if is_winner(copy, playerLetter):
				return i

	# try to take one of the corners
	move = random_move_from_list(board, [1, 3, 7, 9])
	if move != None:
		return move

	# try to take the center
	if is_space_free(board, 5):
		return 5

	# move on one of the sides
	return random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
	for i in range(1, 10):
		if is_space_free(board, i):
			return False
	return True

print('Welcome to Tic Tac Toe!')

while True:
	orig_board = [' '] * 10
	player_letter, computer_letter = choose_letter()
	turn = goes_first(player_letter)
	print('The ' + turn + ' will go first.')
	playing = True

	while playing:
		if turn == 'player':
			drawBoard(orig_board)
			move = player_move(orig_board)
			get_move(orig_board, player_letter, move)

			if is_winner(orig_board, player_letter):
				drawBoard(orig_board)
				print('Hooray! You have won the game!')
				playing = False
			else:
				if is_board_full(orig_board):
					drawBoard(orig_board)
					print('The game is a tie!')
					break
				else:
					turn = 'computer'
		else:
			move = computer_move(orig_board, computer_letter)
			get_move(orig_board, computer_letter, move)

			if is_winner(orig_board, computer_letter):
				drawBoard(orig_board)
				print('The computer has beaten you! You lose.')
				playing = False
			else:
				if is_board_full(orig_board):
					drawBoard(orig_board)
					print('The game is a tie!')
					break
				else:
					turn = 'player'

	if not play_again():
		break
