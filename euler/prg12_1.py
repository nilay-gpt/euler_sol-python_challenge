import math

def main():
    l = []
    a=0
    for i in xrange(1,1000000000):
        a+=i
        l=[]
        for j in xrange(1,a):
            
           
            if a%j==0:
                l.append(j)
                if(len(l)==499):
                    print a
                    return
            
                    
                   
                
if __name__ == '__main__':
    main()
