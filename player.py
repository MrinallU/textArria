import sys
class Player:
  def __init__(self, x, y, hp):
    self.x = x
    self.y = y
    self.hp = hp
  def move(self, dir):
    if dir == 'w':
      self.x = self.x - 1
    elif dir == 'n':
      self.y = self.y + 1
  sys.path.append(".")
    

 