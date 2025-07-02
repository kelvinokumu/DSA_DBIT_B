def find_min(lst):
    if len(lst) == 0:
        return None

    min_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
    return min_value
