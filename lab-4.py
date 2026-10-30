# Лабораторная работа №4
# Вариант 3
# Хранилище 2x4, требование - антидот (d), стартовые очки выживания 10
# Алгоритм решения - полный перебор
import itertools

# Стартовый набор предметов (без антидота - он обязателен и ставится отдельно)
items = [
    ("r", "Винтовка", 3, 25),
    ("p", "Пистолет", 2, 15),
    ("a", "Боекомплект", 2, 15),
    ("m", "Аптечка", 2, 20),
    ("i", "Ингалятор", 1, 5),
    ("k", "Нож", 1, 15),
    ("x", "Топор", 3, 20),
    ("t", "Оберег", 1, 25),
    ("f", "Фляжка", 1, 15),
    ("s", "Еда", 2, 20),
    ("c", "Арбалет", 2, 20),
]

capacity = 2 * 4 - 1       # хранилище 2x4, минус 1 ячейка под антидот
start_points = 10 + 10     # очки по варианту + бонус за обязательный антидот
total_value = sum(value for _, _, _, value in items)

# Полный перебор всех комбинаций предметов
best_value = -1
best_combo = ()
for count in range(len(items) + 1):
    for combo in itertools.combinations(items, count):
        weight = sum(size for _, _, size, _ in combo)
        if weight <= capacity:
            value = sum(value for _, _, _, value in combo)
            if value > best_value:
                best_value = value
                best_combo = combo

left_value = total_value - best_value
survival_points = start_points + best_value - left_value

# Вывод результата в виде заполненных ячеек хранилища
cells = ["d"]
for code, name, size, value in best_combo:
    cells.extend([code] * size)

print("Решение задачи о рюкзаке (вариант 3, хранилище 2x4):")
print()
for row_start in range(0, len(cells), 4):
    row = cells[row_start:row_start + 4]
    print(", ".join(f"[{c}]" for c in row))

print()
print("Выбранные предметы:")
for code, name, size, value in best_combo:
    print(f"  [{code}] {name} - размер {size}, ценность {value}")
print(f"  [d] Антидот (обязателен) - размер 1, ценность не учитывается (бонус +10)")

print()
print(f"Занято ячеек: {len(cells)} из {2 * 4}")
print(f"Суммарная ценность взятых предметов: {best_value}")
print(f"Суммарная ценность оставленных предметов: {left_value}")
print(f"Итоговые очки выживания: {survival_points}")
