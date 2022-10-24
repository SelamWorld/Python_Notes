
def Odev1():                # 1. soru Ayak Sayısı
    Animals=[0,0,0]
    Toplam=0
    for i in range(3):      #input almak için for döngüsü
        Animals[i]=int(input("hayvan sayılarını gir:"))
    Toplam=Animals[0]*2+Animals[1]*4+Animals[2]*4   #hayvan sayılarını bacaklarla çarp ve topla (1. hayvanı 2 ile, 2. ve 3. hayvanları 4 ile çarp)
    print(Toplam)           # toplamı yazdır
def Odev2():
    Names=["Halil","Fatih","Vural","Ibrahim","Ahmet"]       # listeyi isimlerle tanımla
    if abs(Names.index("Fatih")-Names.index("Vural"))==1:   # (Fatih ile Vural arasındaki index farkı bire eşit ise yan yanalar) sorgusu. Fark -1 çıkabilir o yüzden abs() kullandım
        print("True")
    else:                                                   # fark bire eşit değil ise yan yana değiller
        print("False")

def Odev3():
    Stringif="hayatımda dite kola gÖrdüm"
    Seslilist=["A","a","E","e","I","ı","İ","i","O","o","Ö","ö","U","u","Ü","ü"]
    Sessizlist=[]
    Stringlist=list(Stringif)
    for i in range(0,len(Stringlist)):
        for j in range(0,len(Seslilist)):
            if Stringlist[i]!=Seslilist[j]:
                Sessizlist.append(Stringlist[i])
                break
    print(Sessizlist)

Odev3()


