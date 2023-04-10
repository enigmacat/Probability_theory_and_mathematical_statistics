
# =====================================================================
# В первом ящике находится 8 мячей, из которых 5 - белые.
# Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4.
# Какова вероятность того, что 3 мяча белые?
# ===========================================================================

from math import comb



# вероятность, что из первого ящика 0, а из второго 3
p0_3 = (comb(5, 0)*comb(3, 2)/comb(8, 2)) * (comb(5, 3)*comb(7, 1)/comb(12, 4))
# вероятность, что из первого ящика 1, а из второго 3
p1_2 = (comb(5, 1)*comb(3, 1)/comb(8, 2)) * (comb(5, 2)*comb(7, 1)/comb(12, 4))
# вероятность, что из первого ящика 0 или 1 белый мяч, а из второго 3
p1 = p0_3 + p1_2


# вероятность, что первый ящик может содержать белый мяч под номером 1, а второй ящик - белые 2 и 3
p2_1 = (comb(5, 1)*comb(3, 1)/comb(8, 2)) * (comb(5, 2)*comb(7, 2)/comb(12, 4))
# вероятность, что первый ящик может содержать белый мяч под номером 2, а второй ящик - белые 1 и 2
p2_2 = (comb(5, 2)*comb(3, 0)/comb(8, 2)) * (comb(5, 2)*comb(7, 2)/comb(12, 4))
p2_3 = 0  # из первого ящика 2 белых мяча, а из второго - 2
          # Это может произойти единственным способом: первый ящик содержит белые 1 и 2, а второй ящик - белые 1 и 2.
          # Вероятность этого события равна 0, так как в первом ящике всего 2 мяча, а нужно выбрать 3.

# вероятность, что из первого ящика достали 1 или 2 белых мяча, а из второго 2
p2 = p2_1 + p2_2 + p2_3

# вероятность, что из первого ящика достали 2, а из второго - 1
   # Первый множитель вычисляет вероятность, что из первого ящика достали 2 белых и 0 черных.
   # Второй множитель вычисляет вероятность, что из второго ящика достали 1 белый и 3 черных.
p3 = (comb(5, 2)*comb(3, 0)/comb(8, 2)) * (comb(5, 1)*comb(7, 3)/comb(12, 4))

# общая вероятность, что будет 3 белых мяча
p = p1 + p2 + p3

# рез-т с округлением до 2 знаков после запятой
print(f"\nВероятность, что 3 мяча белые: {round(p, 2)}")
