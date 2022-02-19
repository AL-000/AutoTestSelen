from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


def main():
    #запуск браузера и открытие страницы с кликом на "Обратная связь"
    driver = webdriver.Chrome()
    url = "https://zooshoptest.ru/"
    driver.get(url)
    element = driver.find_element_by_xpath("//a[text()='Обратная связь']").click()
    time.sleep(1)

    #Ввод Имени
    elements_name = driver.find_elements_by_xpath("//input[@name='name']")
    second_name = elements_name[1]
    second_name.click()
    second_name.clear()
    second_name.send_keys('Test')
    time.sleep(1)

    #Ввод Фамилии
    elements_lastname = driver.find_elements_by_xpath("//input[@name='lastname']")
    second_lastname = elements_lastname[1]
    second_lastname.click()
    second_lastname.clear()
    second_lastname.send_keys('Testov')
    time.sleep(2)

    #Ввод телефона
    elements_phone = driver.find_elements_by_xpath("//input[@name='phone']")
    second_phone = elements_phone[1]
    second_phone.click()
    second_phone.clear()
    second_phone.send_keys('8-333-444-44-44')
    time.sleep(2)

    #Проверка добавки второго телефона
    elements_phoneADD = driver.find_elements_by_xpath("//a[@class='b24-form-control-add-btn']")
    second_phoneADD = elements_phoneADD[1]
    second_phoneADD.click()

    #Ввод второго телефона
    elements_phone2 = driver.find_elements_by_xpath("//input[@name='phone']")
    third_phone2 = elements_phone2[2]
    third_phone2.click()
    third_phone2.clear()
    third_phone2.send_keys('8-555-555-55-55')
    time.sleep(1)

    #Ввод почты
    elements_email = driver.find_elements_by_xpath("//input[@name='email']")
    second_email = elements_email[1]
    second_email.click()
    second_email.clear()
    second_email.send_keys('test@mail.ru')
    time.sleep(2)

    #(JavaScriptExecutor) Нажатие кнопки вниз
    button_low = driver.find_element_by_xpath("//button[@class = 'b24-window-scroll-arrow-down']")
    driver.execute_script("arguments[0].click();", button_low)
    time.sleep(2)

    #Поле ввода текста (комментариев)
    element_comm = driver.find_elements_by_xpath("//textarea[@class = 'b24-form-control']")
    second_comm = element_comm[1]
    second_comm.click()
    second_comm.clear()
    second_comm.send_keys('test commente')
    time.sleep(2)

    # (JavaScriptExecutor) Нажатие чекбокса
    che_box = driver.find_elements_by_xpath("//input[@onclick='this.blur()']")
    che_box2 = che_box[1]
    driver.execute_script("arguments[0].click();", che_box2)
    time.sleep(2)

    # (JavaScriptExecutor) Нажатие стрелки вниз у чекбокс формы
    che_form = driver.find_elements_by_xpath("//div[@class='b24-form-scroll-textable-arrow-item']")
    che_form2 = che_form[1]
    driver.execute_script("arguments[0].click();", che_form2)
    time.sleep(2)

    # подтверждение чекбокса
    check_access = driver.find_elements_by_xpath("//button[contains(text(), 'Принимаю')]")
    check_access2 = check_access[1]
    driver.execute_script("arguments[0].click();", check_access2)
    time.sleep(2)

    # Нажатие кнопки отправить
    elem_comm = driver.find_elements_by_xpath("//button[contains(text(), 'Отправить')]")
    send_feed = elem_comm[2]
    send_feed.click()

    time.sleep(5)

main()
