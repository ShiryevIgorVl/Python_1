# Война и мир
from typing import Any

wap_file_name = "war_and_peace_UTF-8.txt"

wap_processed_file_name = "wap_processed_file_name.txt"

statistics_dictionary = {}


# Читаем файл war_and_peace.txt и возвращаем список char
def read_txt_file_to_list(file_name):
    file = open(file_name, "r", encoding="utf-8", errors="replace")
    wap_list = list(file.read())
    file.close()
    return wap_list


# Удаляем разные символы из списка и преобразум список в строку
# def removing_unreadable_characters(list_for_removing_spaces):
#     my_list = []
#     for i in range(len(list_for_removing_spaces) - 1):
#         if (list_for_removing_spaces[i] != " ") and (list_for_removing_spaces[i] != "\xa0") and (
#                 list_for_removing_spaces[i] != "\n") and (list_for_removing_spaces[i] != "/") and (list_for_removing_spaces[i] != "\t"):
#             my_list.append(list_for_removing_spaces[i])
#
#     # string = "".join(map(str, my_list))
#     return my_list

# Удаляем разные символы из списка и преобразум список в строку
def removing_unreadable_characters(list_for_removing_spaces):
    my_list = []
    for i in range(len(list_for_removing_spaces) - 1):
        if (list_for_removing_spaces[i] != " ") and (list_for_removing_spaces[i] != "\xa0") and (
                list_for_removing_spaces[i] != "\n") and (list_for_removing_spaces[i] != "/") and (
                list_for_removing_spaces[i] != "\t"):
            my_list.append(list_for_removing_spaces[i])

    # string = "".join(map(str, my_list))
    return my_list


# Записываем новый файл.txt для логирования
def write_file(file_name, sting_for_write):
    file = open(file_name, "w", encoding="utf-8")
    file.write(sting_for_write)
    file.close()


# Вставляем пробел после завершения предложения
def insert_space_after_dot(input_list):
    for i in range(len(input_list) - 1):
        if (input_list[i] == ".") or (input_list[i] == "!") or (input_list[i] == "?") or (input_list[i] == "."):
            input_list.insert(i + 1, " ")
    string = "".join(map(str, input_list))
    return string


# Делим String в List по предложениям, разделитеь пробел
def devision_to_parts(string_for_devision) -> list | Any:
    list_output = string_for_devision.split(" ")
    return list_output


def filling_dictionary_abc_chars(dictionary) -> dict | Any:
    for i in range(ord('а'), ord('я') + 1):
        dictionary[chr(i)] = ""
    return dictionary


def statistics_char(list_char, input_char) -> int | Any:
    """
    :type input_char: str
    :type list_char: list
    """
    count = 0

    for j in range(0, len(list_char) - 1):
        if list_char[j] == input_char:
            count += 1
    return count


filling_dictionary_abc_chars(statistics_dictionary)

war_and_peace_list = read_txt_file_to_list(wap_file_name)

list_for_write_file = removing_unreadable_characters(war_and_peace_list)
counter_char = statistics_char(list_for_write_file, 'а')

# string_for_write_file = insert_space_after_dot(list_for_write_file)
# list_devision = devision_to_parts(string_for_write_file)
# write_file(wap_processed_file_name, string_for_write_file)

print("Счетчик Я", counter_char)
