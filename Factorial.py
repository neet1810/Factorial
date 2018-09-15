def factorial(n):
    if n > 1:
        factor = n * factorial(n-1)
    else:
        return 1
    return factor

def validateNum():
    while True:
        var = input("Please enter a number: ")
        try:
            var = int(var)
            break
        except:
            None
    return var

num = validateNum()
print(factorial(num))

