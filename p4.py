def calculate_expression(n):
    nn = int(str(n) * 2) 
    nnn = int(str(n) * 3)  
    result = n + nn + nnn
    return result

n = 5

result = calculate_expression(n)

print("Результат виразу {} + {} + {} = {}".format(n, n * 11, n * 111, result))
