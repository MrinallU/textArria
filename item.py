class item:
  def __init__(self, name, doesDamage, appearence, val):
    self.name = name
    self.doesDamage = doesDamage
    self.appearence = appearence
    self.val = val
  def __repr__(self):
    return self.appearence
  def getStat(self):
    if self.doesDamage == True:
      return self.val * -1
    else:
      return self.val
  
