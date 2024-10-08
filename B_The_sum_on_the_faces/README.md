# B. Сумма на гранях

## Ограничения
 | Ограничение времени | 1 секунда |
 |----------------------|-----------|
 | Ограничение памяти   | 256.0 Мб  |
 | Ввод                 | стандартный ввод или input.txt |
 | Вывод                | стандартный вывод или output.txt |

## Описание задачи

Вася взял игральную кость и написал на гранях числа a1, a2, a3, a4, a5 и a6.

Для генерации случайного числа Вася решил воспользоваться следующим алгоритмом:

1. Выбрать число k.
2. Подбросить кубик k раз и записать на листик последовательно выпавших чисел bj.
3. Пройтись по списку с конца и вычеркнуть число bj, если оно равно b(j-1) (b1 всегда останется в последовательности).

Определите математическое ожидание суммы оставшихся в последовательности чисел, если Вася сообщит вам числа ai и k.

Обратите внимание, что кубик у Васи честный и все выпадение любой из граней равновероятно. Кроме этого, подбрасывания кубика независимы.

## Формат ввода

В первой строке записаны 6 целых чисел a1, a2, a3, a4, a5 и a6 (1 ≤ ai ≤ 1000).

Во второй строке записано одно число k (1 ≤ k ≤ 1000).

## Формат вывода

Выведите одно вещественное число — требуемое по условию задачи математическое ожидание.

Ответ будет считаться верным, если относительная или абсолютная погрешность не будет превышать 10^(-6).

## Примеры

### Пример 1

**Ввод:**
```
1 2 3 4 5 6
2
```

**Вывод:**
```
6.4166666667
```

### Пример 2

**Ввод:**
```
1 1 1 1 1 1
3
```

**Вывод:**
```
1.0000000000
```

### Пример 3

**Ввод:**
```
1 2 1 2 2 2
2
```

**Вывод:**
```
2.3333333333
```

## Примечания

В первом примере из 36 возможных исходов в 6 будет вычеркнуто повторяющееся число.

Во втором примере возможна единственная последовательность 2 2 2, после вычеркивания двух двоек длина последовательности станет равной одному.
