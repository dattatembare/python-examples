name = "DATTA"
print(list(name))
# ['D', 'A', 'T', 'T', 'A']
print([name[i] for i in range(len(name)-1, -1, -1)])
# ['A', 'T', 'T', 'A', 'D']
print("".join([name[i] for i in range(len(name)-1, -1, -1)]))
# ATTAD
name = list(name)
name.reverse()
print("".join((name)))

