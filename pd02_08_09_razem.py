#Sprawdzenie czy liczba jest podzielna przez 3 lub 5 lub 7 oraz czy jest podzielna przez 3 i 5 i 7.
print("Sprawdzenie czy zadana liczba całkowita jest podzielna przez 3, 5 lub 7.".upper())
while True:
    number = input("Podaj liczbę całkowitą: ")
    number_by_3 = (int(number) / 3)
    number_by_5 = (int(number) / 5)
    number_by_7 = (int(number) / 7)
    if ((number_by_3) - int(number_by_3) == 0):
        statement_by_3 = "jest"
    else:
        statement_by_3 = "nie jest"
    if ((number_by_5) - int(number_by_5) == 0):
        statement_by_5 = "jest"
    else:
        statement_by_5 = "nie jest"
    if ((number_by_7) - int(number_by_7) == 0):
        statement_by_7 = "jest"
    else:
        statement_by_7 = "nie jest"
    if (statement_by_3 == "jest" and statement_by_5 == "jest" and statement_by_7 == "jest"):
        print("Liczba " + str(number) + " jest podzielna przez 3, 5 i 7.")
        print("")
    elif (statement_by_3 == "nie jest" and statement_by_5 == "nie jest" and statement_by_7 == "nie jest"):
        print("Liczba " + str(number) + " nie jest podzielna przez ani przez 3, ani przez 5, ani przez 7.")
        print("")
    else:
        print("Liczba " + str(number) + " " + str(statement_by_3) + " podzielna przez 3, " + str(statement_by_5) + " podzielna przez 5 i " + str(statement_by_7) + " podzielna przez 7.")
        print ("")