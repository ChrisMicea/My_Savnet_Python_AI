print("1. Cappucino - 4 lei...")
print("2. Espresso - 3.5 lei...")
optiune = input("Alegeti optinea? [1, 2]: ")
if optiune == "1" or optiune == '2':
    bancnota = input("Introduceti bancnota [5, 10]: ")
    if bancnota == "5" or bancnota == "10":
        rest = int(bancnota) - (4 if optiune == '1' else 3.5)
        print(f"Veti primi restul de {rest} lei.")
        print("Produsul se livreaza...")
    else:
        print("Bancnota invalida")
else:
    print("Optiunea nu este valida")