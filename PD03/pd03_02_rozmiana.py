# Rozmiana kasy (poprawka, bo w wersji z groszami dziesiętnymi gdzieś fikały 0)

list_coins = (500,200,100,50,20,10,5,2,1)
list_quantity = [0,0,0,0,0,0,0,0,0]

amount = float(input('Podaj kwotę do zamiany (w formacie złote.grosze): '))
amount = amount*100

index = 0
while (index < 9):
    list_quantity[index] = int(amount/list_coins[index])
    amount = amount - (list_quantity[index])*(list_coins[index])
    index = index + 1

print_index = 0
while (print_index < 3):
    print(str(int(list_coins[print_index]/100)) + ' zł:\t' + str(list_quantity[print_index]))
    print_index = print_index + 1
while (print_index < 9):
    print(str(int(list_coins[print_index])) + ' gr:\t' + str(list_quantity[print_index]))
    print_index = print_index + 1

# Rozmiana kasy

# print("Wymiana/zamiana określonej kwoty na bilon \n".upper())

# list_coins = (5,2,1,0.50,0.20,0.10,0.05,0.02,0.01)
# list_quantity = [0,0,0,0,0,0,0,0,0]

# amount = float(input('Podaj kwotę do zamiany (w formacie złote.grosze): '))

# index = 0
# while (index < 9):
#     list_quantity[index] = int(amount/list_coins[index])
#     amount = amount - (list_quantity[index])*(list_coins[index])
#     index = index + 1

# print_index = 0
# while (print_index < 3):
#     print(str(list_coins[print_index]) + ' zł:\t' + str(list_quantity[print_index]))
#     print_index = print_index + 1
# while (print_index < 9):
#     print(str(int(100*list_coins[print_index])) + ' gr:\t' + str(list_quantity[print_index]))
#     print_index = print_index + 1
    
# Rozmiana kasy

list_coins = (500,200,100,50,20,10,5,2,1)
list_quantity = [0,0,0,0,0,0,0,0,0]

amount = float(input('Podaj kwotę do zamiany (w formacie złote.grosze): '))
amount = amount*100

index = 0
while (index < 9):
    list_quantity[index] = int(amount/list_coins[index])
    amount = amount - (list_quantity[index])*(list_coins[index])
    index = index + 1

print_index = 0
while (print_index < 3):
    print(str(int(list_coins[print_index]/100)) + ' zł:\t' + str(list_quantity[print_index]))
    print_index = print_index + 1
while (print_index < 9):
    print(str(int(list_coins[print_index])) + ' gr:\t' + str(list_quantity[print_index]))
    print_index = print_index + 1   
