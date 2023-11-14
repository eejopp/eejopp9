import time, datetime, files
import  json

import keyboard

data={}
json_data=''

def on_release(key):
    print(f'Release key {key.name}')

def help():
    print("F1 - Help (этот текст)")
    print("F2 - Save to XML")
    print("F3 - Load from XML")
    print("F4 - Save to JSON")
    print("F5 - Load from JSON")

def greet():
    help()
    name=input('Вы начинаете игру. Введите свое имя:')
    age=input('Сколько вам лет?')
    gender=input('Ваш пол:')
    date=datetime.datetime.now()
    global data,json_data
    data={'name':name, 'age':age, 'gender':gender, 'data':str(date)}
    #требуется, чтобы данные хранились в формате json, но не понятно зачем это, так как формат json это и есть словарь
    #но раз требуется, то сохранение делается вот такой командой
    json_data=json.dumps(data)


def awake_in_room():
    global data
    print("Вы просыпаетесь в комнате")
    print('Вам приснился \'кошмар\'')
    time.sleep(1)
    print('Вы испугались?\n\n')
    time.sleep(1)
    while True:
        yeses=['Да','да','д','yes','y','YES','Yes']
        noes=['Нет','нет',"н",'no','No','n']
        yn=input('(Да/Нет):')
        if yn in yeses:
            standup();
            break
        if yn in noes:
            print('Продолжаем спать дальше')
            time.sleep(2)
            awake_in_room()
    data['quest1']='yes'

def goodend():
    print('Happy end!')
    exit(0)
def bad_end():
    print('Вы умерли.')
    time.sleep(1)
    print('Вы не смогли пройти игру на счастливую концовку')
    time.sleep(1)
    print('Попробуйте еще раз.')
    exit(0)



def see_man():
    print('Вы видите на соседней кровати мужчину.')
    time.sleep(1)
    print('Ваши действия')
    time.sleep(1)
    print("1. Разбудить")
    print("2. Не беспокоить")
    select=input()
    if select=='2':
        print('Вы ищите выход самостоятельно')
    if select==('1'):
        dialog()



def manyak():
    print('После тчательного осмотра')
    print('вы понимаете что идти вам больше некуда')
    print('и просто дожидаетесь маньяка.')

    time.sleep(3)

    print('Вы ярая фанатка Black Star')
    print('и мечтаете выйти замуж за одного из главных')
    print('холастяков страны.')

    time.sleep(3)

    print('И вам это удается!')
    print('Через минуту к вам входит в комнату')
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Ваша мечта')
    print('О рассказывает вам всю историю похищения.')
    time.sleep(3)
    print('Вам стало невероятно жалко вашего кумира.')
    time.sleep(3)
    print('И теперь вы согласны пойти на все ради него.')
    time.sleep(3)
    print('Всю жизнь вы ждали этого момента')
    time.sleep(3)
    print('И вот час настал!')
    time.sleep(3)
    print('Ваш кумир делает предложение руки и сердца!')
    time.sleep(1)
    print("1. Сказать да")
    print("2. Сказать нет")

    select = input()
    if select == ('1'):
        print('Поздравляю!')
        time.sleep(1)
        print('Вы дошли до финала')
        print('и прошли игру со счастливым концом.')
        time.sleep(3)
        print('Ваш кошмар превратился в мечту.')
        time.sleep(3)
        print('Вы теперь замужем')
        print('вы смогли проснуться')
        print('и не умереть от инфаркта')
        print('На вашем пальце вы обнаружили прекрастное кольцо.')
        time.sleep(1)
        goodend()
    if select == ('2'):
        bad_end()




