# Rysowanie piramidy z # o zadanej wysokości

print("Rysowanie piramidy z # o zadanej wysokości \n".upper())

rows_total = int(input("Podaj wysokość piramidy [ilość poziomów]: "))
row_current = 1
print('')

while (row_current <= rows_total):
    print(((2*row_current-1)*'#').center(2*rows_total-1))
    row_current = row_current + 1
print('')

# Wersja "Krzywa choinka" :o)
# rows_total = int(input("Podaj wysokość piramidy [ilość poziomów]: "))
# row_current = 1
# while (row_current <= rows_total):
#     print((rows_total-row_current)*' ' + row_current*'#')
#     row_current = row_current + 1
# print("")