# 
Пример разметки данных (фото документанта взято из открытых источников).
![example](https://github.com/Boris1001/digit/assets/79296774/291d0511-d5bc-4b1d-b9b6-3b96de862723)
Предварительно установить ultrlytics:

sudo apt install python3-pip

pip install pdf2image

sudo apt install poppler-utils

pip install ultralytics==8.0.224

Ссылка на обученную модель: https://drive.google.com/file/d/10xebg1xeBVjJpbgFZsGrohfK4mSqR14b/view?usp=drive_link
Скачать в каталог со space_direction.py

Пример запуска файла: 

python3 space_direction.py '/home/borisvins/BUH-20230202121804.pdf'

Принимает файл в формате pdf

Возвращает одно из значений: 0, 90, 180, 270 соответствующее углу поворота.

Может сохранять результат в result.txt. Для этого нужно снять коментарии с трёх строк:

# output_path = 'result.txt'

if __name__ == "__main__":
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print('The file is not available')
    image = convert_pdf_to_jpg(f'{file_path}')
    degree = space_direction(image, model)

    
#    with open(output_path, 'w') as file:
#        file.write(str(degree))



determining the direction of a document in space by signs
