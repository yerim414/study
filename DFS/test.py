n, m = map(int, input().split())

light = [0]
light.extend(list(map(int, input().split())))

for _ in range(m):
    a, b, c = map(int, input().split())

    match (a):
        case 1:
            light[b] = c
        case 2:
            light[b:c+1] = [x ^ 1 for x in light[b:c+1]]
        case 3:
            light[b:c+1] = [0] * (c - b + 1)
        case 4:
            light[b:c+1] = [1] * (c - b + 1)

print(*light[1:])