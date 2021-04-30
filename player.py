import sys

def inBounds(x, y, colNums, rowNums, grid):
  if(x == colNums or rowNums == y or x < 0 or y < 0):
    return False
  else:
    if grid[y][x] != '#':
      return True
  return False

class Player:
  def __init__(self, x, y, hp):
    self.x = x
    self.y = y
    self.hp = hp



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

    
  sys.path.append(".")
    

 