# ===================================================================
# На соревновании по биатлону один из трех спортсменов стреляет
# и попадает в мишень.
# Вероятность попадания для первого спортсмена равна 0.9,
# для второго — 0.8, для третьего — 0.6.
# Найти вероятность того, что выстрел произведен: a). первым спортсменом
# б). вторым спортсменом в). третьим спортсменом.
# ==========================================================================

# вероятности попадания для каждого спортсмена
p1 = 0.9
p2 = 0.8
p3 = 0.6

# вероятность выбора каждого спортсмена
p_total = 1/3

# вероятность попадания в мишень
p_hit = p1*p_total + p2*p_total + p3*p_total

# вероятность попадания для первого спортсмена
p1_given_hit = p1*p_total / p_hit

# вероятность попадания для второго спортсмена
p2_given_hit = p2*p_total / p_hit

# вероятность попадания для третьего спортсмена
p3_given_hit = p3*p_total / p_hit

# вывод результатов
print("1-й стрелок: {:.2f}".format(p1_given_hit))
print("2-й стрелок: {:.2f}".format(p2_given_hit))
print("3-й стрелок: {:.2f}".format(p3_given_hit))