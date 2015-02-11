counts = {}
def main(n):
    c = 1
    start = n
    while n!=1:
        if n in counts: 
            c += counts[n]
            break
        if n%2==0: 
            n/=2
        else: 
            n = 3*n+1
        c += 1

    counts[start] = c
    return c

ans = max(((main(i),i) for i in range(1,1000000)))
print("The starting position generating the longest sequence is:->"+format(ans[1]))

