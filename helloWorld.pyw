import PySimpleGUI as sg

import random

def last_dig(item):
    return item % 10

array_size = 10

def sort_array():
    my_array = [random.randint(10, 100) for i in range(array_size)]
    my_array.sort(key = last_dig)
    return (my_array)

layout = [
    [sg.Button('Генерация и сортировка', enable_events=True, key='-FUNCTION-', font='Times 12 bold')],
    [sg.Text('Результат:', size=(50, 1), font='Arial 12')],
    [sg.Text(size=(250, 1), key='-text-', font='Helvetica 10')]
]
window = sg.Window('Сортировка массива 10х1 по последней цифре', layout, size=(750, 350))
while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
    if event == '-FUNCTION-':
        data = ", ".join(map(str, sort_array()))
        set_text = window['-text-']
        set_text.update(data)
     #   print(data)
#    print(round(0.1+0.1+0.1, 2))

# закрываем окно и освобождаем используемые ресурсы
window.close()

