numbers = input("Introduceti un sir de numere separate prin virgula: ")
numbersList = numbers.split(",")
for num in numbersList:
    if not num.isdigit():
        numbersList.remove(num)
print(f"Numerele alese sunt: {numbersList}")

menuOption = ""
while menuOption != "4": 
    menuOption = input("1. Fiecare numar la puterea y\n" +
                        "2. Suma tuturor numerelor din lista\n" +
                        "3. Inmultirea fiecarui numar cu y\n" +
                        "4. Iesire\n" +
                        "Alegeti optiunea: ")
    match(menuOption):
        case "1":
            y = input("Introduceti y: ")
            if not y.isdigit():
                print("y trebuie sa fie un numar")
                continue
            print(f"Numerele la puterea {y} sunt: {[float(num) ** float(y) for num in numbersList]}")
        case "2":
            print(f"Suma tuturor numerelor din lista este: {sum([float(num) for num in numbersList])}")
        case "3":
            y = input("Introduceti y: ")
            if not y.isdigit():
                print("y trebuie sa fie un numar")
                continue
            print(f"Numerele inmultite cu {y} sunt: {[float(num) * float(y) for num in numbersList]}")
        case "4":
            break
        case _:
            print("Optiune invalida")
            continue