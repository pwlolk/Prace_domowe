#Sprawdzenie czy liczba jest parzysta.
print("Sprawdzenie czy zadana liczba całkowita jest parzysta".upper())
while True:
    number = input("Podaj liczbę całkowitą: ")
    number_by_2 = (int(number)/2)
    if ((number_by_2) - int(number_by_2) == 0):
        print("Liczba: " + str(number) + " jest liczbą parzystą")
    else:
        print("Liczba: " + str(number) + " jest liczbą nieparzystą")
        print ("")

#Sporo zasobów na heheszki użytkowników, np. podanie 0, podanie liczby niecałkowitej, podanie litery itd.