class atm :

    def __init__(self,balance,name):
        self.balance = balance
        self.name = name
        self.withdrawals = []

    def withdraw(self, request) :

        if request > self.balance:
            print("not enough")
        elif request < 0 :
            print("take care enter right number")
        else :
            self.withdrawals.append(request)
            while request > 0 :
                if request >= 100 :
                    request -= 100
                    print("give 100")
                elif request >= 50 :
                    request -= 50
                    print("give 50")
                elif request >= 10 :
                    request -= 10
                    print("give 10")
                elif request <= 5 :
                    request -= 5
                    print("give 5")

        return self.balance - request

    def show_withdrawals(self):
        for w in self.withdrawals :
            print(w)

atm1 = atm(1000,"baraka")
atm1.withdraw(100)
atm1.withdraw(200)

atm1.show_withdrawals()


