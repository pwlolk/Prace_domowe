# Próba integracji kilku poprzednich zadań

import math

def F_to_C():
    print('\nZamiana stopni Fahrenheita na stopnie Celsjusza')
    print('Posłużymy się następującym wzorem [°C]=([°F]-32)/1.8')
    print("")
    temp_F = input('Podaj wartośc temperatury w stopniach Fahrenheita: ')
    temp_C = (float(temp_F)-32)/1.8
    temp_C_2 = format(temp_C, '.2f')
    print('Temperatura w skali Celsjusza: ' + str(temp_C_2) + '°C')
    dec = input('\nPowtórzyć te obliczenia [T] czy wrócić do menu "MULTITOOL" [dowolny klawisz]?')
    if (dec == 'T'):
        F_to_C()
    else:
        options()
        decision_switch()

def circle_area():
    print('\nObliczenie pola koła o zadanym promieniu (r)')
    print('Posłużymy się następującym wzorem A = Pi x r x r')
    print("")
    r = input('Podaj promień koła: ')
    A = math.pi * float(r) * float(r)
    A = format(A, '.5f')
    print('Promień koła z dokładnością do 5-ego miejsca po przecinku: ' + str(A) + ' jednostek kwadratowych')

def rectangle():
    print('\nRysowanie prostokąta o zadanej szerokości i wysokości')
    width = int(input('Podaj szerokość prostokąta: '))
    height = int(input('Podaj wysokość prostokąta: '))
    print('+' + (width - 2) * '-' + '+')
    print((height - 2) * ('|' + (width - 2) * ' ' + '|\n'), end="")
    print('+' + (width - 2) * '-' + '+')

def options(): # Próba stworzenia funkcji wyświetlania opcji, topornie
    list_of_options = [
        ['Zamiana stopni Fahrenheita na stopnie Celsjusza', F_to_C],
        ['Obliczenie pola koła o zadanym promieniu (r)', circle_area],
        ['Rysowanie prostokąta o zadanej szerokości i wysokości', rectangle]
                    ]
    print('\n"MULTITOOL" menu:')
    for i, option in enumerate(list_of_options):
        print('[{}] {}'.format(i+1, option[0]))

def decision_switch():
    decision_M = str(input('\nWybierz interesującą Cię opcję: '))
    if (decision_M == '1'):
        F_to_C()
    elif (decision_M == '2'):
        circle_area()
    elif (decision_M == '3'):
        rectangle()
    else:
        print('Nieprawidłowy wybór, wybierz jeszcze raz')
        options()
        decision_switch() #Nie za bardzo wiem, jak na to wpadłem i dlaczego to działa, ale to chyba działa.

options()
decision_switch()