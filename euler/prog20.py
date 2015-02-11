from math import factorial
def main():
    x=int(raw_input("enter the fact no.::"))
    x1=factorial(x)
    #print x1
    x2=map(int, str(x1))
    #print x2
    #x3=list(map(sum,x2))
    #x4=sum(x3)
    #print x4
    x3=sum(x2)
    print x3
    
if __name__ == '__main__':
    main()
