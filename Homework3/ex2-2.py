winningNums = [4,12,31,17,22,25]
winnings = {
    0: 0,
    1: 0,
    2: 50,
    3: 500,
    4: 500,
    5: 1000,
    6: 5000
}
chosenNums = []

while len(chosenNums) < 6:
    num = input("Introduceti un numar: ")
    if not num.isdigit():
        print("Numar invalid")
        continue
    chosenNums.append(int(num))

matches = 0
matchedNums = []
for num in chosenNums:
    if num in winningNums:
        matches += 1
        matchedNums.append(num)

print(f"Numerele castigatoare sunt: {winningNums}")
print(f"Numerele alese sunt: {chosenNums}")
print(f"Numerele ghicite sunt: {matchedNums}")
print(f"Suma castigata este: {winnings.get(matches, 0)}")
