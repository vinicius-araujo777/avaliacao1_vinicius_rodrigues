ln = []
for i in range(10):
    ln.append(int(input("numero:")))
sp = 0
si = 0
for i in ln:
    if i %2 == 0:
        sp += i
    else:
        si += i

print(sp, "soma par")
print(si,"soma impar")