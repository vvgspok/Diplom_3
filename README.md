## Описание
Данный файл содержит функции для класса BasePage, LoginPage, MainPage, OrderFeedPage, ProfilePage, RecoverPage
Данный файл содержит тесты для класса TestMainFunctionalPage, TestOrderFeedPage, TestProfilePage, TestRecoverPage

## Функции для класса BasePage
### go_to_url 
Переходит по указанному адресу
### find_element_with_wait
Ожидает и находит видимый элемент
### wait_until_the_specified_text_disappears
Ждет пока заданный текст не исчезнет в элементе
### wait_until_the_specified_text_appears
Ждет пока заданный текст не появится в элементе
### click_to_element
Выполняет клик по элементу
### add_text_to_element
Вводит текст в поле
### get_text_from_element
Получает текст из элемента
### check_element_is_clickable
Проверяет кликабельность элемента 
### check_displaying_of_element
Проверяет отображение элемента
### drag_and_drop
Перетаскивает элемент 

## Функции для класса LoginPage
### auto_user
Авторизация юзера 

## Функции для класса MainPage
### go_to_constructor
Нажать на раздел Конструктор
### go_to_order_feed
Нажать на раздел Лента заказов
### go_to_profile 
Нажать на раздел Профиль

## Функции для класса OrderFeedPage
### create_burger_and_order
Собирает бургер и оформляет заказ 
### click_to_order
Нажимает на заказ в ленте заказов 

## Функции для класса ProfilePage
### click_go_to_order_history
Переходит на страницу история заказов пользователя
### click_logout_in_account
Нажимает на кнопку Выход

## Функции для класса RecoverPage
### go_to_page_password_recovery
Переходит на страницу восстановления пароля
### submit_recovery_email
Отправляет письмо на почту для восстановления
### fill_password_and_code_field
Заполняет поля пароль и код

## Тесты для класса TestMainFunctionalPage
### test_click_go_to_constructor
Тест проверяет переход по клику на Конструктор
### test_click_go_to_order_feed
Тест проверяет переход по клику на Лента заказов
### test_click_on_ingredient_opens_details_modal
Тест проверяет всплывающее окно с деталями, если кликнуть на ингредиент
### test_ingredient_modal_closes
Тест проверяет закрытие всплывающего окно с деталями при клике на крестик
### test_add_ingredient_increases_counter
Тест проверяет увеличение коунтера, при добавлении ингредиента в заказ
### test_authorized_user_can_create_order
Тест проверяет оформление заказа через залогиненного пользователя 

## Тесты для класса TestOrderFeedPage
### test_click_order_to_show_details
Тест проверяет клик на заказ, открывает всплывающее окно с деталями
### test_compare_orders_in_feed_and_history
Тест проверяет отображение заказа пользователя в разделе История заказов и на странице Лента заказов
### test_change_total_orders_counter
Тест проверяет увеличение счетчика "Выполнено за всё время" после создания нового заказа
### test_change_today_orders_counter
Тест проверяет увеличение счетчика "Выполнено за сегодня" после создания нового заказа
### test_order_in_progress
Тест проверяет наличие номера нового заказа в разделе "В работе"

## Тесты для класса TestProfilePage
### test_click_go_to_personal_account
Тест проверяет переход по клику на Личный кабинет
### test_go_to_order_history
Тест проверяет переход в раздел История заказов
### test_logout_in_account
Тест проверяет выход из аккаунта

## Тесты для класса TestRecoverPage
### test_go_to_password_recover
Тест проверяет переход на страницу восстановления пароля по кнопке "Восстановить пароль"
### test_filling_email_and_click_recover_button
Тест проверяет ввод почты и клик по кнопке "Восстановить"
### test_password_visibility_toggle
Тест проверяет подсвечивание поля при клике на "показать/скрыть"