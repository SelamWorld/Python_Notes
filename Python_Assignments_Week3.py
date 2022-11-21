def Odev1():        #fibonacci sayıları 1
    num1=1
    num2=1
    num3=0
    fibnum=int(input("kaçıncı fşbonacci sayısını istiyorsunuz:"))
    if fibnum==1 or fibnum==2:
        num3=1
    else:
        for i in range(fibnum-2):
            num3 = num2+num1
            num1 = num2
            num2 = num3
    print(num3)

def Odev2():        # Apocalyptic Sayılar
    Num=int(input("sayı girin: "))      # sayıyı input al
    Us=2**Num                           # 2 nin üssü olarak al
    Sus=str(Us)                         # string yap
    j=0                                 # kaç tane 666 içerdiği
    ix=0                                # gerisini ben de bilmiyorum bi şekilde yaptım hocam
    for i in range(len(Sus)):
        if ix==len(Sus)-2:
            break
        if Sus[ix]=="6":
            if Sus[ix+1]=="6" and Sus[ix+2]=="6":
                j += 1
                ix+=2
        ix+=1
    if j==0:
        print("Apocalytpic değil")
    else:
        print("{}. dereceden Apocalytpic".format(j))

def Odev3(str):
    lstr=str.split("zip")
    if len(str)>=3:
        print(str.find("zip",2))
    else:
        print("-1")

def Odev4(str):
    lstr=str.split(" ")                 # kelimeleri ayırarak bir dizi oluşturdum
    for i in range(len(lstr)):
        a=[]                            # keliemelrin harflerini içine atacağım dizi her keliem bittiğinde sıfırlanacak
        a=list(lstr[i])                 # kelimelerin herbirinin harflerini a dizisine atadım
        for j in range(len(lstr[i])):
            if j != 0 and j != len(lstr[i]) - 1:            # kelimenin ilk ve son harfi yani a[] dizisinin ilk ve osn elemanı değilse
                a[j]="-"                                    # a nın elemanlarını "-" ile değiştri
            print(a[j],end=" ")                             # ve yaz

def Odev5():                            # sadeleştirme
    a=[[[[[["kek"]]]]]]
    c=""
    while True:
        b=a.pop()                       # a nın içindeki elemanı b ye ata bu sayede 1 parantezden kurtulduk
        a=b                             # a yı b yap ve pop işlemini tekrarla
        if type(b)==type(c):            # en son parantezden de kurtulduğumuzda b bir str oluyor
            break
    d=[""]
    d[0]=a
    print(d)
    pass

Odev5()

