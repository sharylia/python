def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

try:
    set1_input = input("Введите элементы первого множества, разделенные запятыми: ")
    set2_input = input("Введите элементы второго множества, разделенные запятыми: ")

    set1 = {x.strip() for x in set1_input.split(",")}
    set2 = {x.strip() for x in set2_input.split(",")}

    result = symmetric_difference(set1, set2)

    if result:
        print("Симметрическая разность:", result)
    else:
        print("Симметрическая разность пустая (все элементы совпадают).")
except Exception as e:
    print("Ошибка:", e)
