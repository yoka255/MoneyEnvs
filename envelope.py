import random
class Envelope:
  def __init__(self, money=0, used=False):
    self.money = random.randint(0, 1000)
    self.used = used
