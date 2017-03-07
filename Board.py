from random import randint, choice
empty = " "
barrier = "#"
board = {}
board_size = 100
for y in range(1, board_size + 1):
  board[y] = {}
  for x in range(1, board_size + 1):
    board[y][x] = empty

def make_passageway(board):
  for y in range(1, len(board) + 1):
    for x in range(1, len(board) + 1):
      board[x][y] = barrier
  x, y = randint(1, len(board)), randint(1, len(board))
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  for _ in range(board_size * (board_size // 4) * 3):
    dr = choice(directions)
    x += dr[0]
    y += dr[1]
    x = min(max(x, 1), len(board) - 1)
    y = min(max(y, 1), len(board) - 1)
    board[x][y] = empty

make_passageway(board)

all_enemies = [{
    "health": 5,
    "char": "I",
    "damage": 5,
    "min-lvl": 0,
    "exp": 5
  }, 
  {
    "health": 8,
    "char": "G",
    "damage": 8,
    "min-lvl": 0,
    "exp": 10
  },
  {
    "health": 13,
    "char": "D",
    "damage": 13,
    "min-lvl": 2,
    "exp": 15
  },
  {
    "health": 15,
    "char": "P",
    "damage": 15,
    "min-lvl": 4,
    "exp": 17
  },
  {
    "health": 18,
    "char": "N",
    "damage": 18,
    "min-lvl": 8,
    "exp": 20
  },
]
