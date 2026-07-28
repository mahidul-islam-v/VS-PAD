n = int(input())
register = {}


for i in range(n):
    s = input()
    register[s] = 0 if s not in register else register[s]+1
    
    print('OK' if register[s] == 0 else f'{s}{register[s]}')