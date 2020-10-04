
class BaseStrategy:

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
