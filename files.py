import json
import csv

def save_to_json(filename, data):
    with open(filename,'w') as file:
        json.dump(data,file)

def read_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def save_to_csv(filename, header, data):
    with open(filename,'w',newline='') as file:
        writer=csv.writer(file,delimiter=';')
        writer.writerow(header)
        temp=[]
        for row in data:
            temp.append(data[row])
        writer.writerow(temp)

def read_from_csv(filename):
    with open(filename,'r') as file:
        reader=csv.reader(file,delimiter=';')
        temp=[row for row in reader]#считали все во временную переменную
        header=temp[0]#получили заголовоки
        temp_data=temp[1]#получили данные
        data={}
        for i in range(len(header)):
            data[header[i]]=temp_data[i]
        return data