def mrakroom():
    print('Вы решили выбраться из этой мрачной комнаты.')
    time.sleep(2)
    print('Вы проверяете дом и ищите зацепки.')
    time.sleep(3)
    print('(знания о похитителя могли бы сейчас пригодиться)')
    time.sleep(3)
    print('Этот дом выглядит как сказка')
    print('но прошлая комната продолжает вас пугать.')
    time.sleep(3)
    print('Вы видите две двери и решаете в какую зайти.')
    time.sleep(2)
    print('Будьте очень внимательны с выбором.')
    print('Он легко повлияет на вышу судьбу.')
    time.sleep(1)
    print("1. Правая дверь")
    print("2. Левая дверь")
    select = input()
    if select == ('1'):
        print('Эта комната вся завешена портретами Егора Крида.')
        time.sleep(2)
        print('Вы начинаете рассматривать каждую деталь.')
        time.sleep(1)
        print('и понимаете кто похитил вас на самом деле.')
        manyak()
    if select == ('2'):
        print('Эта комната вся завешена портретами Тимати.')
        time.sleep(2)
        print('Вы начинаете рассматривать каждую деталь.')
        time.sleep(1)
        print('и понимаете кто похитил вас на самом деле.')
        manyak()




def  exitown():
    time.sleep(2)
    print(' ')
    print("1. Осмотреть цепь")
    print("2. Пытаться достать ключ")
    select = input()
    if select == ('2'):
        print('Вы поняли что цепь непрочная.')
        time.sleep(2)
        print('Теперь можете легко выбраться')
        mrakroom()
    if select == ('1'):
        print('Пока вы пытались дотянуться до ключа')
        print('вы обнаружили что цепь непрочнаяя')
        time.sleep(2)
        print('и смогли легко выбраться.')
        mrakroom()



def knowhistory():
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Вы узнали кто вас похитил')
    time.sleep(1)
    print('Вам стало страшно выбираться одному')
    time.sleep(1)
    print('Предложить мужчине выбираться вместе?')
    while True:
        yeses=['Да','да','д','yes','y','YES','Yes']
        noes=['Нет','нет',"н",'no','No','n']
        yn=input('(Да/Нет):')
        if yn in yeses:
            print('Он вам не доверяет.')
            time.sleep(1)
            print('Вы ищите выход самостоятельно.')
            exitown()
        if yn in noes:
            print('Вы ему не доверяете.')
            time.sleep(1)
            print('Вы ищите выход самостоятельно.')
            exitown()



def dialog():
    time.sleep(1)
    print("Он тоже оказался заключенным, но находится тут уже 5 дней.")
    time.sleep(1)
    print("Вы хотите узнать его историю?")
    while True:
        yeses=['Да','да','д','yes','y','YES','Yes']
        noes=['Нет','нет',"н",'no','No','n']
        yn=input('(Да/Нет):')
        if yn in yeses:
            knowhistory()
            break
        if yn in noes:
            print('Он больше не хочет с нами разговаривать.')
            time.sleep(1)
            print('Теперь вы работаете самостоятельно.')
            time.sleep(1)
            exitown()




def find_exit():
    print("Оглядываемся по сторонам в поисках выхода.")
    time.sleep(2)
    print('Вы увидели ключ, на столе, но не можете до него дотянуться.')
    time.sleep(1)
    print('Ваши действия?')
    time.sleep(1)
    print("1. Осмотреться")
    print("2. Плакать")
    select=input()
    if select=='2':
        bad_end()
    if select==('1'):
        see_man()




def standup():
    print('Пытаемся встать.')
    time.sleep(2)
    print('Обнаруживаем, что мы прикованы цепью к кровати и находимся не в своей комнате.')
    time.sleep(1)
    print("Что делать?")
    time.sleep(1)
    print("1. Искать выход из ситуации")
    print("2. Плакать")
    select=input()
    if select=='2':
        bad_end()
    if select==('1'):
        find_exit()

def on_f1_release():
    help()


def on_f2_release():
    print('Save data in CSV')
    header=data.keys()
    files.save_to_csv('data.csv',header,data)

def on_f3_release():
    print('Load data from CSV')
    data=files.read_from_csv('data.csv')
    print(data)

def on_f4_release():
    print('Save data in Json')
    #header=['Имя','возраст','пол','время','испугались']
    files.save_to_json('data.json',data)

def on_f5_release():
    print('Load data from Json')
    data=files.read_from_json('data.json')
    print(data)

#keyboard.on_release(on_release)
keyboard.add_hotkey('f2',on_f2_release);
keyboard.add_hotkey('f3',on_f3_release);
keyboard.add_hotkey('f4',on_f4_release);
keyboard.add_hotkey('f5',on_f5_release);
#keyboard.wait()