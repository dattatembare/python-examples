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

print(dupes)  # [8, 6, 7]


def find_duplicates(in_list):
    num_count = {}
    for num in in_list:
        num_count[num] = num_count.get(num, 0) + 1

    return {k: v for k, v in num_count.items() if v > 1}


print(find_duplicates(a))  # {7: 2, 6: 2, 8: 2}
