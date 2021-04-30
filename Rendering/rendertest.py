from time import sleep
import os

grid = [
  ["#", "#", "#"],
  ["0", "@", "@"],
  ["@", "@", "@"],
]
def countdown(n):
    while 0 <= n:
        # add some spaces after the number to make sure we overwrite the entire last output
        for val in grid:
          for x in val:
            print(x,end = " ")
          print()
        grid[max(n, 0)][max(n, 0)] = '@'
        n -= 1
        sleep(0.3)
        os.system('clear')

countdown(2)
for val in grid:
  for x in val:
    print(x,end = " ")
  print()