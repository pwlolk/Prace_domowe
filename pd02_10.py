# Latami przestępnymi są te, których numeracja jest podzielna przez 4 i niepodzielna przez 100.

print("Sprawdzenie czy dany rok jest przestępny".upper())
current_year = 2018
while True:
    year = input("Który rok sprawdzić? ")
    year_by_4   = (int(year) / 4)
    year_by_100 = (int(year) / 100)
    if ((year_by_4) - int(year_by_4) == 0):
        condition_by_4 = 1
    else:
        condition_by_4 = 0
    if ((year_by_100) - int(year_by_100) == 0):
        condition_by_100 = 0
    else:
        condition_by_100 = 1
    if (condition_by_4 == 1 and condition_by_100 == 1):
        if(int(year) < current_year):
            print("Rok " + str(year) + " BYŁ rokiem przestępnym.")
            print("")
        elif(int(year) > current_year):
            print("Rok " + str(year) + " BĘDZIE rokiem przestępnym.")
            print("")
        else:
            print("Rok " + str(year) + " JEST rokiem przestępnym.")
            print("")
    else:
        if(int(year) < current_year):
            print("Rok " + str(year) + " NIE BYŁ rokiem przestępnym.")
            print("")
        elif(int(year) > current_year):
            print("Rok " + str(year) + " NIE BĘDZIE rokiem przestępnym.")
            print("")
        else:
            print("Rok " + str(year) + " NIE JEST rokiem przestępnym.")
            print("")