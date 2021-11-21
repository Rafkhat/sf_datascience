"""Игра 'Угадай число'
Компьютер сам загадывает и сам угадывает число"""

import numpy as np

# Стрелочкой -> указываем что на выходе, 1 - стандартное значение числа, 
# по умолчанию

def random_predict(number: int=1) -> int:
    
    """  Рандомно угадываем число
    Это документация. С помощью DocstringGenerator Enter автоматически 
    заполняются поля
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток"""
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break # Выход из цикла если угадали
    return count
#print(f'Количество попыток: {random_predict(10)}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов 
    угадывает наш алгоритм

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_lst = [] # Здесь будем сохранять количество попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    
    for number in random_array:
        count_lst.append(random_predict(number))
    score = int(np.mean(count_lst))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# Вызываем функцию
score_game(random_predict)
