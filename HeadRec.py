def headrec(n,num):
    if n>num:
        return
    headrec(n+1,num)
    print(n)
n=int(input(" Enter n to print n to 1"))
headrec(1,n)