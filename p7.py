def print_even_numbers(n, m):
    for i in range(-n, n + 1, m):
        if i % 2 == 0:
            print(i)


m = 42  
n = 10  

print("Усі парні числа від -{} до {} з кроком {}: ".format(n, n, m))
print_even_numbers(n, m)
