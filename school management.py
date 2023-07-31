children={}
classes=[i for i in range(1,12)]

def add():
    name = input('имя ученика: ').title()
    class_child = int(input('номер класса: '))
    if class_child<12:
        children[name]=class_child
        print(f'ученик {name} добавлен на класс {class_child}')
    else:
        print(f'класс {class_child} нету в нашей школе')

def delete():
    name_del = input('имя ученика: ').title()
    if name_del in children.keys():
        print(f'ученик {name_del} исключон из класса {children[name_del]}')
        children.pop(name_del)

    else:
        print(f'ученик под именем {name_del} нету в списке учеников')

def change():
    name_change=input('имя ученика: ').title()
    class_change=int(input('на какой класс перевести: '))
    if class_change in range(1,12):
        if name_change in children.keys():
            children[name_change]=class_change
            print(f'ученик {name_change} переведен на {class_change} класс')
        else:
            print(f'ученик под именем {name_change} нету в списке учеников')
    else:
        print(f'класс {class_change} нету в нашей школе')

while True:
    print('--------------------------','\n''1-добавит ученика','\n''2-удалит ученика','\n''3-изменит класс ученика','\n''4-показат списик учеников')
    operator=int(input('что хотите делат? '))
    if operator==1:
        add()
    elif operator==2:
        delete()
    elif operator==3:
        change()
    elif operator==4:
        k=0
        for i,j in children.items():
            k+=1
            print(f'{k}) {i} ученик класса {j}')
    else:
        print('выбрано не правилний команда')