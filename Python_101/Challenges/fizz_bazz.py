 # Reto #0: EL FAMOSO "FIZZ BUZZ" son operaciones matematicas basicas, donde operamos con el modulo o resto '%'


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)