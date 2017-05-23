def fib(n):
    if not isinstance(n, int) or n < 0:
        print("not a damn")
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input("number of terms in fibonacci sequence?\n"));
for i in range(n):
    print(fib(i))
    
