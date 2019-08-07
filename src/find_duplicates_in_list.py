# Find duplicates in list without using libraries.
a = [1, 5, 7, 6, 8, 8, 9, 6, 7, 4]
seen = {}
dupes = []

for x in a:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1

print(dupes)
