def str_find(sequence, subs):  # -1, если не нашёл индекс начала подстроки
    for i in range(len(sequence) - len(subs) + 1):
        for k in range(len(subs)):
            if subs[k] != sequence[k+i]:
                break
        else:
            return i
    return -1