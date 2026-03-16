def get_input_ages() -> list:
    n = 0
    while not n:
        n = input("Cati participanti avem la sondaj? ")
        try:
            n = int(n)
        except ValueError:
            print("Numarul de participanti trebuie sa fie un numar intreg.")
            n = 0
    
    # could have been done with a counter instead of len(ages)
    ages = []
    while len(ages) < n:
        age = input(f"Introduceti varsta participantului {len(ages) + 1}: ")
        try:
            age = int(age)

            if age < 0 or age > 150:
                print(f"Varsta trebuie sa fie intre 0 si 150 ani.")
                continue
            
            ages.append(age)
        except ValueError:
            print(f"Nu ati introdus un format valid la participantul {len(ages) + 1}")
    
    return ages

def get_avg_ages(ages: list) -> float:
    return sum(ages) / len(ages)

if __name__ == "__main__":
    ages = get_input_ages()
    if ages:
        avg_age = get_avg_ages(ages)
        print(f"Media varstelor este: {avg_age}")
