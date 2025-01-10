def convert_str_to_int(arr_str):
    arr_int = []
    for s in arr_str:
        arr_int.append(int(s))
    return arr_int
def print_arr_perline(arr_int):
    for value in arr_int:
        print(value)
def get_even_digits(arr_int):
    arr_int_even = []
    for value in arr_int:
        if value % 2 == 0:
            arr_int_even.append(value)
    return arr_int_even
def negative_digits(arr_int):
    arr_int_negative = []
    for x in arr_int:
        if x < 0:
            arr_int_negative.append(x)
    return arr_int_negative
def prime_digits(arr_int):
    arr_int_prime = []
    for a in arr_int:
        if a <= 1:
            continue
        count = 0
        for i in range(1, a+1):
            if a%i == 0:
                count += 1
        if count == 2:
            arr_int_prime.append(a)
    return arr_int_prime

