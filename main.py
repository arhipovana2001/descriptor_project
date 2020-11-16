class Value:
    def __init__(self):
        self.amount = None

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        if isinstance(value, (float, int)):
            if value >= 0:
                self.amount = int(value - value * instance.commission)
            else:
                raise ValueError('Amount can\'t be < 0')
        else:
            raise TypeError('Amount may be int or float')


class Account:
    amount = Value()

    def __init__(self, commission):
        if isinstance(commission, (float, int)):
            if commission >= 0:
                if type(commission) is float:
                    self.commission = commission
                elif type(commission) is int:
                    self.commission = commission / 100
            else:
                raise ValueError('Commission can\'t be < 0')
        else:
            raise TypeError('Commission may be float or int')


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
