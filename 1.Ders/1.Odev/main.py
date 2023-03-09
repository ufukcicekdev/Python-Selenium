#3.Soru Cevapları

#1.Cevap


USER_NAME = "ufuk"
PASSWORD = "112233"

while True:
    userName = input("Kulllanıcı Adını Giriniz?\n")
    passWord = input("Kullanıcı Şifresini Giriniz?\n")
    if userName == "":
        print("KullanıcıAddı Boş Gecilemez!")
    elif passWord == "":
        print("Parola Boş Gecilemez!")
    elif passWord != passWord.isdigit():
        print("Numerik Değer Giriniz!")

    if userName == USER_NAME and passWord== PASSWORD:
        print(f"Giriş Başarılı.Hoş Geldin {userName}")
        break

#2.cevap



# AUTO_PLAY = False
# AUTO_COMPLETE = False

# result = input("Otomatik oynatma açılsın mı? E/H\n")

# if result.upper() == "E":
#     print("Otomatik Oynatma Açıldı!")
# elif result.upper() =="H":
#     print("Otomatik Oynatma Kapand!")

# else:
#     print("Gerçersiz bir değer giridin!")



# 3.cevap


# mail_list = ["@gmail.com","@outlook.com"]


# result = input("Mail adresinizi girin?")s

# for i in mail_list:
#     if i in result:
#         print("Devam edebilirsiniz")
#     else:
#         print("Geçerli mail adresi giriniz!")
