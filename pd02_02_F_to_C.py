#Zamiana stopni Fahrenheita na stopnie Celsjusza
intro = "Zamiana stopni Fahrenheita na stopnie Celsjusza"
wzor_descr = "Posłużymy się następującym wzorem [°C]=([°F]-32)/1.8"
print("")
print(intro.upper())
print(wzor_descr)
print("")
temp_F = input("Podaj wartośc temperatury w stopniach Fahrenheita: ")
temp_C = (float(temp_F)-32)/1.8
temp_C_2 = format(temp_C, '.2f')
print("Temperatura w skali Celsjusza: " + str(temp_C) + "°C")
print("Temperatura w skali Celsjusza, z dokładnością do drugiego miejsca po przecinku: " + str(temp_C_2) + "°C")
print("")
decyzja = input("Czy chcesz powtórzyć przeliczenie? [T/N]: ")
decyzja = decyzja.capitalize()
if (decyzja == 'T'):
    print("Jeszcze nie wiem jak to zapętlić...")
elif (decyzja == 'N'):
    print("Bye!")
else:
    print("Bezsensowna odpowiedź, bye!")