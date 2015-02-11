def main():
    L,limit=set(),101
    for i in range(2,limit):
        for j in range(2,limit):
            L.add(pow(i,j))
    print len(L)
if __name__ == '__main__':
    main()
