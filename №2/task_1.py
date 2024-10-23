def analyze_list(lst):
    if not lst:
        return {'max': None, 'min': None, 'avg': None, 'med': None}

    max_value = max(lst)
    min_value = min(lst)
    avg_value = sum(lst) / len(lst)

    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    med_value = (sorted_lst[n // 2] if n % 2 != 0 else 
                 (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2)

    return {'max': max_value, 'min': min_value, 'avg': avg_value, 'med': med_value}

try:
    user_input = input("Введите числа, разделенные запятыми: ")
    numbers = [float(x) for x in user_input.split(",")]
    result = analyze_list(numbers)
    print(result)
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
