print("Xos gelmisiz")
eded = input("1-100 arasi ededi daxil edin: ")
eded = int(eded)

eded2 = input("Ededi texmin edin: ")
eded2 = int(eded2)

while eded2 != eded:
    if eded2 > eded:
        print("Boyuk eded yazmisiz")
    elif eded2 < eded:
        print("Kicik eded yazmisiz")
    
    eded2 = input("Ededi texmin edin: ")
    eded2 = int(eded2)
else:
    print("tapdiz! tebrikler")
