#Wyświetlanie pierwszej i ostatniej cyfry danej liczby
print("Wyświetlanie pierwszej i ostatniej cyfry danej liczby".upper())
while True:
    number = input("Podaj liczbę: ")
    first_digit = number[0]
    last_digit = number[-1:]
    print("Pierwsza cyfra: " + str(first_digit))
    print("Ostatnia cyfra: " + str(last_digit))
    print("")