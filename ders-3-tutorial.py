# Deyer tipləri:
- tam ədəd: 5  7  96  -75   (integer)
- kəsr ədəd: 5.4  8.9   -4.7
- string: "alvan"  "amin" ""
- list: ["alvan", "amin", "", "salam"]

# Ekrana yazmaq üçün:
- print(...)
- Ekrana string yazmaq: print("amin")
- Ekrana ədəd yazmaq: print(15)

# İstifadəçidən dəyər almaq
input("instruksiya")
address = input("Harada yaşayırsınız?")
yash = input("Neçə yaşın var?")

# String-i ədəd-ə çevirmək üçün:
yash = int(yash)

# Dəyər tanımlamaq
x = 15    #-> tam ədəd
y = 4.8   #-> kəsr ədəd
ad = "amin"   #-> string
adlar = ["alvan", "amin", "", "salam"]    #-> string ardıcıllıq
yaslar = [15, 19, 35, 57]      #-> tam ədəd ardıcıllığı
boylar = [1.7, 1.65, 2.1]      #-> kəsr ədəd ardıcıllığı

cem = x + y
ferq = x - y

# müqayisə etmək
print(5 > 7)    #-> False
print(56 == 56)    #-> True
print(address == "Baku")   #-> ...

# şərt vermək
if address == "Baku":
    print("Beli, siz bakidansiniz!")
elif address == "Lerik":
    print("Siz Lerikdənsiniz!")
else:
    print("Siz başqa yerdənsiz")

if yash > 25:
    print("25 yashdan boyuk!")
elif yash < 25:
    print("25 yashdan kiçikdi")
else:
    print("25 yaşınız var")


# List yaratmaq üçün:
adlar = ["amin", "alvan", "huseyn"]

# Listə element əlavə etmək
adlar.append("salam")

# Listdən element silmək:
adlar.remove("alvan")

# Listin hansısa elementi üçün
adlar[2]
if adlar[2] == "amin":
    # Hər hansısa işlər

if yashlar[6] > 16:
    # Hər hansısa işlər


# Listin bir neçə elementi üçün
adlar[2:7]
adlar[:4]
adlar[3:]

# Listin hər bir elementinə baxmaq üçün
for ad in adlar:
    # Hər hansısa işlər

# Ədəd aralığı üçün
for eded in range(0, 15):
    # Hər hansısa işlər

# Elementin listin içində olub-olmamağına baxmaq:
if "amin" in adlar:
    # Hər hansısa işlər

istenilen = input("Hansi adi yoxlayaq? ")
if istenilen in adlar:
    # Hər hansısa işlər


