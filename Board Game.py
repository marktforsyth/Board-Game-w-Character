from random import randint, choice
from Board import board, empty, make_vwall, all_enemies

def find_empty_space():
  while True:
    x = randint(1, len(board))
    y = randint(1, len(board))
    
    if board[x][y] == empty:
      return x, y

def gen_board_data():
  for i in range(0, 5):
    x, y = find_empty_space()
    board[x][y] = "*"
  
  ladderX, ladderY = find_empty_space()
  board[ladderX][ladderY] = "L"
  
  global enemies
  enemies = []
  
  for i in range(1, 4):
    enemies.append(get_random_enemy(how_far_down, all_enemies))
    
  for enemy in enemies:
    x, y = find_empty_space()
    enemy["x"] = x
    enemy["y"] = y
    
    board[enemy["x"]][enemy["y"]] = enemy["char"]
  
  for i in range(0, 2):
    tresX, tresY = find_empty_space()
    whichTres = randint(0, 2)
    board[tresX][tresY] = treasures[whichTres]
    
global enemy_health_var
enemy_health_var = 5

global gold_var, heal_var
gold_var = 50 # double every time
heal_var = 15 # add 5 to the health potions every time=

theFirstX, theFirstY = find_empty_space()

player = {
  "x": theFirstX,
  "y": theFirstY,
  "coins": 0,
  "health": 100,
  "weapon": {
    "damage": 1,
    "name": "cheap sword",
    "type": "slash"
  },
  "exp": 0,
  "level": 0
}

board[player["x"]][player["y"]] = "C"

treasures = ["g", "h", "w"]

global how_far_down
how_far_down = 0

global has_health_potion
has_health_potion = False

def get_random_enemy(level, enemies):
  '''
  Returns valid enemy for given level
  '''
  available_enemies = []
  
  for enemy in enemies:
    if enemy["min-lvl"] >= level:
      available_enemies.append(enemy)
      
  return choice(available_enemies).copy()

weapons = [
  {
    "name": "mace",
    "damage": 6,
    "type": "spin",
    "min-lvl": 2
  },
  {
    "damage": 1,
    "name": "cheap sword",
    "type": "slash",
    "min-lvl": 0
  },
  {
    "name": "better sword",
    "damage": 5,
    "type": "slash",
    "min-lvl": 2
  },
  {
    "name": "better mace",
    "damage": 9,
    "type": "spin",
    "min-lvl": 5
  },
  {
    "name": "awesome sword",
    "damage": 10,
    "type": "slash",
    "min-lvl": 5
  },
  {
    "name": "legendary sword",
    "damage": 20,
    "type": "slash",
    "min-lvl": 10
  },
  {
    "name": "awesome mace",
    "damage": 15,
    "type": "spin",
    "min-lvl": 10
  }
]

gen_board_data()

def get_random_weapon(level):
  whichWeapon = randint(0, len(weapons)-1)
  available_weapons = []
  
  for weapon in weapons:
    if weapon["min-lvl"] >= level:
      correct_weapon = True
    else:
      get_random_weapon(level)
  
  if correct_weapon:
    print("You got a " + weapons[whichWeapon]["name"] + "!")
    player["weapon"] = weapons[whichWeapon]

def make_divider(size):
  divider = []
  for i in range(size):
    divider.append('---')
  return '|'.join(divider)

divider = make_divider(len(board))

def printBoard():
  global how_far_down
  
  for d in range(1, (len(board) + 1)):
    print()
    # print(divider)
    for i in range(1, len(board) + 1):
      if i == len(board):
        print(" " + str(board[i][d]), end="")
      else:
        print(" " + str(board[i][d]) + "", end="")
  print("\n"*2)
  print("Gold: " + str(player["coins"]), end=", ")
  print("Health: " + str(player["health"]), end=", ")
  print("Weapon: " + player["weapon"]["name"], end=", ")
  print("Depth: " + str(how_far_down), end=", ")
  print("XP: " + str(player["exp"]))

def attack():
  for enemy in enemies:
    if enemy["x"] + 1 == player["x"] or enemy["x"] - 1 == player["x"] or enemy["y"] + 1 == player["y"] or enemy["y"] - 1 == player["y"]:
      enemy["health"] -= player["weapon"]["damage"]
      print("The enemy is at " + str(enemy["health"]) + " health.")
      if player["weapon"]["type"] == "slash":
        break

def enemyMove():
  for enemy in enemies:
    cmd = randint(1, 4)
  
    xVal = abs(enemy["x"] - player["x"])
    yVal = abs(enemy["y"] - player["y"])
    
    dx = 0
    dy = 0
    
    if xVal > yVal:
      if player["x"] > enemy["x"]:
        dx = 1
      else:
        dx = -1
    else:
      if player["y"] > enemy["y"]:
        dy = 1
      else:
        dy = -1
    
    if enemy["x"] + dx == player["x"] and enemy["y"] + dy == player["y"]:
      print("Oh no! Then enemy hit you!")
      player["health"] -= enemy["damage"]
    elif board[enemy["x"]+dx][enemy["y"]+dy] == "*":
      print("The enemies head slams into the barrier")
    elif board[enemy["x"]+dx][enemy["y"]+dy] == "g" or board[enemy["x"]+dx][enemy["y"]+dy] == "w" or board[enemy["x"]+dx][enemy["y"]+dy] == "h":
      print("Oh no! The enemy got to the chest before you! Good luck on the next one!")
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 2)
      board[tresX][tresY] = treasures[whichTres]
      
      board[enemy["x"]][enemy["y"]] = empty
      enemy["x"] += dx
      enemy["y"] += dy
      board[enemy["x"]][enemy["y"]] = enemy["char"]
    elif board[enemy["x"]+dx][enemy["y"]+dy] != empty:
      pass # the tile is occupied
    else:
      board[enemy["x"]][enemy["y"]] = empty
      enemy["x"] += dx
      enemy["y"] += dy
      board[enemy["x"]][enemy["y"]] = enemy["char"]
      
