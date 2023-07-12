
def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


lista_numeros = [10, 5, 8, 15, 3]
resultado = find_max(lista_numeros)
print("El número máximo es:", resultado)
