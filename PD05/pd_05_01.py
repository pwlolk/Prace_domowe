with open("a.txt", "a+") as file:
    file.seek(0)
    single_string = str(file.readlines())

# Zliczenie znaków w tekście
number_of_letters = len(single_string)-4
for i,znaki in enumerate(single_string):
    if (single_string[i] == "." and single_string[i+1] == "\\" and single_string[i+2] == "n"): # bo break line'y generują 5 dodatkowych znaków
        number_of_letters = number_of_letters - 5
print("Liczba znaków w tekście: " + str(number_of_letters))

# Zliczenie zdań przez zliczenie wystąpień ciągu ". " i paru innych
dots_spaces = 0
for i,znaki in enumerate(single_string):
    if (single_string[i] == "." and single_string[i+1] == " "): # standardowe zakończenia zdań
        dots_spaces = dots_spaces + 1
    if (single_string[i] == "." and single_string[i+1] == "'"): # koniec tekstu
        dots_spaces = dots_spaces + 1
    if (single_string[i] == "." and single_string[i+1] == "\\" and single_string[i+2] == "n"): # breakline'y
        dots_spaces = dots_spaces + 1
print("Liczba zdań w tekście: " + str(dots_spaces))

# Zliczenie słów przez zliczenie wystąpień ciągu " "
spaces = 0
for i,znaki in enumerate(single_string):
    if (single_string[i] == " "):
        spaces = spaces + 1
print("Liczba słów w tekście: " + str(spaces+1))