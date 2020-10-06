import random
class Envelope:
  def __init__(self, money=random.randint(0, 1000), used=False):
    self.money = money
    self.used = used
