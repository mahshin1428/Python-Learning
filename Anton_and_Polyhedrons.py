n = int(input())

total = 0
for _ in range(0, n):
    s = input("")

    if s == 'Tetrahedron':
        total += 4
    if s == 'Cube':
        total += 6
    if s == 'Octahedron':
        total += 8
    if s == 'Dodecahedron':
        total += 12
    if s == 'Icosahedron':
        total += 20

print(total)
