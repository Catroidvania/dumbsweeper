# main.py
# created fri may 31 2024
# by catroidvania


from random import randrange


def generate_board(width: int, height: int, mine_percent: float) -> [[str]]:
	board = [[0 for w in range(width)] for h in range(height)]
	mine_count = int(width * height * (mine_percent / 100))

	while mine_count:
		x = randrange(0, width)
		y = randrange(0, height)
		if board[y][x] == 0:
			board[y][x] = '@'
			mine_count -= 1

	# ah indentation based syntax
	for r in range(height):
		for c in range(width):
			if board[r][c] == '@':
				continue
			for ox in [-1, 0, 1]:
				for oy in [-1, 0, 1]:
					x_in_range = c + ox > -1 and c + ox < width
					y_in_range = r + oy > -1 and r + oy < height
					x_y_not_0 = ox or oy
					if x_in_range and y_in_range and x_y_not_0 and board[r + oy][c + ox] == '@':
						board[r][c] += 1

	for r in range(height):
		for c in range(width):
			if not board[r][c]:
				board[r][c] = '.'
			elif board[r][c] != '@':
				board[r][c] = str(board[r][c])
	
	return board


if __name__ == "__main__":
	while True:
		try:
			width = int(input("board width: "))
			if width < 1:
				raise ValueError # lmao
			break
		except ValueError:
			print("width must be number above 0!")

	while True:
		try:
			height = int(input("board height: "))
			if height < 1:
				raise ValueError # lmao again
			break
		except ValueError:
			print("height must be number above 0!")

	while True:
		try:
			percent = float(input("percetage of board that will be mines: "))
			if 0 <= percent <= 100:
				break
			raise ValueError # lmao x3
		except ValueError:
			print("must be number between 0 and 100!")

	board = generate_board(width, height, percent)

	print(f"`@ are mines, . is a blank square, {int(width * height * (percent / 100))} mines on this board`")
	for r in board:
		for c in r:
			print(f"||`{c}`|| ", end='')
		print()
