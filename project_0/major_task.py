import numpy as np

def needed_predict(number: int = 1) -> int:
    """Угадываем число через бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число затраченных попыток
    """
    count = 0
    
    least = 1
    
    highest = 100
    
    while least <= highest:
        count +=1
        # Берем среднее число в диапозоне
        predict_num = (least + highest) // 2
        
        if predict_num == number:
            #Нам повезло, угадали с первого раза, можно заканчивать
            break
        elif predict_num < number:
            #Если загаданное число больше
            least = predict_num + 1
            
        else:
            #Если загаданное число меньше    
            highest = predict_num - 1
    return count

def score_game(predict_function) -> int:
    """За какое количество попыток в среднем алгоритм угадывает число

    Args:
        predict_function: функция нахождения

    Returns:
        int: среднее кол-во попыток
    """
    
    count_ls = []
    
    #Загадывается список рандомных чисел
    random_array = np.random.randint(1, 101, size=1000)
    
    for number in random_array:
        count_ls.append(predict_function(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score 
   
if __name__ == "__main__":
    score_game(needed_predict)