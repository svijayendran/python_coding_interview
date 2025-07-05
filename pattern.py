n = 5

for i in range(0, n+1):
    for j in range(i):
        print("*", end="")
    print("")

print("")
for i in range(0, n):
    for i in range(0, n+1):
        print("*", end="")
    print("")

print("")

for i in range(n, 0, -1 ):
    for j in range(i):
        print("*", end="")
    print("")
    
for i in range(0,n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n, 0, -1):
    print(' ' *(n - i) + "*" * (2 * i -1) )
            
