from basestrategy import BaseStrategy

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

