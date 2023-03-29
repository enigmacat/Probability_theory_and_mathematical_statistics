#======================================================
# В лотерее 100 билетов. Из них 2 выигрышных.
# - Какова вероятность того, что 2 приобретенных билета
# окажутся выигрышными?
#=======================================================

num_tickets = 100
num_win_tickets = 2

# вероятность приобретения первого выигрышного билета
p_first_win_ticket = num_win_tickets / num_tickets

# вероятность приобретения второго выигрышного билета после приобретения первого
p_second_win_ticket = (num_win_tickets - 1) / (num_tickets - 1)

# общая вероятность того, что два приобретенных билета окажутся выигрышными
p_both_win_tickets = p_first_win_ticket * p_second_win_ticket

print("Вероятность получить два выигрышных билета:",
      p_both_win_tickets,  "или ~", round(p_both_win_tickets*100, 2), "%\n")