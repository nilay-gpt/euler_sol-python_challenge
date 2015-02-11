def main():
    a,b,c,count=-1,1,0,0
    while True:
        c=a+b
        a,b,count=b,c,count+1
        if(len(map(int,str(c)))>=1000):break       
    print count-1
if __name__ == '__main__':
    main()
