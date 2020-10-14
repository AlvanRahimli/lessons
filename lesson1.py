# Ekranda nəyisə göstərmək üçün:
print("Salam!")

# İstifadəçidən mətn istəmək üçün
# Məsələn,
ad = input("Adınız nədir?")

# String-i tam ədədə çevirmək üçün:
yas = input("Neçə yaşınız var?")
yas = int(yas) # Bu yaş veriləni artıq tam ədəd olacaq

# Riyazi əməllər
# +  -  *  /  %  **
print(5 + 7)        # Ededleri toplayir
print(4 - 2)        # Ededleri cixir
print(5 * 8)        # Ededleri vurur
print(15 / 4)       # Ededleri bolur
print(14 % 4)       # 14-ün 4-ə bölünməsindən alınan qalığı tapır
print(2 ** 3)       # 2-nin kubunu tapır. Yəni, 2*2*2=8 hesablayir
 
# Müqayisə əməlləri
# >   <   >=   <=   ==   !=

print(5 > 2)        # Ekrana "True" yazılacaq
print(15 < 6)       # Ekrana "False" yazılacaq
print(100 == 100)   # Ekrana "True" yazılacaq


# Şərt yazmaq
eded1 = input("Birinci ədədi deyin. ")
eded1 = int(eded1)
if eded1 > 100:
    print("Bəli, 100-den boyukdur!")
elif eded1 == 100:
    print("Eded1 100-e beraberdir")
else:
    print("Eded1 100-den kicikdir")

# Ikinci misal:
print("Adiniz nedir?")
ad = input()
print("Parolunuz nedir?")
parol = input()

if ad == "alvan" and parol == "12345":
    print("Kecin, Alvan")
elif ad == "amin" and parol == "qwerty":
    print("Kecin, Amin")
else:
    print("Sehv ad ve parol")
