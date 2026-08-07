n = int(input())

for _ in range(n):
    ln = int(input())
    s = list(str(input()))
    ns = f"{s[0]}"

    cur_del = "2"
    possible = True

    for i in range(1,len(s)-1):
        sl = ns[len(ns)-1]
        sc = s[i]
        if sl != sc:
            ns+= sc
        else:
            if sc == cur_del:
                possible = False
                break
            else:
                cur_del = sc

    ns+= f"{s[len(s)-1]}"

            
    print(ns if possible else -1)

