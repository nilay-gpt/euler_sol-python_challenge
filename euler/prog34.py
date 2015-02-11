from math import factorial
def main():
    l,gt=[],0
    for i in range(3,1000000):
        total=0
        for j in str(i):
            k1=int(j)
            total +=factorial(k1)
            if total == i: l.append(i)       
    for i in l:gt +=i  
    print gt
if __name__ == '__main__':
    main()
