def suma(lista: list) -> float:
    sum = 0

    for i in lista:
        sum += i
    
    return sum

def medie(lista: list) -> float:
    avg = 0.0

    for i in lista:
        avg += i
    
    return avg / len(lista)

def putere(lista: list) -> float:
    # Nu inteleg la ce se refera prin "putere"
    power = 1.0

    for i in lista:
        power *= i
    
    return power

meniu = {
    "1": medie,
    "2": suma,
    "3": putere
}

def get_input_numbers() -> list:
    print("Introduceti numere. Cand sunteti gata, introduceti x.")
    numbers = []

    while True:
        number = input("Numar: ")
        if number == "x":
            break
        try:
            number = float(number)
            numbers.append(number)
        except ValueError:
            print("Nu ati introdus un numar valid.")
    
    return numbers

def main():
    nmbers = get_input_numbers()

    menuOption = 0
    while menuOption != "4":
        print("Meniu:")
        print("1. Media numerelor")
        print("2. Suma numerelor")
        print("3. Puterea numerelor din lista de numere")
        print("4. Iesire")
        menuOption = input("Optiune: ")

        match menuOption:
            case "1":
                print(medie(nmbers))
            case "2":
                print(suma(nmbers))
            case "3":
                print(putere(nmbers))
            case "4":
                break
            case _:
                print("Optiune invalida")


if __name__ == "__main__":
    main()
