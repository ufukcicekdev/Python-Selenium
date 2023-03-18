#sınıflar
#modüler
#paket yönetimi

import matematik as m
import random


class Human:
    name = "Halit"
    #built in
    #yapıcı block
    #initialized
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi")

    def __str__(self):
        return f"{self.name}"

    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking")


#instance => Örnekleme


human1 = Human("Enes")
# human1.name = "ufuk"
human1.talk("Merhaba")
human1.walk()

print(human1)

human2 = Human("Kadir")
# human2.name = "Kadir"
human2.talk("Merhaba")
human2.walk()
print(human2)

print("*" * 100)
#Modül

print(m.topla(4,4))
print(m.bol(4,4))


print(random.randint(0,100))
