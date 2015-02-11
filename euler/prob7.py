
def main():
    l=[]
#    for num in range(1,15):
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#            else:
#                n1=num
#        l.append(n1)
#    print n range(1,101):
    j=0
    for num in xrange(2,200000):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            j+=1
            l.append(num)
            print j
    print "----------->",l[10000]


if __name__ == '__main__':
        main()
