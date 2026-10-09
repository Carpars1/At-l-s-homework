
class Person:
    #name=""
    #age=0
    #gender=""
    job="developer"   #zorunlu olmayanları ve değiştirilebilir olanları buraya yazıyoruz

    def __init__(self,name,age,gender):   #zorunlu olarak girmemiz gerekiyorsa buraya yazıyoruz
        self.name=name
        self.age=age
        self.gender=gender

    def print_name(self):
        print(self.name)  #name değişkenini üstten çeker



eto=Person("Eto",25,"male")
print(eto.name)
print(eto.gender)
print(eto.age)

eto.print_name()
print(eto.job)

eto.job="engineer"
print(eto.job)
