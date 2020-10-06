"""
    Authors: Yoav Katz, Guy Haviv, Sahar Shaul.
    Date: 06/10/2020
"""

import random


class BaseStrategy:
    """
        Class which represents the basic strategy of letting the user select envelopes manually.
        Also serves as the base class for other strategy classes.
    """
    def __init__(self, envs):
        # Constructor function
        self.envelopes = envs

    def play(self):
        # Function which activates the strategy on the envelopes which were defined before.
        self.perform_strategy()

    def perform_strategy(self):
        # Lets the user manually choose for each envelope whether he likes to take it or not.
        for envelope in self.envelopes:
            letter = input("The amount is: " + str(envelope.money) + " Take(T) or Leave(L) - ")
            if letter == 'T':
                print(envelope.money)
                return
            elif letter != 'L':
                print("Wrong Input - Envelope Was Skipped")
        print("Returning last envelope")
        print(self.envelopes[-1].money)

    def display(self):
        # Returns a message which displays what the class does
        return r"BaseStrategy - user select manually envelopes"


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envs):
        # Constructor function
        super().__init__(envs)

    def perform_strategy(self):
        # Chooses a random envelope
        rnd = random.randint(0, len(self.envelopes)-1)
        print("The amount is: " + str(self.envelopes[rnd].money))

    def display(self):
        # Returns a message which displays what the class does
        return r"Automatic_BaseStrategy - random selection of envelop"


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envs, p=0.25):
        # Constructor function
        super().__init__(envs)
        self.percent = p

    def perform_strategy(self):
        # Choose envelope with more money that in the highest of N% group
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
        # Returns a message which displays what the class does
        return r"More_then_N_percent_group_strategy - return envelope with more money that in the highest of N% group"


class N_max_strategy(BaseStrategy):
    def __init__(self, envs, n=3):
        # Constructor function
        super().__init__(envs)
        self.N = n

    def perform_strategy(self):
        # Choose envelope after N max values (default N=3)
        count = 1
        best = 0
        i = 0
        while count < self.N:
            if self.envelopes[i].money > best:
                best = self.envelopes[i].money
                count += 1
            i += 1
        print("The amount is: " + str(self.envelopes[i].money))

    def display(self):
        # Returns a message which displays what the class does
        return r"N_max_strategy - return envelope after N max values (defualt N=3)"
