CNP = input("Introduceti primele 7 cifre ale CNP-ului: ")
if CNP.isdigit() and len(CNP) == 7:
    if int(CNP[1:2]) < 6 or int(CNP[1:2]) > 26:
        print("Aveti peste 18 ani")
    else:
        print("Aveti sub 18 ani")
else:
    print("CNP-ul nu este valid")
