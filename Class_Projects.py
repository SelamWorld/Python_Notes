

ders = 0  #main#################################main##########MAİN########## MAİN #############################################3

if ders == 3:   # üssü alma
    def sayius():
        x=int(input("sayi girin:"))
        y=int(input("us girin:"))
        print(x**y)
    sayius()
    pass

if ders == 2:  # sayiyi çarpanlarına ayır
    sayi = 48
    for a in range(1,sayi+1):
        if sayi % a==0:
            print(a)
    pass
if ders== 1:   # kelimedeki harflerin hepsi büyük veya küçük ise true değilse false
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
if ders == 0:               # zigzag
    import time, sys

    indent = 0  # How many spaces to indent.
    indentIncreasing = True  # Whether the indentation is increasing or not.

    try:
        while True:  # The main program loop.
            print(' ' * indent, end='')
            print('¯\_(ツ)_/¯')
            time.sleep(0.05)  # Print for 1/10 of a second.

            if indentIncreasing:
                # Increase the number of spaces:
                indent = indent + 1
                if indent == 20:
                    # Change direction:
                    indentIncreasing = False

            else:
                # Decrease the number of spaces:
                indent = indent - 1
                if indent == 0:
                    # Change direction:
                    indentIncreasing = True
    except KeyboardInterrupt:
        sys.exit()
    pass