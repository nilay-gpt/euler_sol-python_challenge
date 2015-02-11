from math import factorial

def main():
    a=int(raw_input("enter the grid right side size::"))
    b=int(raw_input("enter the grid left side size::"))
    c0=(a+b)
    c=factorial(c0)
    c1=factorial(a)
    c2=factorial(b)
    c3=(c1*c2)
    print c/c3
    

if __name__ == '__main__':
    main()