def find_enemy_at(x, y):
  for enemy in enemies:
    if x == enemy["x"] and y == enemy["y"]:
      return enemy

def check():
  global has_health_potion, enemy_health_var, how_far_down
  global gold_var, heal_var 
  
  cmd = input(">>> ")
  
  dx = 0
  dy = 0
  should_regen_health = True
    
  if cmd == "u":
    if player["y"] <= 1:
      print("\nYou cannot go up past here!")
    else:
      dy = -1
  elif cmd == "d":
    if player["y"] >= len(board):
      print("\nYou cannot go down past here!")
    else:
      dy = 1
  elif cmd == "r":
    if player["x"] >= len(board):
      print("\nYou cannot go right past here!")
    else:
      dx = 1
  elif cmd == "l":
    if player["x"] <= 1:
      print("\nYou cannot go left past here!")
    else:
      dx = -1
  elif cmd == "a":
    attack()
    should_regen_health = False
  elif cmd == "hp":
    if has_health_potion == True:
      player["health"] += heal_var
      print("Your health has been raised by " + str(heal_var) + "!")
      has_health_potion = False
    else:
      print("\nYou don't have a health potion!")
    should_regen_health = False
  else:
    print("\nWe do not recognize your command")
    should_regen_health = False
  
  if should_regen_health:
    rand_healing = randint(1, 5)
    player["health"] += rand_healing
  
 
  enemy = find_enemy_at(player["x"] + dx, player["y"] + dy)
  if enemy:
    print("Oh no! The enemy hit you!")
    
    board[player["x"]][player["y"]] = empty
    player["x"] += dx*2
    player["y"] += dy*2
    board[player["x"]][player["y"]] = "C"
  
    if player["x"] + dx*2 <= 0 or player["y"] + dy*2 <= 0 or player["x"] + dx*2 >= len(board) or player["y"] + dy*2 >= len(board):
      board[player["x"]][player["y"]] = empty
      enemy["x"] = player["x"]
      enemy["y"] = player["y"]
      player["x"] += dx
      player["y"] += dy
      board[player["x"]][player["y"]] = "C"
      
      board[enemy["x"]][enemy["y"]] = enemy["char"]
  if board[player["x"]+dx][player["y"]+dy] == "*":
    print("Your head slams into the barrier")
  if board[player["x"]+dx][player["y"]+dy] == "L":
    board[player["x"]][player["y"]] = empty
    player["x"] += dx
    player["y"] += dy
    board[player["x"]][player["y"]] = "C"
    
    print("\nGoing downstairs...\n")
    how_far_down += 1
    
    enemy_health_var += 2
    gold_var *= 2
    heal_var += 5
    
    for y in range(1, 21):
      board[y] = {}
      for x in range(1, 21):
        board[y][x] = empty
    
    make_vwall()
    make_vwall()
    
    board[player["x"]][player["y"]] = "C"
    
    for enemy in enemies:
      board[enemy["x"]][enemy["y"]] = empty
    
    gen_board_data()
    
  else:
    if board[player["x"]+dx][player["y"]+dy] == "g":
      print("You got " + str(gold_var) + " gold!")
      player["coins"] += gold_var
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 2)
      board[tresX][tresY] = treasures[whichTres]
    elif board[player["x"]+dx][player["y"]+dy] == "w":
      get_random_weapon(how_far_down)
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 2)
      board[tresX][tresY] = treasures[whichTres]
    elif board[player["x"]+dx][player["y"]+dy] == "h":
      print("You got a health potion!")
      has_health_potion = True
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 2)
      board[tresX][tresY] = treasures[whichTres]

    board[player["x"]][player["y"]] = empty
    player["x"] += dx
    player["y"] += dy
    board[player["x"]][player["y"]] = "C" # '''

print("Your commands are 'u', 'd', 'l', 'r', 'a' and 'hp'\n")

def remove_enemy(enemy):
  '''
  Deletes an enemy from the enemy list and creates a new one in it's place
  '''
  
  enemyGold = randint(1, 10)
  print("You killed the enemy! You loot it and find " + str(enemyGold) + " gold.")
  player["coins"] += enemyGold
  
  new_enemy = get_random_enemy(how_far_down, enemies)
  
  board[enemy["x"]][enemy["y"]] = empty
  newEnX, newEnY = find_empty_space()
  
  enemies.remove(enemy)
  enemies.append(new_enemy)
  
  new_enemy["x"] = newEnX
  new_enemy["y"] = newEnY
  board[new_enemy["x"]][new_enemy["y"]] = new_enemy["char"]

while True:
  enemyMove()
  printBoard()
  check()
  
  if player["health"] >= 100:
    player["health"] = 100
  
  dead_enemies = []
  
  for enemy in enemies:
    if enemy["health"] <= 0:
      dead_enemies.append(enemy)
      
      player["exp"] += enemy["exp"]
      if player["exp"] >= 50:
        player["level"] += 1
        player["exp"] = 0
  
  for enemy in dead_enemies:
    remove_enemy(enemy)
    
  if player["health"] <= 0:
    print("You died. :(")
    break
