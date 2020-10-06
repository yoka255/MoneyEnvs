import random

class BaseStrategy:
    def __init__(self, envs):
        self.envelopes = envs

    def play(self):
        self.perform_strategy()

    def perform_strategy(self):
        for envelope in self.envelopes:
            letter = input("The amount is: " + str(envelope.money) + " Take(T) or Leave(L) - ")
            if letter == 'T':
                print(envelope.money)
                return
            elif letter == 'L':
                pass
            else:
                print("Wrong Input - Envelope Was Skipped")
        print("Returning last envelope")
        print(self.envelopes[-1].money)

    def display(self):
        return "BaseStrategy - user select manually envelopes"


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envs):
        super().__init__(envs)

    def perform_strategy(self):
        rnd = random.randint(0, 99)
        print("The amount is: " + str(self.envelopes[rnd].money))

    def display(self):
        return "Automatic_BaseStrategy - random selection of envelop"


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envs, p=0.25):
        super().__init__(envs)
        self.percent = p

    def perform_strategy(self):
        self.percent = float(self.percent)
        n = len(self.envelopes)
        best = 0
        for e in self.envelopes[:int(n * self.percent)]:
            best = max(best, e.money)
        for e in self.envelopes[int(n * self.percent):-1]:
            if e.money > best:
                print(f"The envelope that was chosen contains {e.money}$")
                return
        print(f"The envelope that was chosen contains {self.envelopes[-1].money}$")

    def display(self):
        return "More_then_N_percent_group_strategy - return envelope with more money that in the highest of N% group"


class N_max_strategy(BaseStrategy):
    def __init__(self, envs, n=3):
        super().__init__(envs)
        self.N = n

    def perform_strategy(self):
        count = 1
        max = 0
        i = 0
        while count < self.N:
            if self.envelopes[i].money > max:
                max = self.envelopes[i].money
                count += 1
            i += 1
        print("The amount is: " + str(self.envelopes[i].money))

    def display(self):
        return "N_max_strategy - return envelope after N max values (defualt N=3)"
