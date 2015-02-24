def main():
    l=[]
    for a in xrange(1000000):
        a=str(a)
        if a==a[::-1]:
            b=bin(int(a))
            b1=b[::-1]
            if b[2:]==b1[:-2]:l.append(int(a))
    print sum(l)


if __name__=='__main__':
    main()
