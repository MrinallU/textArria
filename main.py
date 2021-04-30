import mysql.connector
import os

from player import Player
from time import sleep
from mysql.connector.constants import ClientFlag

# pip install mysql-connector-python
p = Player(0, 0, 100)
prevGrid = [
  ["@", "#", "#"],
  ["0", "@", "@"],
  ["@", "@", "@"],
]
grid = [
  ["P", "#", "#"],
  ["0", "@", "@"],
  ["@", "@", "@"],
]

def renderLevel(dir, grid):
  os.system('clear')

  for val in grid:
    for x in val:
      print(x,end = " ")
    print()

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



gameLoop = True
renderLevel("n", grid)
while gameLoop == True:
  dir = input("Enter the dir you want to go in (w, a, s, d): ")
  grid[p.y][p.x] = prevGrid[p.y][p.x]
  p.move(dir, grid)
  grid[p.y][p.x] = "P"
  renderLevel(dir, grid)
  print(p.x, end=" ")
  print(p.y)
