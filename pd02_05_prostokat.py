#Rysowanie prostokąta o zadanej szerokości i wysokości
print("Rysowanie prostokąta o zadanej szerokości i wysokości".upper())
while True:
    width = int(input("Podaj szerokość prostokąta: "))
    height = int(input("Podaj wysokość prostokąta: "))
    print("+" + (width-2)*"-" + "+", end = "")
    print((height-2)*('\n' + "|" + (width-2)*" " + "|"))
    print("+" + (width-2)*"-" + "+")