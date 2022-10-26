import csv
import os


files = os.listdir('C:/Users/krif1/OneDrive/Рабочий стол/блокноты')
del(files[files.index("test.py")])

ans = input("Хотите посмотреть блокноты [1], создать блокнот [2], изменить блокнот[3] или удалить блокнот [4]? ")

if ans == '1':
    print("Ваши блокноты:")
    for i in files:
        print(i)
        
if ans == '4':
    name = input("Введите имя блокнота: ")
    try:
        if '.csv' in name:
            os.remove('C:/Users/krif1/OneDrive/Рабочий стол/блокноты/' + name)
        else:
            os.remove('C:/Users/krif1/OneDrive/Рабочий стол/блокноты/' + name + '.csv')
        print("Блокнот удалён")
    except FileNotFoundError:
        print("Данный блокнот не найден")    
        
if ans == '2':
    im = input("Введите имя нового блокнота: ")
    if '.csv' in im:
        pass
    else:
        im = im + '.csv'
    if im in files:
        print("Такой блокнот уже есть")
    else:
        new = open(im, 'a')
        print("Блокнот создан")
        
if ans == '3':
    na = input("Введите имя блокнота, с которым хотите работать: ")
    if '.csv' in na:
        pass
    else:
        na = na + '.csv'  
    if not(na in files):
        print("Данный блокнот не найден")
    else:
        n = 0
        with open(na, newline='') as File:
            reader = csv.reader(File, delimiter=',')
            for row in reader:
                if row != []:
                    n += 1 #кол-во записей в блокноте

        an = input("Введите команду: ")
        if an.lower() == 'добавить':
            t = input("Введите задачу: ")
            task = (str(n + 1)+ ',' + t).split(",")
            myFile = open(na, 'a')
            with myFile:
                writer = csv.writer(myFile)
                writer.writerow(task)
            print("Запись добавлена")
            
        if 'прочитать' in an.lower():
            data = []
            if an.lower() == 'прочитать':
                with open(na, newline='') as File:
                    reader = csv.reader(File, delimiter=',')
                    for row in reader:
                        if row != []:
                            data.append(row)
                            print(row)
            else:
                k = an.split(' ')[-1]
                if int(k) > n:
                    print("Нет записи с таким номером")
                else:
                    with open(na, newline='') as File:
                        reader = csv.reader(File, delimiter=',')
                        for row in reader:
                            if row != [] and row[0] == str(k):
                                del(row[0])
                                print(row)
                                
                                    
            
        if 'изменить' in an.lower():
            num = an.split(' ')[-1]
            data = []
            with open(na, newline='') as File:
                t = input("Введите задачу: ").split(',')        
                reader = csv.reader(File, delimiter=',')
                for row in reader:
                    data.append(row)
                data[int(num) - 1] = []
                data[int(num) - 1] = [num] + t
                del(data[int(num)])
                
            os.remove('C:/Users/krif1/OneDrive/Рабочий стол/блокноты/' + na)
            myFile = open(na, 'w')
            with myFile:
                writer = csv.writer(myFile)
                writer.writerows(data)             
            print("Запись изменена")  
            
        if 'удалить' in an.lower():
            num = an.split(' ')[-1]
            data = []
            with open(na, newline='') as File:       
                reader = csv.reader(File, delimiter=',')
                for row in reader:
                    data.append(row)
                data[int(num) - 1] = []
                
            os.remove('C:/Users/krif1/OneDrive/Рабочий стол/блокноты/' + na)
            myFile = open(na, 'w')
            with myFile:
                writer = csv.writer(myFile)
                writer.writerows(data)             
            print("Запись удалена")        