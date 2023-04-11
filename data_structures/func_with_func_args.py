def is_odd(num):
    if num % 2:
        return True
    else:
        return False

def change_list(seq, func):
    odd_list = []

    for i in seq:
        if func(i):
            odd_list.append(i)
    return odd_list

seq_list = range(1, 21)
print(change_list(seq_list, is_odd))
