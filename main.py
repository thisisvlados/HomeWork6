import json, csv
import datetime as dt

data = [
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": "true",
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": "false",
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": "true",
        "languages": ["C#", "C++", "C"]
    }
]

#0
with open("HomeWork_6.json", "w") as f:
    json.dump(data, f, indent= 3)

#Сверху создаем json файл

with open("HomeWork_6.json", "r") as read_f:
    data = json.load((read_f))
    pass
print(type(read_f))
#1
with open("HomeWork_6.json", "r") as read_f:
    read_py = json.load(read_f)
    pass
print(type(read_py))

with open("HomeWork_6.json", "r") as read_csv:
    file_writer = csv.reader(read_csv)
    for csv_file in file_writer:
        pass

print(type(csv_file))
#2
with open("HomeWork6_3.csv", "w") as csv_file:
    '''writer = csv.DictWriter(csv_file, fieldnames=[key for key in data[0].keys()])
    writer.writerow(item for item in data)'''
    writer = csv.writer(csv_file)
    writer.writerow(read_py)
#3
#Добавляем информацию о человеке в файл json

dc = {
    'name' : input('Введите имя: '),
    'birthday': input('Введите дату рождения: '),
    'height' : input('Введите рост: '),
    'weight' : float(input('Введите вес: ')),
    'car' : input('Есть ли машина (true/false): '),
    'languages' : input('Какой язык программирования знаете (C++, Python, Pascal, Delphi, C#, C): ')
}
sl = []
with open("HomeWork_6.json", "r") as f:
    sl = json.load(f)
    sl.append(dc)
with open("HomeWork_6.json", "w") as f:
    json.dump(sl,f, indent = 2)


#4
#Добавляем информацию о человеке в файл csv
with open("HomeWork6_3.csv", "a") as csv_file:
    list = ['Name: Valera, Birthday: 19, height: 210, weight: 60.3, car: true, languages: C++, Python']
    writer = csv.writer(csv_file)
    writer.writerow(list)


#5
def Names(name):
    with open ("HomeWork_6.json", "r") as f:
        for i in json.load(f):
            for key, value in i.items():
                if key == "name" and value == name:
                    print(i.items())

#6

def lang(languages):
    with open ("HomeWork_6.json", "r") as f:
        for i in json.load(f):
            for k, v in i.items():
                if k == "languages" and languages in v:
                    print(i.items())

name = input('Введите имя, которое хотите найти: ')
languages = input('Введите язык программирования: ')
Names(name)
lang(languages)