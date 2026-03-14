parola = 7788
parola_introdusa = input("Introduceti parola: ")
if parola_introdusa.isnumeric() and int(parola_introdusa) == parola:
    print("Parola corecta")
else:
    print("Parola incorecta")