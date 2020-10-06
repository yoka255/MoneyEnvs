from abc import ABC
class BaseStrategy(ABC):

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


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, n):
        super(self,n)

    def perform_strategy(self):
        while envelope in self.EnvelopeArr:
            print(envelope.money)
            a = input("The amount is:" + envelope.money + " Take(T) or Leave(L)")
            if(a == 'T'):
                return envelope

            elif(a=='L'):
                pass
                temp = envelope
            else:
                print("Wrong Input Envelope Was Skipped")
        print("returning last envelope")
        return temp


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
