import random
class Envelope:
  """
    Class to represent an envelope using the fields money (which represents the amount of money in the envelope)
    and used (boolean which represents whether the envelope was used or not)
  """
  def __init__(self, money=0, used=False):
    self.money = random.randint(0, 1000)
    self.used = used
