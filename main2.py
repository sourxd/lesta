def iseven(value):
    """
    Побитовое сравнение чисел. Быстрее чем деление.
    Отлично обрабатывает большие числа.
    """
    if value & 1 == 0:
        return True
    return False