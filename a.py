gold, years, sons, daughters = map(int, input().split())

for i in range(1, years+1):
    if gold>=85:
        gold *= 0.075

x_factor = sons*2+daughters
son_g = (gold*2/x_factor) if sons != 0 else 0
daughter_g = (gold/x_factor) if daughters != 0 else 0

print(f"{son_g:.10f} {daughter_g:.10f}")