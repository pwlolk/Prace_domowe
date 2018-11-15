#Zamiana stopni Celsjusza na stopnie Fahrenhaita
intro = "Zamiana stopni Celsjusza na stopnie Fahrenheita"
wzor_descr = "Posłużymy się następującym wzorem [ºF]=[ºC]*1.8+32"
print("")
print(intro.upper())
print(wzor_descr)
print("")
temp_C = input("Podaj wartośc temperatury w stopniach Celsjusza: ")
temp_F = float(temp_C)*1.8+32
temp_F_2 = format(temp_F, '.2f')
print("Temperatura w skali Fahrenheita: " + str(temp_F) + "ºF")
print("Temperatura w skali Fahrenheita, z dokładnością do drugiego miejsca po przecinku: " + str(temp_F_2) + "ºF")
print("")
decyzja = input("Czy chcesz powtórzyć przeliczenie? [T/N]: ")
decyzja = decyzja.capitalize()
if (decyzja == 'T'):
    print("Jeszcze nie wiem jak to zapętlić...")
elif (decyzja == 'N'):
    print("Bye!")
else:
    print("Bezsensowna odpowiedź, bye!")