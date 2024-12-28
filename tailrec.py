def tailrec(n,num):
    if n>num:
        return
    print(n)
    tailrec(n+1,num)
n=int(input(" Enter n to print n to 1"))
tailrec(1,n)