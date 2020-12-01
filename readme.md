Данный репозиторий является результатом решения тестовой задачи.

Инструкция по установке:
1. Скачать репозиторий
2. Установить и запустить виртуальное
    Подробнее читать тут https://pypi.org/project/virtualenv/
3. Установить зависимости (перечень указан в файле requirements.txt)
    Команда для установки зависимостей:
    pip install -r requirements.txt
4. Выбрать базу данных
    По умолчанию настройки установлены на sqlite3. Настройки под PostgreSQL закоментированы в файле settings.py
5. Произвести миграции следующей командой:
     python3 manage.py migrate
6. Запустить сервер следующей командой
    python3 manage.py runserver


Обоснование применения тех или иных решений:

Формулировка задачи:
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


1. Для удовлетворения требований, описанных в разделе "Атрибуты заказа", была создана следующая модель:
    class Order(models.Model):
        date = models.DateField(verbose_name='Дата заказа')
        agent = models.CharField(max_length=100, verbose_name='Контрагент')
        comment = models.CharField(max_length=150, verbose_name='Текст заказа')
        amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма заказа')

    При прохождении миграций в базе данных будет создана таблица с обозначенными полями, при этом поле номера заказа будет выполнять ID экземпляра таблицы.
    Так как в задании нет уточнений, а ответ на дополнительные вопросы (в том числе касательно поля номера заказа) не получен, то считаю данное решение целесообразным.

2. В целях удовлетворения требований по созданию, удалению и изменению заказа был создан ряд обработчиков в файле views.py и форма создания заказа в файле forms.py. При этом хочу обратить внимание на отсутствие уточнений по полю "дата заказа" Возможно "дата заказа" должна была бы устанавливаться автоматически при создании заказа, или меняться при редактировании, или наоборот не меняться. В результате было принято временное решение: "Дата заказа" устанавливается вручную каждый раз при его создании и редактировании. Кроме того нет сведений по полю "контрагент". Как следствие было принято решение по созданию обычного текстового поля, аналогичного полю "Текст заказа". Возможно следовало бы его привязать к некоторому полю из таблицы контрагентов.

3. Для реализации требования по созданию механизма фильтрации заказов по дате был создан обработчик, который принимает их HTML формы два параметра: дату ограничения "слева" и дату ограничения "справа". Так как нет дополнительных уточнений по ограничениям на данное поле, то в обработчике за крайние даты по умолчанию взяты "1900-01-01" и "2100-01-01" соответственно. В случае, если пользователь не введет одну из дат, по умолчанию будут применены упомянутые значения. Актуальная на сегодня дата не взята намеренно, так как в задании нет информации о существовании или отсутствии будущих заказов.

4. Кроме того, для вывода домашней страницы был создан обработчик, который выводит перечень всех заказов. Непосредственно из домашней страницы пользователь имеет возможность создать, удалить и изменить заказы, произвести их фильтрацию и ознакомиться с информацией о конкретном заказе.
