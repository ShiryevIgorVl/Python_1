import math


def input_num_1() -> float:
    while True:
        num = input("Введите 1 сторону треугольника: ")
        try:
            fl_num = float(num)
            break
        except Exception:
            print("Введенной число не является числом")
    return fl_num

def input_num_2() -> float:
    while True:
        num = input("Введите 2 сторону треугольника: ")
        try:
            fl_num = float(num)
            break
        except Exception:
            print("Введенной число не является числом")
    return fl_num

def input_num_3() -> float:
    while True:
        num = input("Введите 3 сторону треугольника: ")
        try:
            fl_num = float(num)
            break
        except Exception:
            print("Введенной число не является числом")
    return fl_num

# Проверяем существование треугольника с заданными сторонами
def checking_existence_triangle(side_1, side_2, side_3) -> bool | None:
    if (side_1 + side_2 > side_3) and (side_2 + side_3 > side_1) and (side_1 + side_3 > side_2):
        return True

# Считаем угол треугольника напротив стороны side_1 в градусах
def corner_solution_alfa(side_1, side_2, side_3) -> float:
    cos_alfa = (side_2**2 + side_3**2 - side_1**2) / (2 * side_2 * side_3)
    alfa_rad = math.acos(cos_alfa)
    alfa = (180 / math.pi) * alfa_rad
    return alfa

# Считаем угол треугольника напротив стороны side_2 в градусах
def corner_solution_beta(side_1, side_2, side_3) -> float:
    cos_beta = (side_1**2 + side_3**2 - side_2**2) / (2 * side_1 * side_3)
    beta_rad = math.acos(cos_beta)
    beta = (180 / math.pi) * beta_rad
    return beta

# Считаем угол треугольника напротив стороны side_3 в градусах
def corner_solution_gamma(side_1, side_2, side_3) -> float:
    cos_gamma = (side_1**2 + side_2**2 - side_3**2) / (2*side_1*side_2)
    gamma_rad = (math.acos(cos_gamma))
    gamma = (180 / math.pi) * gamma_rad
    return gamma

# Вычисляем периметр треугольника
def perimeter_solution(side_1, side_2, side_3) -> float:
    return side_1 + side_2 + side_3

# Вычисляем площадь треугольника
def area_triangle (side_1, side_2, side_3) -> float:
    semi_perimert = perimeter_solution(side_1, side_2, side_3) / 2   #полупериметр
    aria  = math.sqrt(semi_perimert * (semi_perimert - side_1) * (semi_perimert - side_2) * (semi_perimert - side_3))
    return aria

# Выводим результаты в консоль
def print_triangle(alfa, beta, gamma, perimeter, aria):
    print("угол alfa :", "{:.0f}".format(alfa))
    print("угол beta: ", "{:.0f}".format(beta))
    print("угол gamma: ", "{:.0f}".format(gamma))
    print("периметр: ", "{:.3f}".format(perimeter))
    print("площадь: ", "{:.3f}".format(aria))

# Получаем длинны сторон треугольника из консоли. Проверяем на существование треугольника.
# Если все хорошо, все считаем и выводим. Если плохо запрашиваем новые значения длин сторон.
def all_solution():
    while True:
        side_1 = input_num_1()
        side_2 = input_num_2()
        side_3 = input_num_3()
        if checking_existence_triangle(side_1, side_2, side_3):
            aria = area_triangle(side_1, side_2, side_3)
            perimeter = perimeter_solution(side_1, side_2, side_3)
            alfa = corner_solution_alfa(side_1, side_2, side_3)
            beta = corner_solution_beta(side_1, side_2, side_3)
            gamma = corner_solution_gamma(side_1, side_2, side_3)
            print_triangle(alfa, beta, gamma, perimeter, aria)
            break
        else:
            print("Такого треугольника быть не может")

all_solution()


