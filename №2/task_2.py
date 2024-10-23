def tuple_stats(tpl):
    if not tpl:
        return (0, 0, ())

    total_sum = sum(tpl)
    avg_value = total_sum / len(tpl)
    unique_elements = tuple(set(tpl))

    return (total_sum, avg_value, unique_elements)

try:
    user_input = input("Введите числа, разделенные запятыми: ")
    numbers_tuple = tuple(float(x) for x in user_input.split(","))
    result = tuple_stats(numbers_tuple)
    print(result)
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
