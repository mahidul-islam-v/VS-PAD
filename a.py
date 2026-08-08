gold, years, sons, daughters = map(int, input().split())

gold = gold*(0.975**years)

x_factor = sons*2+daughters

son_g = (gold*2/x_factor) if sons != 0 else 0
daughter_g = (gold/x_factor) if daughters != 0 else 0

print(f"{son_g:.10f} {daughter_g:.10f}")