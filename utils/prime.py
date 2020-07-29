def prime(limit_inf, limit_sup):
    prime_list = []
    for i in range(limit_inf, limit_sup):
        for j in range(2, i // 2):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list
