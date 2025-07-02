def find_max(lst):
    if len(lst) == 0:
        return None

    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    return max_value
