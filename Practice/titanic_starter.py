 # Практическая работа

#### Задание 1: Скачайте файл с данными о погибших на титанике
import requests
import os

def to_str(lines):
    # Функция возвращает список преобразованных строк,
    # а принимает список байтовых строк
    
    # Отдельно взятую строку байт можно преобразовать в строку
    # символов следующим образом: str(line, 'utf-8')+'\n'
    # Символ перехода на новую строку добавляется, чтобы при
    # записи в файл каждая запись начиналась с новой строки
    
    # Удалите pass и представьте ваше решение
    pass

    #если не будет работать загрузка файла заккоментить date = download, раскомментить date = open....
def download_file(url):
    # Делаем GET-запрос по указанному адресу
    response = requests.get(url)
    # Получаем итератор строк
    text = response.iter_lines()
    # Каждую строку конвертируем из массива байт в массив символов
    text = to_str(text)

    # Если файла не существует, то создаем его и записываем данные
    if not os.path.isfile("titanic.csv"):
        with open("titanic.csv", "w") as f:
            f.writelines(text)
    return text

# data = download_file("https://raw.githubusercontent.com/haven-jeon/introduction_to_most_usable_pkgs_in_project/master/bicdata/data/titanic.csv")

# Если вы успешно выполнили первое задание, то файл можно не скачивать
# каждый раз, а вместо этого данные читать из файла. Расскомментируйте
# следующую строку и закомментируйте предыдущую
data = open('titanic.csv')
print(os.path.isfile("titanic.csv"))

#### Задание 2: Получаем список словарей - done
# Модуль для работы с файлами в формате CSV
import csv

reader = csv.DictReader(data)
reader.fieldnames[0] = 'lineno'
titanic_data = list(reader)

# Модуль для красивого вывода на экран
from pprint import pprint as pp
#for row in titanic_data:
#    pp(row)



#### Задание 3: Узнать количество выживших и погибших на Титанике - done
def survived(tit_data):
    a = 0
    b = 0
    for i in range(len(tit_data)):
        if tit_data[i]['survived'] == '1':
            a += 1
        else:
            b += 1
    return a, b

pp(survived(titanic_data)) # (500, 809)


#### Задание 4: Узнать количество выживших и погибших на Титанике -done
#### по отдельности для мужчин и женщин
from operator import itemgetter
from itertools import groupby
def survived_by_sex(tit_data):
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, (количество выживших, число погибших))
    female = []
    male = []
    for i in range(len(tit_data)):
        if tit_data[i]['sex'] == "female":
            dict_f = dict()
            dict_f['survived'] = tit_data[i]['survived']
            female.append(dict_f)
        else:
            dict_m = dict()
            dict_m['survived'] = tit_data[i]['survived']
            male.append(dict_m)
    return [('female', survived(female)), ('male',survived(male))]
    # Подумайте над использованием функции survived()
pp(survived_by_sex(titanic_data)) # [('female', (339, 127)), ('male', (161, 682))]
#### Задание 5: Узнать средний возраст пассажиров
def average_age(tit_data):
    age = 0
    b = 0
    for i in range(len(tit_data)):
        if tit_data[i]['age'] != "NA":
            age += float(tit_data[i]['age'])
        else:
            b += 1
    average_age = round(age / (len(tit_data) - b), 2)
    return average_age
    # Функция возвращает средний возраст пассажиров
pp(average_age(titanic_data)) # 29.88


#### Задание 6: Узнать средний возраст мужчин и женщин по отдельности - done
def average_age_by_sex(tit_data):
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, средний возраст)
    female = []
    male = []
    for i in range(len(tit_data)):
        if tit_data[i]['sex'] == "female":
            dict_f = dict()
            dict_f['age'] = tit_data[i]['age']
            female.append(dict_f)
        else:
            dict_m = dict()
            dict_m['age'] = tit_data[i]['age']
            male.append(dict_m)
    return [('female', average_age(female)), ('male',average_age(male))]
    
    # Подумайте над использованием функции average_age()
pp(average_age_by_sex(titanic_data)) # [('female', 28.68), ('male', 30.58)]


#### Задание 7: Сколько детей и взрослых было на борту: - done
def get_group(tit_data):
    children = []
    teens = []
    adults = []
    for i in range(len(tit_data)):
        if tit_data[i]['age'] != "NA":
            if 0 <= float(tit_data[i]['age']) < 14:
                children.append(tit_data[i])
            elif 14 <= float(tit_data[i]['age']) < 18:
                teens.append(tit_data[i])
            else:
                adults.append(tit_data[i])

    return {'[0-14)':children, '[14-18)':teens, '[18-inf)':adults}
#pp(get_group(titanic_data))

#### Получить группы в следующих диапазонах возрастов:
#### [0-14), [14-18), [18-inf]

#### Задание 8: Сколько в каждой группе выживших
print("Survived in age groups:")
pp({'0-14': survived(get_group(titanic_data)['[0-14)'])[0], '14-18': survived(get_group(titanic_data)['[14-18)'])[0], '18-inf': survived(get_group(titanic_data)['[18-inf)'])[0]})

#### Задание 9: Сколько в каждой группе выживших по отдельности для
#### мужчин и женщин
print("Survived in age groups by sex:")
pp({'0-14':survived_by_sex(get_group(titanic_data)['[0-14)']) ,'14-18': survived_by_sex(get_group(titanic_data)['[14-18)']), '18-inf': survived_by_sex(get_group(titanic_data)['[18-inf)'])})

