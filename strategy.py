class BaseStrategy:

	def __init__(self, envs):
		self.envelopes = envs

	def play(self):
		self.perform_strategy()

	def perform_strategy(self):
        while envelope in self.envelopes:
            print(envelope.money)
            a = input("The amount is:" + envelope.money + " Take(T) or Leave(L)")
            if(a == 'T'):
                print(envelope.money)

            elif(a=='L'):
                pass
                temp = envelope
            else:
                print("Wrong Input Envelope Was Skipped")
        print("returning last envelope")
	print(envelope.money)


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envs):
        super(self, envs)

    def perform_startegy(self):
        rnd = random.randint(0, 99)
        print(self.envelopes[rnd].money)


class More_then_N_percent_group_strategy(BaseStrategy):

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

    def perform_startegy(self):
        count = 1
        max = 0
        i = 0
        while count < self.n:
            if self.envelopes[i].money > max:
                max = self.envelopes[i].money
                count += 1
            i += 1
        print(self.envelopes[i].money)
