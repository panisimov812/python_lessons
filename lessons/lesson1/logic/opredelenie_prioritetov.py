'''
    Оператор    |       Описание
    _________________________________________
    **           |   Возведение в степено
    -----------------------------------------
    +            |   Положительное значение
    -            |   Отрицательное значение
    ~            |   Побитовое отрицание
    ------------------------------------------
    *            |   Умножение
    /            |   Деление
    //           |   Целочисленное деление
    %            |   Деление по модулю
    ------------------------------------------
    +            |   Сложение
    -            |   Вычитание
    ------------------------------------------
    |            |   побитовое ИЛИ
    ------------------------------------------
    ^            |   побитовое исключающее ИЛИ
    ------------------------------------------
    &            |   Побитовое И
    ------------------------------------------
    >>           |   Побитовый сдвиг вправо
    <<           |   Побитовый сдвиг влево
    ------------------------------------------
    >,<=,<,>=,   |     Сравнение
    ==, !=       |
    ------------------------------------------
    =, %=, /=,   | Присваивание
    //=, -=, +=, |
    *=, **=      |
    ------------------------------------------
    is, is not   | Идентичность
    ------------------------------------------
    in, in not   | Вхождение
    ------------------------------------------
    not          | Логическое отрицание
    ------------------------------------------
    and          | Логическое И
    ------------------------------------------
    or           | Логическое ИЛИ

'''

a = 2
b = 4
c = 8

print('\n исходные данные переменных \n a = 2 \n b = b \n c = 8 \n')
# приоритет операции сложения
print('\nDefault Order:\t', a, '*', c, '+', b, '=', a * c + b)
print('Forced Order:\t', a, '* (', c, '+', b, ') =', a * (c + b))
print('\nDefault Order:\t', c, '//', b, '-', a, '=', c // b - a)
print('Default Order:\t', c, '// (', b, '-', a, ') =', c // (c - b))
