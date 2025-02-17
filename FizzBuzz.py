# num_max = int(input("Введите максимальное число: \n"))
def input_num() -> int:
    while True:
        num_max = input("Введите максимальное число которое должно быть больше 1:\n")
        try:
            int_max = int(num_max)
            if int_max >= 1:
                print("Максимальное число должно быть не меньше 1")
                break
            else:
                continue
        except Exception:
            print("Введенной число не является целым или числом")
            print(type(num_max))

    return int_max


def fizz_buzz(max_number):
    min_number = 1
    for i in range(min_number, max_number + 1):
        if i == max_number:
            print(max_number)
        elif i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)


int_max = input_num()
fizz_buzz(int_max)

