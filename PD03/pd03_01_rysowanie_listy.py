#Rysowanie listy

print("Rysowanie listy".upper())

#Przyjęcie elementów listy
list = []
dec = '0'
while (dec.capitalize() != 'N'):
    element = input('Podaj kolejny element listy: ')
    list.append(element)
    dec = input('Czy chcesz dodać kolejny element? [dowolony znak - tak / N lub n - nie]')

print('')
print(list, end ='')
print(' --> Szczerze mówiąc, nie rozumiem dlaczego wszystkie elementy w liście lądują jako stringi. \n')

# Szerokość okienka tabeli
max_el = max(list, key=len)
cell_length = len(max_el) + 2
cells_total = len(list)

# Rysowanie z wyśrodkowaniem
index = 0
length = len(list)
print('+' + cells_total*((cell_length*'-') + '+'))
print('+', end = '')
while(index < length):
    print(list[index].center(cell_length) + '+', end = '')
    index = index + 1
print('\n+' + cells_total*((cell_length*'-') + '+'))