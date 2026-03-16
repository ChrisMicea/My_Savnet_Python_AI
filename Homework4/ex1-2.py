import math

def check_power_of_number(num: int) -> int:
    try:
        num = int(num)
    except ValueError:
        print(f"type of num is {type(num)}")
        print("invalid parameter: input needs to be an integer")
        return 0

    if num < 2:
        print("invalid parameter: input needs to be an integer >= 2")
        return 0

    # upper bound is sqrt() + 1 because range is not inclusive of upper bound and we can
    # get perfect squares as input
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            ncpy = num
            power = 0
            while ncpy % i == 0:
                ncpy //= i
                power += 1
            if ncpy == 1:
                return power
    return 0

def main():
    while True:
        num = input("Enter a number (q to exit): ")
        if num == "q":
            break
        # try:
        #     num = int(num)
        # except ValueError:
        #     print("Invalid input")
        #     continue
        print(check_power_of_number(num))

if __name__ == "__main__":
    main()