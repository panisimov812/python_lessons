'''
    Метод множества         |       Описание
    ---------------------------------------------------
    set.add(x)              |   Добавляет элемент x  в множество
    ---------------------------------------------------
    set.update(x,y,z)       |   Добавляется несколько элементов в множество
    ---------------------------------------------------
    set.copy()              |   Возвращает копию множества
    ---------------------------------------------------
    set.pop()               |   Удаляет один элемент из множества, случайным образом
    ---------------------------------------------------
    set.discard( i )        |   Удаляет из множества элемента с порядковым номером i
    ---------------------------------------------------
    set1.intersection(set2) |   Возвращает элементы пренадлижащие обоим множествам
    ---------------------------------------------------
    set1.difference(set2)   |   Возвращает элемент из множества set1, которых нет в set2
'''
print('\nИнциализируем картеж')
zoo = ('Kangaroo', 'Leopard', 'Moose')
print('Tuple:', zoo, '\tLength:', len(zoo))
print(type(zoo))

print('\nИнициалицируем картеж')
bag = {'Red','Green','Blue'}
bag.add('Yellow')
print('\nSet:',bag, '\tLength', len(bag))
print(type(bag))

print('\nИнициализация второго множетсва и возврат элементов пренадлежащим обоим множествам')
box = {'Red','Purple','Yellow'}
print('\nSet:', box,'\tLength', len(box))
print('Common To Both Sets:', bag.intersection(box))