# C. Большая семья бабушки Алевтины

## Ограничения
 | Ограничение времени | 2 секунды                        |
 |----------------------|----------------------------------|
 | Ограничение памяти   | 256.0 Мб                         |
 | Ввод                 | стандартный ввод или input.txt   |
 | Вывод                | стандартный вывод или output.txt |

## Описание задачи

У бабушки Алевтины очень большая семья, которая живёт в разных городах. Раньше все члены семьи собирались дома у бабушки Алевтины, но в 2020 году было решено, что созваниваться по видеосвязи будет безопаснее для всех.
У каждого домохозяйства есть некоторое количество комнат с устройствами, при помощи которых можно организовать видео-конференцию на несколько членов семей из других городов. Комнаты пользуются большим спросом, так как некоторые члены семьи работают на удалёнке и должны встречаться с коллегами по рабочим встречам, поэтому в расписании есть уже занятые слоты. Также все родственники хотят поделиться новостями друг с другом, поэтому у всей семьи есть расписание звонков, чтобы каждый участник мог пообщаться в нужное время.

Вам дана информация о доступности комнат во всех домохозяйствах на день встречи членов семей, а также m запросов на проведение часовой встречи для родственников из разных городов. Для каждого запроса требуется определить набор подходящих временных слотов (в каждом городе надо выбрать ровно одну комнату, и все эти комнаты должны быть свободны в какой-то час), или сообщить, что подходящего набора нет.

Обратите внимание, запросы независимы друг от друга, то есть, ответ на очередной запрос не влияет на занятость комнат.

## Формат ввода

В первой строке ввода записано число c(2 ≤ c ≤ 16) — количество домохозяйств.
Далее следуют c блоков с описанием домохозяйств. В первой строке каждого блока записано название города, где расположена часть семьи, и количество комнат в нём ni(1 ≤ ni ≤ 100). Далее следуют ni строк, в каждой из которых дано расписание бронирования комнаты tij и его название sij. Расписание tij представляет собой строку ровно из 24 символов, k-й символ которой равен ‘X’, если в k-й час суток комната недоступна для бронирования, или ‘.’, если доступна.

В следующей строке записано число m(1 ≤ m ≤ 1000) — количество запросов. В каждой из следующих m строк сначала записано число l(2 ≤ l ≤ c) — количество городов, в которых должно быть забронировано по одной комнате, а далее записаны l названий городов. Названия городов разделены одиночными пробелами.

Названия никаких двух комнат не совпадают. Названия никаких двух городов также не совпадают. Названия комнат и городов представляют собой непустые строки, состоящие из букв английского алфавита длиной не более 10 символов.

## Формат вывода

Для каждого из m запросов в отдельной строке выведите сообщение «Yes» (без кавычек) и названия комнаты, в которой можно организовать встречу, или выведите сообщение «No» (без кавычек), если подходящую комнату найти невозможно.
Комнаты в каждом ответе можно выводить в любом порядке. Если возможных ответов на запрос несколько, разрешается вывести любой подходящий.

## Примеры

### Пример 1

**Ввод:**
```
3
Moscow 2
XXXXXXXX.X.X.X.X.X.XXXXX Kvartal
XXXXXXXXX.X.X.X.X.X.XXXX Kvartet
Minsk 1
XX.XXXXX........XXXXXXXX Toloka
Berlin 2
XX..XXXXXXXXXXXXXXXXXXXX Mitte
XXXXXXXXXXXXXXXX.....XXX Lustgarten
4
3 Moscow Minsk Berlin
2 Moscow Minsk
2 Minsk Berlin
2 Moscow Berlin
```

**Вывод:**
```
No
Yes Kvartal Toloka
Yes Toloka Mitte
Yes Kvartal Lustgarten
```

### Пример 2

**Ввод:**
```
3
Moscow 1
XXXXXXXX...........XXXXX Kvartal
Minsk 1
XXXXXXX...........XXXXXX Toloka
Berlin 1
XXXXXX...........XXXXXXX Mitte
1
3 Moscow Minsk Berlin
```

**Вывод:**
```
Yes Kvartal Toloka Mitte
```