from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    # Открыть страницу http://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)

# Посчитать сумму заданных чисел
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    z = int(x)+int(y)
    summ = str(z)
# Выбрать в выпадающем списке значение равное расчитанной сумме
    Select(browser.find_element(By.TAG_NAME, 'select')).select_by_visible_text(summ)

# Нажать кнопку "Submit"
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(20)
    browser.quit

