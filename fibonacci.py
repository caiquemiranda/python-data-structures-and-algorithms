#
# 
# 
def fibonacci(n):
    n1 = 1
    n2 = 1
    for i in range(n-1):
        total = n1 + n2
        n2 = n1
        n1 = total
    
    return n2


f = fibonacci(5)
print(f)