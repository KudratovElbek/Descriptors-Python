class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        print(f"{self.name} atributi o'qildi")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"{self.name} atributiga {value} yozildi")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"{self.name} atributi o'chirildi")
        del instance.__dict__[self.name]

class MyClass:
    attr = Descriptor('attr')

obj = MyClass()
obj.attr = 10  # "attr atributiga 10 yozildi"
print(obj.attr)  # "attr atributi o'qildi" va "10" chiqadi
del obj.attr  # "attr atributi o'chirildi"
