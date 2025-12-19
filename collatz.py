from typing import List


def syracuse_sequence(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("N должно быть положительным целым числом")
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def syracuse_max(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("N должно быть положительным целым числом")
    max_val = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n > max_val:
            max_val = n
    return max_val
