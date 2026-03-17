def compute(n) :
    s1 = n + 10*n
    s2 = n + 10*n + 100*n
    s3 = n + 10*n + 100*n + 1000*n
    s = n + s1 + s2 + s3
    print(s)

n = int(input("Enter a digit : "))
compute(n)
