import math

def main():
    l = []
    a = 0
   #b = 2
    for i in range (1,8):
        a = a + i 
       # b += 1
        for x in range(1, a+1):
            if a % x == 0:
                l.append(a)
               # print l
                
                if len(l) > 5:
                    print l
                    break
                else:
                    l=[]
                    continue
    print l
                
if __name__ == '__main__':
    main()
