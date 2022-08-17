n = int(input())
if n % 2!=0:
    print(list(i for i in range(n,n**2 + 1,2)))
else:
    print(list(i for i in range(n +1,n**2 + 1,2)))