

ders = -1   #main#################################main##########MAİN########## MAİN #############################################3

if ders == 0:   # üssü alma
    def sayius():
        x=int(input("sayi girin:"))
        y=int(input("us girin:"))
        print(x**y)
    sayius()
    pass

if ders == -2:  # sayiyi çarpanlarına ayır
    sayi = 48
    for a in range(1,sayi+1):
        if sayi % a==0:
            print(a)
    pass
if ders== -1:   # kelimedeki harflerin hepsi büyük veya küçük ise true değilse false
    k=0
    l=0
    c="selma"
    m=len(c)
    for a in c:
        if a.isupper():
            k+=1
        else:
            l+=1

    if k==m or l==m:
        print("true")
    else:
        print("false")


    pass