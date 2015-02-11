def main():
    l=[]
    for i in range(1,1001):
        c=pow(i,i)        
        l.append(c)
    print str(sum(l))[-10:]

if  __name__=="__main__":
    main()  
