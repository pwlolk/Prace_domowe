#Rysowanie listy

print("Rysowanie listy".upper())
lista = ['col1','col2','col3']
len = len(lista)
index = 0

print('+' + len*('----' + '+'))
print('+', end = '')
while(index < len):
    print(str(lista[index]) + '+', end = '')
    index = index + 1
print('\n+' + len*('----' + '+'))
