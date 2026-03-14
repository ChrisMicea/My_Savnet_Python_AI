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
    num = input(f"Introduceti un numar intre 1 si 49 (numarul {len(chosenNums) + 1} / 6): ")
    if not num.isdigit():
        print("Numar invalid")
        continue
    if int(num) in chosenNums:
        print("Numar deja introdus")
        continue
    if int(num) < 1 or int(num) > 49:
        print("Numar in afara intervalului 1-49")
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
