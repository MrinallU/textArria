import sys
import os
import time
import random
from tabulate import tabulate
from item import item

l = [["Dagger", 10, "Common"], ["Master Sword", 100, "Mythical"], ["Poison Potion", 25, "Rare"]]
monsterB = False

itemLib = [
  item("Dagger", True, "🗡️", 10),
  item("Bread", False, "🍞", 3),
  item("Master Sword", False, "⚔️", 10),
  item("Poison Potion", True, "⚗️", 10 ),
  item("Stick", True, "🌿", 1 )
]

def inBounds(x, y, rowNums, colNums, grid):
  if(x == colNums or rowNums == y or x < 0 or y < 0):   
    return False
  else:
    if grid[y][x] != '🌳':
      return True
  
  return False

def getItemData(itemName):
  for i in itemLib:
    if itemName == i.name:
      return i

class Player:
  def __init__(self, x, y, hp, money, currItem):
    self.maxhp = 10
    self.x = x
    self.y = y
    self.hp = hp
    self.money = money
    self.inventory = [
      [item("Stick", True, "🌿", 1 )], 
      [item("Bread", False, "🍞", 3)]
    ]
    self.currItem = currItem
  
  def remItem(self):
    index = 0
    curr = 0
    for i in self.inventory[1]:
      if(i.name == self.currItem.name):
        index = curr
      curr += 1
    self.inventory[1].pop(index)
    self.currItem = self.inventory[0][0]

  def questComplete(self):
    return monsterB
  def move(self, dir, grid):
    prevX = self.x
    prevY = self.y

    if dir == 'a':
      self.x = self.x - 1
    elif dir == 'w':
      self.y = self.y - 1
    elif dir == 's':
      self.y = self.y + 1
    elif dir == 'd':
      self.x += 1
    
    if(inBounds(self.x, self.y, len(grid), len(grid[0]), grid) == False):
      self.x = prevX
      self.y = prevY
    else:
      if(grid[self.y][self.x] == "🏪"):
        renderShop(self)
        self.x = prevX
        self.y = prevY
      elif(grid[self.y][self.x] == "👹"):
        renderBattle(self)
      elif(monsterB == True and grid[self.y][self.x] == "🚪"):
        os.system('clear')
        print("You saved the forest from the monster!")
        quit()
  
  def renderInventory(self, dir):
    os.system('clear')
    n = 0
    for i in self.inventory:
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
        for i in self.inventory:
          for j in i:
            if j.name == cmd:
              isValidItem = True
              item = j
              break
        if isValidItem:
          self.currItem = item
          loop = False
        else:
          print("Invalid Item")
  

    
  sys.path.append(".")

def renderShop(p):
  shopLoop = True
  n = 0

  def startText(num):
    if num == 0:
      return "Welcome to my shop! Take a look of some of my finest goods."
    else:
      return "Take your Time!"
  
  os.system('clear')
  while shopLoop:
    os.system('clear')
    print()
    print(startText(n))

    table = tabulate(l, headers=['Item', 'Price', 'Rarity'], tablefmt='orgtbl')

    print()
    print(table)
    print()
    print("Your Funds $" + str(p.money))

    toBuy = input("What item would you like to buy (e to exit): ")

    os.system('clear')

    if toBuy == "e":
      break

    found = False
    for i in l:
      if toBuy == i[0]:
        if(p.money >= i[1]):
          print("Item Purchaced!")
          found = True
          p.money -= i[1]
          val = 0 if getItemData(toBuy).doesDamage else 1
          p.inventory[val].append(getItemData(toBuy))
        else:
          found = True
          print("Insufficient Funds")

    if found == False:
      print("Sorry, but I don't seem to have that item...")
    time.sleep(0.7)

    n += 1

def renderBattle(p):

  os.system('clear')
  print("You have encountered a monster!")
  time.sleep(0.5)
  battleLoop = True
  n = 0

  monsterHealth = 15
  monsterDamage = 4

  while(battleLoop == True):
    os.system('clear')
    if(n % 2 == 0):
      print("Player turn")
      print("------------")
      print("👤" + " " + " Hp:", end=" ")
      print(p.hp)
      print("👹" + " " + " Hp:", end=" ")
      print(monsterHealth)
      print("Current Item:", end=" ")
      print(repr(p.currItem))
      command = input("Use current item (u) or Go into inventory to switch use item (s): ")

      if(len(p.inventory) == 0):
        os.system('clear')
        print("No more items to use! Defenseless, the monster eats you! Please renter the game to pick up from your last save.")
        time.sleep(1.2)
        quit()
        

      if(command == "s"):
        p.renderInventory('i')
        
      os.system('clear')

      if(p.currItem.doesDamage):
        print("You did " + str(abs(p.currItem.getStat())) + " damage!")
        monsterHealth += p.currItem.getStat(); 
      else:
        prevhp = p.hp
        if(p.hp + p.currItem.getStat() > p.maxhp ):
          p.hp = min(p.maxhp, p.hp + p.currItem.getStat()); 
        else:
           p.hp = p.hp + p.currItem.getStat(); 
        p.remItem()

        print("You recovered " + str(p.hp - prevhp) + " hp!")
       

      # get rid of the item if it heals
    else:
      print("Enemy Turn")
      print("------------")
      print("Enemy did " + str(abs(monsterDamage)) + " damage!")
      p.hp -= monsterDamage
      if(p.hp <= 0):
        os.system('clear')
        print("You ran out of health and died.")
        time.sleep(0.8)
  

    if(monsterHealth <= 0):
      os.system('clear')
      print("Congrats you beat the monster now you can cross the door and finish the game!")
      print()
      time.sleep(0.75)
      print("Gained $100 as reward!")
      p.money += 100
      global monsterB 
      monsterB = True
      battleLoop = False
      time.sleep(2)
    elif(p.hp <= 0):
      os.system('clear')
      print('Oh no you lost! Re-enter the game to pick up form your last save.')
      quit()

    n += 1
  
  


 