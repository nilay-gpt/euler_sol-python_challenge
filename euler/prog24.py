import itertools
def main():
    a='0123456789'
    print ["".join(x) for x in itertools.permutations(a)][999999]
if __name__ == '__main__':
    main()
