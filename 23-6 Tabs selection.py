from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #нажатие кнопки
    button = browser.find_element_by_css_selector('button.trollface')
    button.click()

    #переключение на новое окно
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #считаем по формуле число
    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)

    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

