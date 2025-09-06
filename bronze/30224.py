A = []
while True:
    name, age, weight = input().split()
    if name == "#":
        break

    if int(age) > 17 or int(weight) >= 80:
        A.append(f"{name} Senior")
    else:
        A.append(f"{name} Junior")

print(*A, sep="\n")