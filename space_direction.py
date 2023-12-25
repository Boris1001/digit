'''
Комментарии к коду:
1. `pip install ultralytics==8.0.219` -  Установка ultralytics
1. `from ultralytics import YOLO` - Импорт класса YOLO из библиотеки ultralytics.
2. `image = 'test_img_1_0.jpg.png'` - Путь к изображению.
3. `model = YOLO("best_1522.pt")` - Создание модели YOLO с использованием файла весов "best_1522.pt".
4. `def count_yolo_objects(class_names, confidence_threshold, yolo_output):` - Функция для подсчета объектов, распознанных YOLO.
5. `def compare_values(arr, value_dict):` - Функция для сравнения значений.
6. `def space_direction(image, model):` - Функция для определения направления поворота изображения.
7. `results = model.predict(image)` - Результаты работы модели на изображении.
8. `class_id = results[0].boxes.cls.cpu().numpy().astype(int)` - Идентификаторы классов объектов.

'''

from ultralytics import YOLO  
import cv2
import numpy as np

# Путь к изображению
image = 'test_img_1_0.jpg.png'       

# Загрузка обученной модели
model = YOLO("best_1522.pt")         

def count_yolo_objects(class_names, confidence_threshold, yolo_output):
    """
    Функция для подсчета объектов, распознанных YOLO.

    Аргументы:
    class_names -- список названий классов
    confidence_threshold -- порог уверенности
    yolo_output -- выходные данные YOLO

    Возвращает:
    num_objects -- количество объектов
    yolo_classes -- список классов объектов
    """
    num_objects = 0
    yolo_classes = []

    for detection in yolo_output:
        class_index = int(detection[4])
        confidence = detection[5]

        if confidence >= confidence_threshold:
            num_objects += 1
            yolo_classes.append(class_names[class_index])

    return num_objects, yolo_classes

def compare_values(arr, value_dict):
    """
    Функция для сравнения значений.

    Аргументы:
    arr -- массив значений
    value_dict -- словарь соответствия классов и значений

    Возвращает:
    result -- результат сравнения
    """
    count_40 = 0
    count_90 = 0
    count_180 = 0
    count_270 = 0

    # Подсчет количества значений
    for value in arr:
        if value in value_dict:
            if value_dict[value] == '4_0' or value_dict[value] == '7_0':
                count_40 += 1
            elif value_dict[value] == '4_90' or value_dict[value] == '7_90':
                count_90 += 1

    # Сравнение количества значений и возвращение результата
    if count_40 > count_90:
        return 0
    else:
        return 90


def space_direction(image, model):
    """
    Функция определения направления поворота изображения.

    Аргументы:
    image -- изображение
    model -- модель нейронки

    Возвращает:
    result -- направление поворота (0 или 90)
    """
    results = model.predict(image)
    CLASS_NAMES_DICT = model.model.names
    for r in results:
        class_id = results[0].boxes.cls.cpu().numpy().astype(int)
    
    result = compare_values(class_id, CLASS_NAMES_DICT)
    return result
    
 
# Вывод результатов
print("Документ повёрнут на", space_direction(image, model), "градусов.")
