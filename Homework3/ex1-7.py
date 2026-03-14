lista = input("Introduceti lista de taskuri: ")
# can also be done with regex
lista_taskuri = lista.replace(",", " ").split() # replace commas with space, then split on whitespaces (if sep is empty)
print(lista_taskuri)

for task in lista_taskuri:
    if lista_taskuri.count(task) > 1:
        lista_taskuri.remove(task)
print(lista_taskuri)