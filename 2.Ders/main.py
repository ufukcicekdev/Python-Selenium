# #Tip Donusumlari

# faiz = 1.59
# vade = "36"
# krediAdı = "İhtiyaç Kredisi"


# print(type(faiz))
# print(type(vade))
# print(type(krediAdı))

# print(int(vade) + 12)
# #print(int(krediAdı))  #hata alan bir işleem. İnt dönüştürülebilir bile değer olmalı

# print(str(faiz))


# #Kullanıcıdan veri almas

# #vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
# vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
# print(type(vade))
# #print(int(vade) + 12)  #1. yöntem
# vade = vade + 12
# #string inteerpolation
# #sectiğiniz vade sonucu ortaya çıkan vade: 

# print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
# print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

# #1.Format yöntemi
# isim = input("İsminizi Giriniz: ")
# metin = "Merhaba {name}".format(name = isim)
# print(metin)


# # f-string

# metin = f"Hoş Geldiniz {isim}"




#Listeler
#Döngüler
#fonksiyonlar

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)


krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler[0])

print(len(krediler))

krediler.append("Özel Kredi")
print(krediler)


krediler.append("X Kredi")
print(krediler)

krediler.pop(0) # indeex ile çalışır
print(krediler)

krediler.remove("Taşıt Kredisi") # değer ile çalışır bulduğu ilk değeri silecek
print(krediler)


krediler.extend(["Y Kredisi", "Z Kredisi"])  # birden fazla değer atılabilir
print(krediler)


print(dir(list))


# for 
x = 10

for i in range(x):
    print(i)

print("*****")
for i in range(5,10):
    print(i)

print("*****")
for i in range(0,51,10):
    print(i)

print("*****")


# for i in range(0.1,0.5):   ##Hatalı 
#     print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]


for item in krediler:
    print(item)
print("*****")

for i in range(len(krediler)):
    print(krediler[i], i)

print("*****")




while True:
    print("x")
    break

i = 0
while i <len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i +=1

# fonksiyonlar


fiyat = 100
indirim = 20

fiyat = fiyat - indirim
print(fiyat)


def calculate():
    print(100 - 30)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)  



def sayHello(name):
    print(f"Hello {name}")

calculateWithParams(100, 30)

calculate()
sayHello("ufuk")



def calculateAndRead(price,discount):
    return price - discount

newPrice = calculateAndRead(200,50)
print(newPrice)

print("********************************")

#void func tipi
def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price - discount

fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,50)
print(fonk1)
#print(fonk1 + 100)

print(fonk2)

print("********************************")



