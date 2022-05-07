a, b, n = [int(i) for i in input().split()]
while(a + b + n != 0):
    n = n % 5
    if(n == 0):
        print(a)
    elif(n == 1):
        print(b)
    elif(n == 2):
        print(int((b + 1) / a))
    elif(n == 3):
        print(int((a + b + 1) / (a * b)))
    else:
        print(int((a + 1) / b))
    a, b, n = [int(i) for i in input().split()]