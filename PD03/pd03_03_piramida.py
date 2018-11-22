# Rysowanie piramidy z # o zadanej wysokości

print("Rysowanie piramidy z # o zadanej wysokości \n".upper())

rows_total = int(input("Podaj wysokość piramidy [ilość poziomów]: "))
row_current = 1
print('')

while (row_current <= rows_total):
    print(((2*row_current-1)*'#').center(2*rows_total-1))
    row_current = row_current + 1
print('')

#PODEJŚCIA NIEUDANE (NIEDOKŁADNIE WPATRZYŁEM SIĘ W TREŚĆ ZADANIA)

# rows_total = int(input("Podaj wysokość piramidy [ilość poziomów]: "))
# row_current = 1
# while (row_current <= rows_total):
#      print('{:^30}'.format(row_current*'#'))
#      row_current = row_current + 1
# print("")

# rows_total = int(input("Podaj wysokość piramidy [ilość poziomów]: "))
# row_current = 1
# while (row_current <= rows_total):
#     print((row_current*'#').center(rows_total))
#     row_current = row_current + 1
# print("")

# rows_total = int(input("Podaj wysokość piramidy [ilość poziomów]: "))
# row_current = 1
# while (row_current <= rows_total):
#     if (int(row_current)%2 == 1):
#         print(' ' + (row_current*'#').center(rows_total))
#     else:
#         print((row_current*'#').center(rows_total))
#     row_current = row_current + 1
# print("")

# rows_total = int(input("Podaj wysokość piramidy [ilość poziomów]: "))
# row_current = 1
# while (row_current <= rows_total):
#     print((rows_total-row_current)*' ' + row_current*'#')
#     row_current = row_current + 1
# print("")