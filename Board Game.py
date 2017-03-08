from random import randint, choice, random
from Board import board, empty, barrier, all_enemies, make_passageway

def find_empty_space():
  while True:
    x = randint(1, len(board))
    y = randint(1, len(board))
    
    if board[x][y] == empty:
      return x, y

def gen_board_data():
  
  ladderX, ladderY = find_empty_space()
  board[ladderX][ladderY] = "L"
  
  global enemies
  enemies = []
  
  for i in range(1, 13):
    enemies.append(get_random_enemy(how_far_down, all_enemies))
    
  for enemy in enemies:
    x, y = find_empty_space()
    enemy["x"] = x
    enemy["y"] = y
    
    board[enemy["x"]][enemy["y"]] = enemy["char"]
  
  for i in range(0, 8):
    tresX, tresY = find_empty_space()
    whichTres = randint(0, 4)
    board[tresX][tresY] = treasures[whichTres]

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
    "name": "toy sword",
    "type": "slash"
  },
  "sheild": {
    "name": "cheap sheild",
    "defense": 1,
    "min-lvl": 0
  },
  "items": [],
  "exp": 0,
  "level": 0,
  "attack": 0,
  "hunger": 0
}

board[player["x"]][player["y"]] = "C"

treasures = ["s", "w", "g", "h", "b"]

global how_far_down
how_far_down = 0

def get_random_enemy(level, enemies):
  '''
  Returns valid enemy for given level
  '''
  available_enemies = []
  
  for enemy in enemies:
    if enemy["min-lvl"] <= level:
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
    "damage": 2,
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

sheilds = [
  {
    "name": "cheap sheild",
    "defense": 1,
    "min-lvl": 0
  },
  {
    "name": "decent sheild",
    "defense": 3,
    "min-lvl": 0
  },
  {
    "name": "better sheild",
    "defense": 5,
    "min-lvl": 2
  },
  {
    "name": "awesome sheild",
    "defense": 10,
    "min-lvl": 5
  },
  {
    "name": "awesome sheild",
    "defense": 20,
    "min-lvl": 10
  }
]

gen_board_data()

def get_random_weapon(level):
  '''
  Returns a weapon for the current level
  '''
  whichWeapon = randint(0, len(weapons)-1)
  available_weapons = []
  
  for weapon in weapons:
    if weapon["min-lvl"] <= level:
      available_weapons.append(weapon)
      
  return choice(available_weapons).copy()

def get_random_sheild(level):
  '''
  Returns a sheild for the current level
  '''
  
  whichSheild = randint(0, len(weapons)-1)
  available_sheilds = []
  
  for sheild in sheilds:
    if sheild["min-lvl"] <= level:
      available_sheilds.append(sheild)
  
  return choice(available_sheilds).copy()

def make_divider(size):
  divider = []
  for i in range(size):
    divider.append('---')
  return '|'.join(divider)

divider = make_divider(len(board))

def printBoard():
  global how_far_down
  
  visible_margin = 10
  for y in range(player['y'] - visible_margin, player['y'] + visible_margin + 1):
    print()
    for x in range(player['x'] - visible_margin, player['x'] + visible_margin + 1):
      if x < 1 or y < 1 or x > len(board) or y > len(board):
        print(" " + barrier, end='')
      else:
        print(" " + str(board[x][y]), end="")
  '''
  for y in range(1, (len(board) + 1)):
    print()
    for x in range(1, len(board) + 1):
      print(" " + str(board[x][y]), end="")'''
      
  print("\n"*2)
  print("Gold: " + str(player["coins"]), end=", ")
  print("Health: " + str(player["health"]), end=", ")
  print("Weapon: " + player["weapon"]["name"], end=", ")
  print("Items:", end=" ")
  
  if not player["items"]:
    print("none", end=", ")
  else:
    for item in player["items"]:
      print(item, end=", ")
      
  print("Depth: " + str(how_far_down), end=", ")
  print("XP: " + str(player["exp"]), end=", ")
  print("Level: " + str(player["level"]), end=", ")
  print("Hunger: " + str(player["hunger"]))

def attack():
  for enemy in enemies:
    if is_next_to(enemy, player):
      enemy["health"] -= player["weapon"]["damage"]
      enemy["health"] -= player["attack"]
      print("The enemy is at " + str(enemy["health"]) + " health.")
      if player["weapon"]["type"] != "spin":
        break

def enemyMove():
  visible_margin = 10
  
  for enemy in enemies:
    # If enemy in sight range
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
      enemy_hit_you(enemy) 
    elif board[enemy["x"]+dx][enemy["y"]+dy] == barrier:
      print("The enemy's head slams into the barrier")
    elif board[enemy["x"]+dx][enemy["y"]+dy] == "g" or board[enemy["x"]+dx][enemy["y"]+dy] == "w" or board[enemy["x"]+dx][enemy["y"]+dy] == "h" or board[enemy["x"]+dx][enemy["y"]+dy] == "s" or board[enemy["x"]+dx][enemy["y"]+dy] == "b":
      print("Oh no! The enemy got to the chest before you! Good luck on the next one!")
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 4)
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
      
      if is_next_to(enemy, player):
        enemy_hit_you(enemy)

