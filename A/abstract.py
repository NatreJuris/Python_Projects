from abc import ABC, abstractmethod     #creates abstract class
class shop(ABC):
    def payment(self, total):
        print("total cost:",total)
    @abstractmethod                 #passes in argument
    def pay(self, total):
        pass
class GiftCard(shop):           #implimentation defined
    def pay(self, total):
        print('insufficient funds'.format(total))
obj = GiftCard()
obj.payment("$20")
obj.pay("$20")