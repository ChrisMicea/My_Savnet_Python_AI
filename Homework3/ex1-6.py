word = input("Introduceti un cuvant (fara majuscule): ")
word = word.lower()

firstLetter = word[0]
cnt = 0
for letter in word:
    if letter == firstLetter:
        cnt += 1

print(cnt)

# or
print(word.count(word[0]))
