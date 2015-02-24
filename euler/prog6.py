a=range(1,101)
b=sum(range(1,101))
print b*b - sum(i*i for i in a)
