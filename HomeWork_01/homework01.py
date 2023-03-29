#=============================================================================
# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# - Найти вероятность того, что все карты – крести.
# - Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
#===========================================================================

# функция для вычисления факториала
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# функция для вычисления сочетаний
def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# вычисление числа комбинаций из 13 карт крестей
combinations_of_suits = combinations(13, 4)

# вычисление числа возможных комбинаций из 52 карт
total_combinations = combinations(52, 4)

# вычисление вероятности того, что все карты будут крести
probability = combinations_of_suits / total_combinations

print("Вероятность того, что все карты будут крести, равна:\n",
      probability, "или ~", round(probability*100, 2), "%\n")

# вычисление общего числа возможных комбинаций из 4 карт
total_combinations = combinations(52, 4)

# вычисление числа комбинаций без тузов
combinations_without_aces = combinations(48, 4)

# вычисление числа комбинаций с хотя бы одним тузом
combinations_with_aces = total_combinations - combinations_without_aces

# вычисление вероятности того, что среди 4-х карт будет хотя бы один туз
probability = combinations_with_aces / total_combinations

print("Вероятность того, что среди 4-х карт окажется хотя бы один туз, равна:\n",
      probability, "или ~", round(probability*100, 2), "%\n")