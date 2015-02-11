def main():
    maximum ,number= 0,0
    #number = 0
    for n in xrange(2,1001):
        k = 0
        while True:
            k+=1
            m = 10**k -1
            if m%n == 0:
                if k > maximum:
                    maximum = k
                    number = n
                break
            elif (10*k)%n == 0: break
    print number
if __name__ == '__main__':
    main()
    
