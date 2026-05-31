n = int(input())
c = 0

for i in range(n):
    ip = input()
    c+= 4 if ip == "Tetrahedron" else 6 if ip == 'Cube' else 12 if ip == 'Dodecahedron' else 8 if ip == 'Octahedron' else 20

print(c)