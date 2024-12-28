def indc(n,num):
    if (n<1 or n>num):
        return
    print(n)
    indc(n-1,num)
    print(n)
n=int(input(" Enter a number "))
indc(n,n)