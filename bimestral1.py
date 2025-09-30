ln = []
for i in range(5):
    ln.append(input("nome:"))
print(ln)
na = 0
for i in ln:
    if i[0] != "a" and i[0] != "A":
        print(i)
        na += 1
print(f"{na} nomes não começam com a letra a")