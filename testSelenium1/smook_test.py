#импортируем трубуемые инструменты
import datetime

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#задаем рабочий браузер
driver = webdriver.Chrome()
driver.maximize_window()
#задаем требуемый сайт
url_var = 'https://www.saucedemo.com/'
driver.get(url_var)
#Задаем переменные для логина и пароля
user_name_var = 'standard_user'
password_var = 'secret_sauce'
#Вводим корректный логин и пароль пользователя
user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(user_name_var)
print('Введен логин')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_var)
print('Введен пароль')
#Кликаем по кнопке входа
login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
login_button.click()
print('Кнопка входа нажата, осуществлен вход')
#Сверяем адрес текущей страницы с адресом требуемой адресной строки
main_url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
assert main_url == get_url
#Делаем потверждающий скриншот c текущей датой
now_date = datetime.datetime.utcnow().strftime('%d.%m.%Y_%H.%M')
name_screen_main = f'Шаг_1_Вход {now_date}.png'
time.sleep(1)
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\Selenium\\smoke_test_shop-main\\smoke_test_shop-main\\'
                       'testSelenium1\\screen\\' + name_screen_main)
print('Вход подтвержден')
#Выбираем 1 продукт для добавление в корзину
product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_product_1 = product_1.text
print(value_product_1)
product_price_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = product_price_1.text
print(value_price_product_1)
#Кликаем на кнопку для добавления в корзину
add_to_cart_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
add_to_cart_product_1.click()
print(f'Товар {value_product_1} добавлен в корзину')
#Выбираем 2 продукт для добавление в корзину
product_2 = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
value_product_2 = product_2.text
print(value_product_2)
product_price_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div')
value_price_product_2 = product_price_2.text
print(value_price_product_2)
#Кликаем на кнопку для добавления в корзину
add_to_cart_product_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
add_to_cart_product_2.click()
print(f'Товар {value_product_2} добавлен в корзину')
#Переходим в корзину
cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
cart.click()
print('Переход в корзину прошел успешно')
name_screen_cart = f'Шаг_2_Корзина {now_date}.png'
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\Selenium\\smoke_test_shop-main\\smoke_test_shop-main\\'
                       'testSelenium1\\screen\\' + name_screen_cart)
#Сверяем названия в каталоге с названием в корзине 1 продукта
product_1_cart = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_product_1_cart = product_1_cart.text
print(value_product_1_cart)
assert value_product_1_cart == value_product_1
print('Продукт 1 соответствует выбранному')
#Сверяем названия в каталоге с названием в корзине 2 продукта
product_2_cart = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
value_product_2_cart = product_2_cart.text
print(value_product_2_cart)
assert value_product_2_cart == value_product_2
print('Продукт 2 соответствует выбранному')
#Сверяем цену товара 1 в корзине
product_price_1_cart = driver.find_element(By.XPATH,
                                           '//*[@id="cart_contents_container"]/div/div[1]/div[3]/'
                                           'div[2]/div[2]/div')
value_price_product_1_cart = product_price_1_cart.text
print(value_price_product_1_cart)
assert value_price_product_1_cart == value_price_product_1
print('Цена товара 1 в корзине соответствует')
#Сверяем цену товара 2 в корзине
product_price_2_cart = driver.find_element(By.XPATH,
                                           '//*[@id="cart_contents_container"]/div/div[1]/div[4]/'
                                           'div[2]/div[2]/div')
value_price_product_2_cart = product_price_2_cart.text
print(value_price_product_2_cart)
assert value_price_product_2_cart == value_price_product_2
print('Цена товара 2 в корзине соответствует')
#Продолжаем оформление заказа. Нажимаем на кнопку оформления заказа
checkout_btn = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout_btn.click()
#Вводим форму для формления заказа (Имя, Фамилия, Индекс почты)
first_name_var = "Иван"
last_name_var = 'Морозов'
postal_code_var = 12345
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys(first_name_var)
last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys(last_name_var)
postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
postal_code.send_keys(postal_code_var)
#Делаем скриншот заполненой формы
name_screen_cart = f'Шаг_3_Форма_заполнения_заказа {now_date}.png'
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\Selenium\\smoke_test_shop-main\\smoke_test_shop-main\\'
                       'testSelenium1\\screen\\' + name_screen_cart)
#Кликаем на кнопку продолжающий оформление заказа
continue_btn = driver.find_element(By.XPATH, '//input[@id="continue"]')
continue_btn.click()
#Делаем скриншот финишного этапа формления заказа
name_screen_cart = f'Шаг_4_Финиш {now_date}.png'
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\Selenium\\smoke_test_shop-main\\smoke_test_shop-main\\'
                       'testSelenium1\\screen\\' + name_screen_cart)
#Сверяем названия в финишной форме с каталогом и с названием в корзине 1 продукта
product_1_finish = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_product_1_finish = product_1_finish.text
print(value_product_1_finish)
assert value_product_1_finish == value_product_1 == value_product_1_finish
print('Названия в финишной форме с каталогом и с названием в корзине 1 продукта соответствует')
#Сверяем цену в финишной форме с каталогом и с названием в корзине 2 продукта
product_2_finish = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
value_product_2_finish = product_2_finish.text
print(value_product_2_finish)
assert value_product_2_cart == value_product_2 == value_product_2_finish
print('Цена в финишной форме с каталогом и с названием в корзине 2 продукта соответствует')
#Достаем стоимость вычесленную в финальной форме
price_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
price_total_value_finish = price_total.text
print(price_total_value_finish)
#Проведем сложение цен 1 товара и 2 товара. Уберем из строки с ценой знак $
value_price_product_1_finish = float(value_price_product_1.strip('$'))
value_price_product_2_finish = float(value_price_product_2.strip('$'))
total_value_price = f'Item total: ${value_price_product_1_finish + value_price_product_2_finish}'
print(total_value_price)
#Сверяем стоимость товаров
assert price_total_value_finish == total_value_price
print('Полная стоимость заказа верна')
#Оформляем заказ. Нажимаем на кнопку финального оформления заказа
btn_finish = driver.find_element(By.XPATH, '//button[@id="finish"]')
btn_finish.click()

#Сверяем адрес финиша оформления заказа с текущим адресом
finish_url = 'https://www.saucedemo.com/checkout-complete.html'
get_finish_url = driver.current_url
name_screen_cart = f'Шаг_5_Заказ_оформлен {now_date}.png'
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\Selenium\\smoke_test_shop-main\\smoke_test_shop-main\\'
                       'testSelenium1\\screen\\' + name_screen_cart)
assert finish_url == get_finish_url
print('Заказ создан')
#Нажимаем на кнопку возврата на главную страницу
btn_home = driver.find_element(By.XPATH, '//button[@id="back-to-products"]')
btn_home.click()
name_screen_cart = f'Шаг_6_Возврат_на_главную {now_date}.png'
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\Selenium\\smoke_test_shop-main\\smoke_test_shop-main\\'
                       'testSelenium1\\screen\\' + name_screen_cart)
back_home_url = main_url
get_back_home_url = driver.current_url
assert back_home_url == get_back_home_url
print('Возврат на главную страницу осуществлен успешно')