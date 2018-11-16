#Przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
print("PrzeliczaniE liczby zapisanej w formacie binarnym na system dziesiętny".upper())
while True:
    number_bin = input("Podaj liczbę w formacie binarnym [6 znaków]: ")
    number_dec = (int(number_bin[0])*32)+(int(number_bin[1])*16)+(int(number_bin[2])*8)+(int(number_bin[3])*4)+(int(number_bin[4])*2)+(int(number_bin[5])*1)
    print(str(number_bin) + " to w formacie dziesiętnym: " + str(number_dec))
    print("")