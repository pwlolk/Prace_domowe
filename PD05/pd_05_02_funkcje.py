print("Statystyki pliku\n".upper())
txt_file = input("Jaki plik przeanalizować?: ")

def letters(txt_file):
    with open(txt_file, "a+") as file:
        file.seek(0)
        single_string = str(file.readlines())
    number_of_letters = len(single_string)-4
    for i,znaki in enumerate(single_string):
        if (single_string[i] == "." and single_string[i+1] == "\\" and single_string[i+2] == "n"): # bo break line'y generują 5 dodatkowych znaków
            number_of_letters = number_of_letters-5
    return number_of_letters

# def sentences(txt_file):
#     with open(txt_file, "a+") as file:
#         file.seek(0)
#         single_string = str(file.readlines())
#     dots_spaces = 0
#     for i,znaki in enumerate(single_string):
#         if (single_string[i] == "." and single_string[i+1] == " "): # standardowe zakończenia zdań
#             dots_spaces = dots_spaces+1
#         if (single_string[i] == "." and single_string[i+1] == "'"): # koniec tekstu
#             dots_spaces = dots_spaces+1
#         if (single_string[i] == "." and single_string[i+1] == "\\" and single_string[i+2] == "n"): # breakline'y
#             dots_spaces = dots_spaces+1
#     print("Liczba zdań w tekście: " + str(dots_spaces))
#
# def words(txt_file):
#     with open(txt_file, "a+") as file:
#         file.seek(0)
#         single_string = str(file.readlines())
#     spaces = 0
#     for i,znaki in enumerate(single_string):
#         if (single_string[i] == " "):
#             spaces = spaces+1
#     print("Liczba słów w tekście: " + str(spaces+1))

def characters_analyzed_counter(): #Wykonanie każdej statystyki powinno podbijać licznik, nawet jeżeli się powtarza
    with open ("characters_analyzed.stat", "r+") as file:
        chars_count = int(file.read())
        chars_count = chars_count + int(letters(txt_file))
        file.seek(0)
        file.write(str(chars_count))
        return(chars_count)

print("Liczba znaków w pliku: " + str(letters(txt_file)))
# sentences(txt_file)
# words(txt_file)
print("Dotyczas przeanalizowano łącznie " + str(characters_analyzed_counter()) + " znaków.")