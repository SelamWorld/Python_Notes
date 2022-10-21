import math # math modülünü import et
def print_hi(sayi):         # use two dots after function definition
    name = input()
    print("Hi", name, sayi)

ders = 6
# list
if ders == 1:   # after "if" must use two dots. "and" = && "or" = ||, "if" block can not be empty so use "pass"
    pass
    listme=["a", "g", "k", "e", "b", "m"]
    x= slice(2,4)   # 2 den 4 e kadar olan değerleri ver4
    print(listme[x])
    print(sorted(listme))   # sort one thing as alphabet or numeric (string, array, list)
if ders == 2:   # import library

    print(math.sqrt(16))    # düz import ettiysen bu şekilde kullanıcan
    print(dir(math))    # math modülündeki fonksiyon ve değişkenleri verir
    pass
    print()
if ders == 3:   #dictionary
    sozluk = {"kitap":"book", "dil":"language", "ev": "home"}
    print(sozluk["kitap"])  # index ile çağırırken köşeli parantez kullanılır , Keyler demet olabilir
    print( sozluk.values()) # values verir
    pass
if ders == 4:
    print("a","b","c",sep="[]") # sep=" " ne ile ayırmak istediğni gir, end=" " satır atlamadn ayırmak istediğini gir
    pass
if ders == 5:
    liste=[]    # listeye öğe ekleme
    alfabe="abcdefghijklmnprst"
    for i in alfabe:
        liste+= [i]
    print(liste)
    pass
if ders== 6:    # zigzag
    import time, sys

    indent = 0  # How many spaces to indent.
    indentIncreasing = True  # Whether the indentation is increasing or not.

    try:
        while True:  # The main program loop.
            print(' ' * indent, end='')
            print('********')
            time.sleep(0.1)  # Print for 1/10 of a second.

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
