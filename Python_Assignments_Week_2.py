def sayi_harf_say(stringifade):         # 1- Sayı ve Harfleri Say
    sayi_list=["0","1","2","3","4","5","6","7","8","9"]
    stringlist=list(stringifade)       # strng ifadeyi listeye çevirdim ki içindekileri teker teker kontrol edebileyim
    numbers=0                       # rakamların sayısı
    letters=0                       # harflerin sayısı
    for i in range(len(stringlist)):        # string listedeki elementler sayılara eşit mi kontro let
        if stringlist[i] in sayi_list:      # rakama eşit ise bir arttır
            numbers+=1
        elif stringlist[i]==" ":            # boş ise bişiy yapma
            pass
        else:                               # rakama eşit değil ise harf sayısını bir arttır
            letters+=1
    print("harfler= ",letters)
    print("sayılar= ", numbers)

def ayin_gunleri():
    pass
def kucuk_buyuk_sayılar(stringifade):       # 3. Küçük ve Büyük Sayıları

    smallest=10
    biggest=-10
    intlist=[]                              #sayıların tamamını içine laıcak liste
    temp=-1                                 # sayı negatif ise bir döngü atlama değişkeni
    for i in range(0,len(stringifade),1):
        if i==temp:                         # sayı negatif ise bir döngü atla
            continue
        if stringifade[i]==" ":             # boşluk ise alma
            pass
        elif stringifade[i]=="-":           # negatif ifade ile başlıyor mu
            intlist.append(int(stringifade[i+1])*(-1))      # eksiden sonraki sayıyı al -1 ile çarp
            temp=i+1                                        # sonraki döngüyü atla
        else:
            intlist.append(int(stringifade[i]))             # negatif sayı değilse direk al
    for i in range(len(intlist)):                   # en büyük ve küçük sayıyı bulma döngüsü
        if intlist[i]<smallest:
            smallest=intlist[i]
        if intlist[i]>biggest:
            biggest=intlist[i]

    print(biggest," ", smallest)


def Bes_harf_cevir():
    pass
