

def get_fib_numbers(qty):
    # Вставьте свой код здесь.
    fib_first= 0
    fib_second = 1
    fib_list = [0]
    for i in range(1, qty):
        fid_gen = fib_first + fib_second
        fib_list.append(fid_gen)
        fib_first = fib_list[i - 1]
        fib_second = fib_list[i]
    return fib_list


fib_numbers = get_fib_numbers(10)
assert len(fib_numbers) == 10
print(fib_numbers)

