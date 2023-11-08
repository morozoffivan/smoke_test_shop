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
name_screen_main = f'Вход {now_date}.png'
time.sleep(1)
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\pythonProject\\testSelenium1\\' + name_screen_main)
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
name_screen_cart = f'Корзина {now_date}.png'
driver.save_screenshot('C:\\Users\\ivanm\\PycharmProjects\\pythonProject\\testSelenium1\\' + name_screen_cart)
#Сверяем названия в каталоге с названием в корзине
