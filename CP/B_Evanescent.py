import re 

n = int(input())

for i in range(n):
    sl = int(input())
    s = input()

    if len(s) == 3:
        print(1 if s[0]==s[2] else 2)
    else:

        count = None

        for j in range(1,sl-1):
            s_list = [*s]
            s_list.pop(j)
            cur_count = 1

            for k in range(sl-2): 
                if s_list[k] != s_list[k+1]: cur_count+= 1

            count = min(count, cur_count) if j!=1 else cur_count

        print(count)
