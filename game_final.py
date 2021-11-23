"""Игра 'Угадай число'
Компьютер сам загадывает и сам угадывает число"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    while count < 20:
        count+=1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break # Выход из цикла если угадали
    return count


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

if __name__ == '__main__':
    # Вызываем функцию
    score_game(random_predict)