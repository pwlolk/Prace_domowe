# Wiek psa

print('obliczanie "prawdziwego" wieku psa \n'.upper())

while True:
    dogs_human_years = int(input("Ile pełnych lat ma pies? "))
    dogs_human_months = int(input("Ile dodatkowo miesięcy ma pies? "))
    dogs_human_months_only = dogs_human_years*12+dogs_human_months

    if (dogs_human_months_only <= 24):
        print('"Psi" wiek psa to ' + str(format(float(dogs_human_months_only*10.5/12), '.2f')) + ' lat.\n')
    else:
        print('"Psi" wiek psa to ' + str(format(float(21+((dogs_human_months_only-24)*4.5/12)), '.2f')) + ' lat.\n')