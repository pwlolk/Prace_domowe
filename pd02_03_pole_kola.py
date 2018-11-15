# Obliczenie pola koła
import math
print("Obliczenie pola koła o zadanym promieniu (r)".upper())
print("Posłużymy się następującym wzorem A = Pi x r x r")
print("")
r = input("Podaj promień koła: ")
A = math.pi*float(r)*float(r)
A = format(A, '.5f')
print("Promień koła z dokładnością do 5-ego miejsca po przecinku: " + str(A) + " jednostek kwadratowych")
print("")
decyzja = input("Czy chcesz powtórzyć przeliczenie? [T/N]: ")
decyzja = decyzja.capitalize()
if (decyzja == 'T'):
    print("Jeszcze nie wiem jak to zapętlić...")
elif (decyzja == 'N'):
    print("Bye!")
else:
    print("Bezsensowna odpowiedź, bye!")