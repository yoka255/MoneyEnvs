from abc import ABC
class BaseStrategy(ABC):

	def __init__(self, envs):
		self.envelopes = envs

	def play(self):
		self.perform_strategy()

	def perform_strategy(self):
		pass


class More_then_N_percent_group_strategy:

	def __init__(self, envs, p):
		super(self, envs)
		self.percent = p

	def perform_strategy(self):
		n = len(envelopes)
		best = 0
			best = max(best, e.money)
		for e in envelopes[(int)n*self.percent:-1]:
			if e.money > best:
				print(f"The envelope that was chosen contains {e.money}$")
				return
		print(f"The envelope that was chosen contains {envelopes[-1].money}$")
