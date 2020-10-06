import random


class BaseStrategy:
    def __init__(self, envs):
        self.envelopes = envs

    def play(self):
        self.perform_strategy()

    def perform_strategy(self):
        pass


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envs):
        super(self, envs)

    def perform_startegy(self, counter):
        rnd = random.randint(0, 99)
        return self.envelopes[rnd]


class N_max_srategy(BaseStrategy):
    def __init__(self, envs, n):
        super(self, envs)
        self.n = n

    def perform_startegy(self, counter):
        count = 1
        max = 0
        i = 0
        while count < self.n:
            if self.envelopes[i] > max:
                max = self.envelopes[i]
                count += 1
            i += 1
        return self.envelopes[i]








class More_then_N_percent_group_srategy(BaseStrategy):
    def __init__(self, envs, p):
        super(self, envs)
        self.percent = p

    def perform_startegy(self, counter):
        pass
