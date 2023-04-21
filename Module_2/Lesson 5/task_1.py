# Задача 1: змоделювати залізницю, що працює за наступними правилами:
#
# Існує клас Вагон. Вагони бувають пасажирські, грузові та локомотиви. Ці три класи вагонів теж між собою відрізняються
# (грузовий вагон для сипучих грузів, для рідких etc).
#
# Всі Вагони мають спільні атрибути (для кожного Вагону задається ширина колії, для кожного Грузового Вагону задається
# вантажопідйомність ітд)
#
# Вагон + Вагон = Потяг. Потяг може складатися з будь якої кількості вагонів. Порядок вагонів важливий.
#
# Вагони додаються до Потягу оператором +.
# Потяг може їхати тільки якщо його першим або останнім елементом є Локомотив. Потяг має тільки 1 Локомотив.
#
# Потяг має метод Їхати, що здійснює переміщення потягу з одного міста в інше (міста задаються рядками).
# Потяг має задане поточне Місце Перебування. Тому, він може їхати тільки з поточного Місця Перебування
#
# Потяги їздять згідно Розкладу. Розклад - це список Рейсів, заданий для кожного Потягу (сприймате це як Dict[Train, List[Reis]].
# Кожен Рейс - це набір точки А, точки В і напрямку (А -> B, B -> A)
#
# Розкладом керує загальний клас Залізниця. Залізниця може створювати нові Потяги, змінювати спиок Рейсів для кожного з Потягів
# і здійснювати переміщення Потягу за допомогою триггеру методу Їхати.
#
# Потяг їде тільки якщо Рейс прийшов з валідними початковою та кінцевою точкою.

# Потяг має виводити поточний рейс, свій поточний склад Вагонів, свій номер, поточну точку перебування і статус (очікує початку рейсу чи їде)
