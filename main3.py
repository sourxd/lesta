def mysort(data: list) -> list:
    """
    Быстрая сортировка, которая разделяет входной список на 2 списка. Один больше опорного числа,
    второй меньше. После этого рекурсивно проходит по каждому массиву.
    Базовый случай, при котором длина подмассива равна меньше или 1 означает,
    что список отсортирован и его нужно вернуть.
    """
    if len(data) > 1:
        av_value = data[0]
        small = [i for i in data[1:] if i <= av_value]
        large = [j for j in data[1:] if j > av_value]
        return mysort(small) + [av_value] + mysort(large)
    else:
        return data


data = [53, 345, 56, 567, 23, 7, 4, 76, 23]
print(mysort(data))