def is_next_to(thing1, thing2):
  dx = abs(thing1['x'] - thing2['x'])
  dy = abs(thing1['y'] - thing2['y'])
  return (dx == 0 and dy == 1) or (dx == 1 and dy == 0)

def enemy_hit_you(enemy):
  print("Oh no! Then enemy hit you!")
  damage = max(0, enemy["damage"] - player["sheild"]["defense"])
  player["health"] -= damage

def find_enemy_at(x, y):
  for enemy in enemies:
    if x == enemy["x"] and y == enemy["y"]:
      return enemy

def check():
  global how_far_down
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
    if "health potion" in player["items"]:
      player["health"] += heal_var
      print("Your health has been raised by " + str(heal_var) + "!")
      player["items"].remove("health potion")
    else:
      print("\nYou don't have a health potion!")
    should_regen_health = False
  else:
    print("\nWe do not recognize your command")
    should_regen_health = False
    
  if player["hunger"] >= 50:
    should_regen_health = False
    
    if player["hunger"] >= 85:
      player["health"] -= 5
      
      if player["hunger"] >= 100:
        player["hunger"] = 100
      elif player["hunger"] <= 0:
        player["hunger"] = 0
  
  if should_regen_health:
    if player["level"] == 0:
      rand_healing = randint(0, 3)
    else:
      rand_healing = randint(0, player["level"]*3)
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
  if board[player["x"]+dx][player["y"]+dy] == barrier:
    print("Your head slams into the barrier")
    player["health"] -= 5
    return
  if board[player["x"]+dx][player["y"]+dy] == "L":
    board[player["x"]][player["y"]] = empty
    player["x"] += dx
    player["y"] += dy
    board[player["x"]][player["y"]] = "C"
    
    print("\nGoing downstairs...\n")
    how_far_down += 1
    
    gold_var *= 2
    heal_var += 5
    
    make_passageway(board)
    
    board[player["x"]][player["y"]] = "C"
    
    for enemy in enemies:
      board[enemy["x"]][enemy["y"]] = empty
    
    gen_board_data()
    
  else:
    if board[player["x"]+dx][player["y"]+dy] == "g":
      print("You got " + str(gold_var) + " gold!")
      player["coins"] += gold_var
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 4)
      board[tresX][tresY] = treasures[whichTres]
    elif board[player["x"]+dx][player["y"]+dy] == "w":
      weapon = get_random_weapon(how_far_down)
      
      print("You got a " + weapon["name"] + "!")
      player["weapon"] = weapon
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 4)
      board[tresX][tresY] = treasures[whichTres]
    elif board[player["x"]+dx][player["y"]+dy] == "h":
      print("You got a health potion!")
      player["items"].append("health potion")
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 4)
      board[tresX][tresY] = treasures[whichTres]
    elif board[player["x"]+dx][player["y"]+dy] == "s":
      sheild = get_random_sheild(how_far_down)
      
      print("You got a " + sheild["name"] + "!")
      player["sheild"] = sheild
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 4)
      board[tresX][tresY] = treasures[whichTres]
    elif board[player["x"]+dx][player["y"]+dy] == "b":
      player["hunger"] -= 30
      
      tresX, tresY = find_empty_space()
      whichTres = randint(0, 4)
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
  
  choice = random()
  
  if choice <= 0.3:
    whichOne = randint(0, 3)
    
    if whichOne == 0:
      weapon = get_random_weapon(how_far_down)
      print("You killed the enemy! You loot it and find a " + weapon["name"] + "!")
      player["weapon"] = weapon
    elif whichOne == 1:
      sheild = get_random_sheild(how_far_down)
      print("You killed the enemy! You loot it and find a " + sheild["name"] + "!")
      player["weapon"] = weapon
    elif whichOne == 2:
      enemyGold = randint(1, 10)
      print("You killed the enemy! You loot it and find " + str(enemyGold) + " gold.")
      player["coins"] += enemyGold
    else:
      print("Something's gone wrong")
  
  new_enemy = get_random_enemy(how_far_down, enemies)
  
  board[enemy["x"]][enemy["y"]] = empty
  newEnX, newEnY = find_empty_space()
  
  enemies.remove(enemy)
  enemies.append(new_enemy)
  
  new_enemy["x"] = newEnX
  new_enemy["y"] = newEnY
  board[new_enemy["x"]][new_enemy["y"]] = new_enemy["char"]

while True:
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
        player["attack"] += 3
  
  for enemy in dead_enemies:
    remove_enemy(enemy)
    
  if player["health"] <= 0:
    print("You died. :(")
    break
  
  player["hunger"] += 0.5
  
  enemyMove()
  printBoard()
  check()
