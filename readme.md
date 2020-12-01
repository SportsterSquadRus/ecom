Данный репозиторий является результатом решения тестовой задачи.

## Формулировка задачи:
Написать на Python программу хранения и редактирования списка заказов.
Функционал:
- Вывести список заказов за указанный период
- Добавить заказ
- Удалить заказ
- Изменить заказ
Требования:
- Хранить заказы в реляционной базе данных.
- Тип базы данных должен легко меняется. Например, если изначально данные
хранились в MySQL, то программу должно быть легко переделать на MS SQL,
заменив всего одну строку кода, а в идеале вообще не меняя код, только выполнив
настройки.
- Программа должна иметь WEB-интерфейс.
- К программе должна прилагаться инструкция как ее развернуть/запустить.
- Атрибуты заказа: номер, дата, сумма, контрагент, текст заказа.
Как будет оцениваться:
При разработке программы нужно показать знания python, ООП, теории
реляционных баз данных, умение обосновать выбор способа реализации. В
сопроводительном письме описать, почему программа реализована именно таким
способом, из каких соображений.
-----------------------------------

## Инструкция по установке:
1. Скачать репозиторий
2. Установить и запустить виртуальное окружение.  
    Подробнее можно ознакомиться по ссылке https://pypi.org/project/virtualenv/
3. Установить зависимости (перечень указан в файле requirements.txt).  
    Команда для установки зависимостей:  
    pip install -r requirements.txt
4. Выбрать базу данных.  
    По умолчанию настройки установлены на sqlite3. Настройки под PostgreSQL закоментированы в файле settings.py
5. Произвести миграции следующей командой:  
     python3 manage.py migrate
6. (опционально) Ввести тестовые данные командой:  
    python3 manage.py loaddata test.json
7. Запустить сервер:  
    Команда запуска сервера:  
    python3 manage.py runserver
-----------------------------------

## Обоснование применения решений:

1. Требования PEP8 соблюдаются путем автоформатирования кода с помощью vscode и pylint


2. Для удовлетворения требований, описанных в разделе "Атрибуты заказа", была создана следующая модель:
```

    class Order(models.Model):


        date = models.DateField(verbose_name='Дата заказа')

        agent = models.CharField(max_length=100, verbose_name='Контрагент')

        comment = models.CharField(max_length=150, verbose_name='Текст заказа')

        amount = models.DecimalField(
            max_digits=9, decimal_places=2, verbose_name='Сумма заказа', validators=[MinValueValidator(Decimal('0.01'))])
```
**Номер заказа**:  
При прохождении миграций в базе данных будет создана таблица с обозначенными полями, при этом поле номера заказа будет выполнять ID экземпляра таблицы. Так как в задании нет уточнений, а ответы на дополнительные вопросы (в том числе касательно поля номера заказа) не получены, то считаю данное решение целесообразным.

**Дата заказа**:   
date = models.DateField(verbose_name='Дата заказа')   
Так как отсутствуют уточнения касательно поля "дата заказа", было принято временное решение поле "Дата заказа" устанавливать вручную каждый раз при создании и редактировании заказа. Возможно, следовало бы его указывать автоматически при создании заказа, но для принятия подобного решения прошу дать дополнительные уточнения.

**Текст заказа**:  
comment = models.CharField(max_length=150, verbose_name='Текст заказа')  
Создано обычное текстовое поле.

**Контрагент**:  
agent = models.CharField(max_length=100, verbose_name='Контрагент')  
В условиях отсутствия уточнений по данному полю, которое, возможно, должно быть связано с элементами другой таблицы, было принято решение создать текстовое поле, аналогичное полю "Текст заказа"

**Сумма заказа**:  
amount = models.DecimalField(
            max_digits=9, decimal_places=2, verbose_name='Сумма заказа', validators=[MinValueValidator(Decimal('0.01'))])  
Ввиду отсутствия уточнений по данному полю, создано числовое поле с возможностью указания двух знаков после запятой и минимальным значением, равным 0,01.


3. В файле views.py был создан ряд обработчиков в целях удовлетворения требований по созданию, удалению и изменению заказа.

4. Для реализации требования по созданию механизма фильтрации заказов по дате был создан обработчик, который принимает из HTML формы два параметра: дату ограничения "слева" и дату ограничения "справа". Так как нет дополнительных уточнений по ограничениям на данное поле, то в обработчике за крайние даты по умолчанию взяты "1900-01-01" и "2100-01-01" соответственно. В случае, если пользователь не введет одну из дат, по умолчанию будут применены упомянутые значения. Актуальная на сегодня дата не взята намеренно, так как в задании нет информации о существовании или отсутствии будущих заказов.

5. Для вывода домашней страницы был создан обработчик, который выводит перечень всех заказов. Непосредственно из домашней страницы пользователь имеет возможность создать, удалить и изменить заказы, произвести их фильтрацию и ознакомиться с информацией о конкретном заказе.

6. Проверка работоспособности формы осуществляется с помощью тестов.

7. С переченем активных элементов страницы можно ознакомиться на картинке ниже (обозначены цветом)


![Image of Yaktocat](https://github.com/SportsterSquadRus/ecom/blob/master/1.png)
