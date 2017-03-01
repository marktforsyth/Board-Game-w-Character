from random import randint
empty = " "
board = {}
for y in range(1, 21):
  board[y] = {}
  for x in range(1, 21):
    board[y][x] = empty

def make_vwall():
  x = randint(1, len(board))
  numgaps = randint(1, 5)
  gaps = [randint(1, len(board)) for i in range(numgaps)]
  for y in range(1, len(board) + 1):
    if y in gaps:
      board[x][y] = empty
    else:
      board[x][y] = "*"

make_vwall()
make_vwall()

all_enemies = [{
    "health": 5,
    "char": "I",
    "damage": 10,
    "min-lvl": 0
  }, 
  {
    "health": 8,
    "char": "G",
    "damage": 16,
    "min-lvl": 0
  },
  {
    "health": 13,
    "char": "D",
    "damage": 26,
    "min-lvl": 2
  },
  {
    "health": 15,
    "char": "P",
    "damage": 30,
    "min-lvl": 4
  },
  {
    "health": 18,
    "char": "N",
    "damage": 36,
    "min-lvl": 8
  },
]

def find_empty_space():
  while True:
    x = randint(1, len(board))
    y = randint(1, len(board))
    
    if board[x][y] == empty:
      return x, y
