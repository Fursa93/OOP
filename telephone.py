class Telephone:
    number = '0731731884'
    counter: int = 0

    def enter_number (self, number ) ->None:
        self.number =  number

    def call_subscriber(self):
        self.counter += 1
        return self.counter

    def call (self):
         self.call_subscriber()

    def get_counter(self) ->int:
        return self.counter


def total_call(telephones) -> int:
    return sum(telephone.get_counter() for telephone in telephones)


Tp1 = Telephone()
Tp2 = Telephone()
Tp3 = Telephone()
Tp1.enter_number('3265656')
K1 = Tp1.number
Tp2.enter_number('56565')
K2 = Tp2.number
Tp3.enter_number('66131')
K3 = Tp3.number
Tp1.call()
Tp1.call()
Tp2.call()
Tp2.call()
Tp3.call()
Tp3.call()
Tp3.call()
Tp3.call()

l = [Tp1, Tp2, Tp3]

print('Numbers: ', K1, K2, K3, 'calls subscriber: ', len(l))
print('total calls:', total_call(l))