import math
print("Różne obliczenia".upper())
print("Wybierz opcję")
print("[1] Konwersja °F->°C")
print("[2] Konwersja °C->°F")
print("[3] Obliczenie pola koła")
option = input("")
if (option == "1"):
    #Zamiana stopni Celsjusza na stopnie Fahrenhaita
    print("")
    print("Zamiana stopni Celsjusza na stopnie Fahrenheita")
    print("Posłużymy się następującym wzorem [°F]=[°C]*1.8+32")
    temp_C1 = input("Podaj wartośc temperatury w stopniach Celsjusza: ")
    temp_F1 = float(temp_C1)*1.8+32
    temp_F1_2 = format(temp_F1, '.2f')
    print("Temperatura w skali Fahrenheita: " + str(temp_F1) + "°F")
    print("Temperatura w skali Fahrenheita, z dokładnością do drugiego miejsca po przecinku: " + str(temp_F1_2) + "°F")
    print("")
    dec1 = input("Czy chcesz powtórzyć przeliczenie? [T/N]: ")
    dec1 = dec1.capitalize()
    if (dec1 == 'T'):
        print("Jeszcze nie wiem jak to zapętlić...")
    elif (dec1 == 'N'):
        print("Bye!")
    else:
        print("Bezsensowna odpowiedź, bye!")

elif (option == '2'):
    #Zamiana stopni Fahrenheita na stopnie Celsjusza
    print("")
    print("Zamiana stopni Fahrenheita na stopnie Celsjusza")
    print("Posłużymy się następującym wzorem [°C]=([°F]-32)/1.8")
    temp_F2 = input("Podaj wartośc temperatury w stopniach Fahrenheita: ")
    temp_C2 = (float(temp_F2)-32)/1.8
    temp_C2_2 = format(temp_C2, '.2f')
    print("Temperatura w skali Celsjusza: " + str(temp_C2) + "°C")
    print("Temperatura w skali Celsjusza, z dokładnością do drugiego miejsca po przecinku: " + str(temp_C2_2) + "°C")
    print("")
    dec2 = input("Czy chcesz powtórzyć przeliczenie? [T/N]: ")
    dec2 = dec2.capitalize()
    if (dec2 == 'T'):
        print("Jeszcze nie wiem jak to zapętlić...")
    elif (dec2 == 'N'):
        print("Bye!")
    else:
        print("Bezsensowna odpowiedź, bye!")

elif (option == '3'):
    # Obliczenie pola koła
    print("")
    print("Obliczenie pola koła o zadanym promieniu".upper() + " (r)")
    print("Posłużymy się następującym wzorem A = Pi x r x r")
    rad = input("Podaj promień koła: ")
    area = math.pi*float(rad)*float(rad)
    area = format(area, '.5f')
    print("Promień koła z dokładnością do 5-ego miejsca po przecinku: " + str(area) + " jednostek kwadratowych")
    print("")
    dec3 = input("Czy chcesz powtórzyć przeliczenie? [T/N]: ")
    dec3 = dec3.capitalize()
    if (dec3 == 'T'):
        print("Jeszcze nie wiem jak to zapętlić...")
    elif (dec3 == 'N'):
        print("Bye!")
    else:
        print("Bezsensowna odpowiedź, bye!")

else:
    print("")
    print("Nie ma takiej opcji ani możliwości zapętlenia, uruchom program jeszcze raz.")