def fibonacci(n):
    valores = []
    a, b = 0, 1  
    for _ in range(n):  
        if a < 2:
            valores.append(a)
        else:
            prime = True
            for i in range(2, int(a**0.5) + 1):
                if a% i == 0:
                    prime = False
                    break
            if prime:
                valores.append(a)
        a, b= b,a+b
    return print(valores)
    
fibonacci(99)