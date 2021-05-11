import mysql.connector
import os
import time

from player import Player
from player import monsterB
from item import item
from time import sleep
from mysql.connector.constants import ClientFlag

# pip install mysql-connector-python
p = Player(0, 0, 10, 10, item("Bread", False, "🍞", 3))
grid = [
  ["👤", "🏪", "🌳", "@", "@"],
  ["@", "@", "@", "@", "👹"],
  ["🌳", "🌳", "🚪", "@", "@"],
]

prevGrid = [

  ["@", "🏪", "🌳", "@", "@"],
  ["@", "@", "@", "@", "👹"],
  ["🌳", "🌳", "🚪", "@", "@"],
]


def renderLevel(dir, grid):
  os.system('clear')
  for val in grid:
    for x in val:
      print(x,end = "     ")
    print()

def renderInventory(dir):
  os.system('clear')
  if(dir == 'i'):
    n = 0
    for i in p.inventory:
      if n == 0:
        print("Weapons")
      else:
        print("Medicine")
      print("---------")
      for j in i:
        print(j.name + " ",end=repr(j))
        print()
      print()
      n += 1
    loop = True
    while loop:
      cmd = input("Press e to exit or type name of item to use: ")
      if cmd == 'e':
        break
      else:
        isValidItem = False
        item = 0
        for i in p.inventory:
          for j in i:
            if j.name == cmd:
              isValidItem = True
              item = j
              break
        if isValidItem:
          p.currItem = item
          loop = False
        else:
          print("Invalid Item")





config = {
    'user': 'root',
    'password': 'Thekey2275!',
    'host': '35.223.103.123',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}




config['database'] = 'testdb' 
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()

cnxn.commit() 


# first we setup our query
# query = ("INSERT INTO space_missions (company_name) VALUES (5)")
# cursor.execute(query)
# cnxn.commit()  

# cursor.execute("SELECT * FROM space_missions")
# my_result = cursor.fetchone()
# while my_result is not None:
#     print(my_result)
#     my_result = cursor.fetchone()

print("Venture through the forest and defeat the monster in the forest and exit through the door to complete the quest!")
time.sleep(1)
print()
print("Tip: Visit the shop to purchace the goods needed to beat the monster.")
time.sleep(2.5)

os.system('clear')

gameLoop = True
monsterIsBeat = False
fst = False
prevX = 0
prevY = 0
renderLevel("n", grid)
while gameLoop == True:
  prevX = p.x
  prevY = p.y
  print("Press 'i' to open inventory")
  dir = input("Enter the dir you want to go in (w, a, s, d): ")

  grid[p.y][p.x] = prevGrid[p.y][p.x] 
  p.move(dir, grid)

  if(p.questComplete() == True and fst == False):
    p.x -= 1
    grid[1][4] = "💀"
    prevGrid[1][4] = "💀"
    fst = True

  grid[p.y][p.x] = "👤"
  renderInventory(dir)
  renderLevel(dir, grid)



  print(p.x, end=" ")
  print(p.y)
  print("Current Item",end=" ")
  print(repr(p.currItem))
  print("Funds", end=" ")
  print("$" + str(p.money))

  print()

  if  prevGrid[p.y][p.x] == '🚪' and monsterB == False:
    os.system('clear')
    print("Beat the monster first! What kind of hero are you?!")
    time.sleep(2)
    grid[p.y][p.x] = prevGrid[p.y][p.x]
    p.x = prevX
    p.y = prevY
    grid[p.y][p.x] = "👤"
    renderLevel(dir, grid)
