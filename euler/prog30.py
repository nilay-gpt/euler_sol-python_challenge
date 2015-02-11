def main():
    l,gt=[],0
    for i in range(2,1000000):
        total=0
        for j in str(i):total +=int(j)**5            
        if total == i:l.append(i)          
    for i in l:gt +=i  
    print l,gt
if __name__ == '__main__':
    main()
