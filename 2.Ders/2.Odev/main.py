#Aldığı isim soy isim ile listeye öğrenci ekleyen

students = []
def addStudens(name, surname):
    print("------------- Tek Öğrenci Ekleme -------------------------")

    if name != "":
        if not name.isdigit() and not surname.isdigit():
            students.append(name + " " + surname)
            print(f"{name} {surname} isimli kayıt eklendi")
        else:
            print("Lütfen isminizde veya soyisminizde sayısal değer olmasın..")

    print(f"Listenin son hali: {students}")

    
#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran

def deleteItems(deleteStudent):
    print("-------------Öğreenci Silme -------------------------")

    if deleteStudent != "" and not deleteStudent.isdigit():
        students.remove(deleteStudent) 
    else:
        print("Lütfen isminizde veya soyisminizde sayısal değer olmasın ve gerçerli bir değer girin")

    print(f"Listenin son hali: {students}")


#Listeye birden fazla öğrenci eklemeyi mümkün kılan

def multipleStudent(multipleStudents):
    print("------------- Çoklu öğrenci Ekleme -------------------------")

    if multipleStudents!= "":
        list2 = []
        for item in multipleStudents.split(","):
            if item!="":
                list2.append(item)
        students.extend(list2)
    print(f"Listenin son hali: {students}")

    

def studentsNumber():
    print("-------------Öğreenci Numarası Listesi -------------------------")
    for i in range(len(students)):
        print(f"Student: {students[i]}, Number: {i}")



def multipleDeleteStudent(multipleDeleteStudents):
    print("------------- Çoklu Öğrenci Silme -------------------------")

    if multipleDeleteStudents !="":
        for item in multipleDeleteStudents.split(","):
            if item!="":
                students.remove(item)


    print(f"Listenin son hali: {students}")


while True:
    name = input("Lütfen isminizi giriniz: \n")
    surname = input("Lütfen soyisminizi giriniz: \n")

    addStudens(name, surname)
    deleteStudent = input("Silmek istedğiniz Öğrencinin Adı-Soyadı: \n")
    deleteItems(deleteStudent)

    multipleStudents = input("Birden Fazla öğrenci eklemek için isim ve Soy isim arasında ',' kulllaranarak ekleyebilirsiniz. İsimleri girin: \n")
    multipleStudent(multipleStudents)

    studentsNumber()

    multipleDeleteStudents = input("Çoklu silme için öğrenci isimleri arasında ',' koyarak ekleyebilirsiniz: \n ")
    multipleDeleteStudent(multipleDeleteStudents)

    quit = input("Çıkmak için 'q' ya basın, devam etmek için enter'a basın: \n")
    if quit.upper() == "Q":
        break





