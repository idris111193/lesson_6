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

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


obj = MyDerivedClass("Alice", age=30, height=170)


obj.name = "Bob"
obj.age = 35
obj.height = 175


print(obj.name)
print(obj.age)
print(obj.height)
