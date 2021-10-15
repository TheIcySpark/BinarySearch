class Solution:
    def solve(self, n):
        next_value = compute_next(str(n))
        prev_value = compute_prev(str(n))
        if abs(next_value - n) == abs(prev_value - n):
            return next_value
        else:
            return next_value if abs(next_value - n) < abs(prev_value - n) else prev_value

def compute_next(n):
    if all_digits_odd(n):
        n = str(int(n) - 1)
    i = 0
    n = list(n)
    while i < len(n):
        if int(n[i]) % 2 == 0:
            new_value = int(n[i]) + 1
            n[i] = str(new_value)
            break
        i += 1
    i += 1
    while i < len(n):
        n[i] = '1'
        i += 1
    return int("".join(n))


def compute_prev(n):
    if all_digits_odd(n):
        n = str(int(n) - 1)
    i = 0
    while i < len(n):
        if int(n[i]) % 2 == 0:
            if int(n[i])  == 0:
                n = str(int(n) - int(n[i:]) - 1)
                i = 0
                continue
            else:
                n = list(n)
                new_value = int(n[i]) - 1
                n[i] = str(new_value)
                break
        i += 1
    i += 1
    while i < len(n):
        n[i] = '9'
        i += 1
    return int("".join(n))


def all_digits_odd(n):
    for i in n:
        if int(i) % 2 != 0:
            return False
    return True
