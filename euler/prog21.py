def main():
    l,k,k1=[],[],[]
    for a in range(1,10000):
        for i in range(1,a):
            if (a%i==0):
                l.append(i)
        l1=sum(l)
        for j in range(1,l1):
          if (l1%j==0):
              k.append(j)
        l2=sum(k)
        if (a==l2 and a!=l1 ):
            k1.append(a),k1.append(l1)
        else:
            l,k=[],[]
    print sum(set(k1))
if __name__ == '__main__':
    main()
