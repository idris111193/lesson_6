class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name



class NasledieBank(Bank):
    def set_money(self, money):
        self._Bank__money = money

    def get_money(self):
        return self._Bank__money

    def set_key(self, key):
        self._Bank__key = key

    def get_key(self):
        return self._Bank__key


nasledie_bank = NasledieBank("John", 30, 1000, "password")


print(nasledie_bank.get_name())


print(nasledie_bank.get_money())
nasledie_bank.set_money(1500)
print(nasledie_bank.get_money())

# новый класс

class ArgumentDescriptor:
    def __init__(self, default=None):
        self._value = default

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value

class MyBaseClass:
    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    name = ArgumentDescriptor()

class MyDerivedClass(MyBaseClass):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    age = ArgumentDescriptor()
    height = ArgumentDescriptor()


obj = MyDerivedClass("Alice", age=30, height=170)
print(obj.name)
print(obj.age)
print(obj.height)


obj.age = 35
obj.height = 175

print(obj.age)
print(obj.height)


