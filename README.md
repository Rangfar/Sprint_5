Проект тестирует различные функциональные элементы веб-приложения Stellar Burgers

Расположение заданий и название функций их решения:
1)проверка успешной регистрации - test_registration.py  - test_succes_registration
2)проверка ошибки некорректного ввода пароля            - test_registration.py - test_incorrect_password_get_error_message

3)проверка входа по кнопке «Войти в аккаунт» на главной     - test_entry.py - test_button_login_your_account_in_main_page
4)проверка входа через кнопку «Личный кабинет»              - test_entry.py - test_button_personal_account_in_main_page
5)проверка входа через кнопку в форме регистрации           - test_entry.py - test_login_button_in_registration_page
6)проверка входа через кнопку в форме восстановления пароля - test_entry.py - test_login_button_in_forgot_password_page

7)проверка перехода по клику на «Личный кабинет» с главной страницы            - test_personal_account.py - test_go_to_lk_from_main_page_via_pesonal_account_button
8)проверка перехода из личного кабинета по клику на «Конструктор»              - test_personal_account.py - test_go_to_main_page_from_lk_with_click_designer_button
9)проверка перехода из личного кабинета по клику на на логотип Stellar Burgers - test_personal_account.py - test_go_to_main_page_from_lk_with_click_on_logo
10)проверка выхода из аккаунта по кнопке «Выйти» в личном кабинете             - test_personal_account.py - test_logout_in_lk

11)проверка перехода к разделу «Булки» в конструкторе главной страницы   - test_burger_designer.py - test_transition_to_bun
12)проверка перехода к разделу «Соусы» в конструкторе главной страницы   - test_burger_designer.py - test_transition_to_sauces
13)проверка перехода к разделу «Начинки» в конструкторе главной страницы - test_burger_designer.py - test_transition_to_toppings