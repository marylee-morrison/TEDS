class TeaCup:
  def __init__(self, capacity):
    # Python executes when a new cup of tea is created.
    self.capacity = capacity # Total ounces the cup holds.
    self.amount = 0 # Current ounces in the cup. All cups start empty!

  def fill(self):
      while self.amount < self.capacity:
          self.amount += 1

  def empty(self):
    self.amount = 0

  def drink(self, amount_drank):
    self.amount -= amount_drank
    # If it's empty, it stays empty!
    if (self.amount == 0):
      self.amount = 0

steves_cup = TeaCup(12)  # Maybe a fancy tea latte.
yis_cup = TeaCup(16)    # It's a rough morning!
brandis_cup = TeaCup(2)  # Just a quick sip.