# Halil İbrahim Çalış ALl rights reserved. Github: https://github.com/SelamWorld/Python_Notes

def Ayak_Sayisi():                # 1. soru AYAK SAYISI
    Animals=[0,0,0]
    Toplam=0
    for i in range(3):      #input almak için for döngüsü
        Animals[i]=int(input("hayvan sayılarını gir:"))
    Toplam=Animals[0]*2+Animals[1]*4+Animals[2]*4   #hayvan sayılarını bacaklarla çarp ve topla (1. hayvanı 2 ile, 2. ve 3. hayvanları 4 ile çarp)
    print(Toplam)           # toplamı yazdır
def Yaninda_Mi():                # 2. soru YANINDA MI ?
    Names=["Fatih","anan","Vural","Ibrahim","Fatih"]        # listeyi isimlerle tanımla
    if abs(Names.index("Fatih")-Names.index("Vural"))==1:   # (Fatih ile Vural arasındaki index farkı bire eşit ise yan yanalar) sorgusu. Fark -1 çıkabilir o yüzden abs() kullandım
        print("True")
    else:                                                   # fark bire eşit değil ise yan yana değiller
        print("False")

def Sesli_Harf_Kaldir():                # 3. soru SESLİ HARF KALDIR
    Stringinput="hayatımda diyet kola gÖrmedim"             # input alınan string cümle
    Seslilist=["A","a","E","e","I","ı","İ","i","O","o","Ö","ö","U","u","Ü","ü"] # sesli büyük ve küçük harflerden oluşan liste
    Stringoutput=""                                         # output vereceğimiz sesszi harflerden oluşa nstringi atacağımız değişken
    Stringlist=list(Stringinput)                            # input alınan string içindeki harfleri listeye atayıp ayırdık
    for i in range(0,len(Stringlist)):                      # string ifadenin harflerinden oluşan listeyi for döngüsü açtık
          if not Stringlist[i] in Seslilist:                # eğer cümledeki harf sesli harf listesindek bulunmuyorsa
             Stringoutput+=Stringlist[i]                    # output vereceğimiz string değişkenine harfleri ekle
    print(Stringoutput)                                     # output ver

def Hangi_Yuzyil():     # 4. Soru HANGİ YÜZYIL
    Year=1900           # Yıl değişkeni
    Century=0           # asır değişkeni
    if Year%100==0:     # yıl % 100 kalan 0 ise bi alt yüzyılı ver
        Century= Year//100      # yüzyılı; yılı 100 e bölerek hesapla
    else:                       # Yıl 1000'in katı değilse
        Century= Year//100+1    # Yılı 100 e bölerek yüyılı bul ve bir ekle
    print("{}. Yüyıldasınız".format(Century))

def Index_Carpici():     # 5. Soru İNDEX ÇARPICI
    Indexlist=[2,3,4,5,6]           # sayı listesi
    Toplam=0                        # Toplam değişkeni
    for i in range(len(Indexlist)): # listeyi for dngüsüne al
        Toplam+=Indexlist[i]*i      # toplamı listenin her bir elemanının indexiyle çarpıp arttır
    print(Toplam)

