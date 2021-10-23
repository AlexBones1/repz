from selenium import webdriver
import time 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input[placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[placeholder="Enter last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[placeholder="Enter email"]')
    input3.send_keys('Smolensk@sekr.com')

    input4 = browser.find_element_by_css_selector('input#file')
    input4.send_keys(r"C:\Users\alex\selen ex\ttk.txt")

    






    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
