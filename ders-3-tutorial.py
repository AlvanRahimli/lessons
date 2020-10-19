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

----------------------------------------------------------

while *aparmali das qalib*:
    *dasi apar*

say = 20
while say > 0:
    print("say 0-dan boyukdur")
    say -= 1
else:
    print("say 0-a beraberdir")
